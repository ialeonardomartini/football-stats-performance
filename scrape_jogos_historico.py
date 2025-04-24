import requests
from bs4 import BeautifulSoup
from datetime import datetime
from sqlalchemy.orm import Session

from app.db.database import SessionLocal, engine
from app.db.models import JogoHistorico, Base
from app.db.crud import salvar_jogo_historico
from app.schemas.jogo_historico import JogoHistoricoSchema

# ⚠️ RECRIA a tabela do zero
print("🧨 Apagando e recriando tabela jogos_resultados...")
JogoHistorico.__table__.drop(bind=engine, checkfirst=True)
JogoHistorico.__table__.create(bind=engine, checkfirst=True)

db: Session = SessionLocal()

for ano in range(2014, 2025):
    print(f"\n📅 Raspando temporada {ano}...")
    url = f"https://fbref.com/pt/comps/24/{ano}/cronograma/{ano}-Serie-A-Resultados-e-Calendarios"
    table_id = f"sched_{ano}_24_1"

    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        tabela = soup.find("table", {"id": table_id})
        if not tabela:
            print(f"⚠️ Tabela não encontrada para {ano}")
            continue

        linhas = tabela.find("tbody").find_all("tr")

        for linha in linhas:
            try:
                def clean(text):
                    return text.strip() if text else None

                def to_int(txt):
                    if txt:
                        txt = txt.replace(".", "").replace(",", "")
                        return int(txt) if txt.isdigit() else None
                    return None

                rodada = clean(linha.find(["td", "th"], {"data-stat": "gameweek"}).text)
                if not rodada or not rodada.isdigit():
                    continue
                dia_semana = clean(linha.find(["td", "th"], {"data-stat": "dayofweek"}).text)
                data_str = clean(linha.find(["td", "th"], {"data-stat": "date"}).text)
                hora_str = clean(linha.find(["td", "th"], {"data-stat": "start_time"}).text)
                mandante = clean(linha.find(["td", "th"], {"data-stat": "home_team"}).text)
                visitante = clean(linha.find(["td", "th"], {"data-stat": "away_team"}).text)
                placar = clean(linha.find(["td", "th"], {"data-stat": "score"}).text)
                publico = clean(linha.find(["td", "th"], {"data-stat": "attendance"}).text)
                estadio = clean(linha.find(["td", "th"], {"data-stat": "venue"}).text)

                data = datetime.strptime(data_str, "%Y-%m-%d").date() if data_str else None
                hora = datetime.strptime(hora_str, "%H:%M").time() if hora_str else None

                jogo = JogoHistoricoSchema(
                    temporada=ano,
                    rodada=rodada,
                    dia_semana=dia_semana,
                    data=data,
                    hora=hora,
                    mandante=mandante,
                    visitante=visitante,
                    placar=placar,
                    publico=publico,
                    estadio=estadio
                )

                salvar_jogo_historico(db, jogo)

            except Exception as e:
                print(f"❌ Erro ao processar jogo ({ano}): {e}")
                continue

    except Exception as e:
        print(f"❌ Erro ao acessar temporada {ano}: {e}")
        continue

db.close()
print("\n✅ Dados históricos de 2014 a 2024 salvos com sucesso.")
