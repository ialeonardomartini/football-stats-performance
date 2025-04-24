from sqlalchemy.orm import Session
from datetime import datetime

from app.db.models import JogoHistorico
from app.schemas.jogo_historico import JogoHistoricoSchema

from app.db.models import JogoAtual
from app.schemas.jogo_atual import JogoAtualSchema

def salvar_jogo_historico(db: Session, jogo: JogoHistoricoSchema):
    db_jogo = JogoHistorico(
        temporada=jogo.temporada,
        rodada=jogo.rodada,
        dia_semana=jogo.dia_semana,
        data=jogo.data,
        hora=jogo.hora,
        mandante=jogo.mandante,
        visitante=jogo.visitante,
        placar=jogo.placar,
        publico=jogo.publico,
        estadio=jogo.estadio
    )
    db.add(db_jogo)
    db.commit()

def salvar_jogo_atual(db: Session, jogo: JogoAtualSchema):
    db_jogo = JogoAtual(
        temporada=jogo.temporada,
        rodada=jogo.rodada,
        dia_semana=jogo.dia_semana,
        data=jogo.data,
        hora=jogo.hora,
        mandante=jogo.mandante,
        visitante=jogo.visitante,
        placar=jogo.placar,
        publico=jogo.publico,
        estadio=jogo.estadio
    )
    db.add(db_jogo)
    db.commit()