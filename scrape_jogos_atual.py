import requests
from bs4 import BeautifulSoup
from datetime import datetime
from sqlalchemy.orm import Session

from app.db.database import SessionLocal, engine
from app.db.models import JogoAtual, Base
from app.db.crud import salvar_jogo_atual
from app.schemas.jogo_atual import JogoAtualSchema

# ⚠️ RECRIA a tabela do zero
print("🧨 Apagando e recriando tabela jogos_temporada_atual...")
JogoAtual.__table__.drop(bind=engine, checkfirst=True)
JogoAtual.__table__.create(bind=engine, checkfirst=True)

db: Session = SessionLocal()

temporada = 2025
url = "https://fbref.com/pt/comps/24/cronograma/Serie-A-Resultados-e-Calendarios"
table_id = "sched_2025_24_1"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

print(f"\n📅 Raspando temporada atual {temporada}...")

try:
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    tabela = soup.find("table", {"id": table_id})
    if not tabela:
        print(f"⚠️ Tabela não encontrada para temporada atual.")
    else:
        linhas = tabela.find("tbody").find_all("tr")

        for linha in linhas:
            try:
                def clean(text):
                    return text.strip() if text else None

                rodada = clean(linha.find(["td", "th"], {"data-stat": "gameweek"}).text)
                if not rodada:
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

                jogo = JogoAtualSchema(
                    temporada=temporada,
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

                salvar_jogo_atual(db, jogo)

            except Exception as e:
                print(f"❌ Erro ao processar jogo: {e}")
                continue

except Exception as e:
    print(f"❌ Erro ao acessar a temporada atual: {e}")

db.close()
print("\n✅ Temporada atual 2024 salva com sucesso.")
