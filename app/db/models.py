from sqlalchemy import Column, Integer, String, Date, Time
from app.db.database import Base

class JogoHistorico(Base):
    __tablename__ = "jogos_historico"

    id = Column(Integer, primary_key=True, index=True)
    temporada = Column(Integer)
    rodada = Column(String)
    dia_semana = Column(String)
    data = Column(Date)
    hora = Column(Time, nullable=True)
    mandante = Column(String)
    visitante = Column(String)
    placar = Column(String)
    publico = Column(String, nullable=True)
    estadio = Column(String, nullable=True)

class JogoAtual(Base):
    __tablename__ = "jogos_atual"

    id = Column(Integer, primary_key=True, index=True)
    temporada = Column(Integer)
    rodada = Column(String)
    dia_semana = Column(String)
    data = Column(Date)
    hora = Column(Time, nullable=True)
    mandante = Column(String)
    visitante = Column(String)
    placar = Column(String, nullable=True)
    publico = Column(String, nullable=True)
    estadio = Column(String, nullable=True)   

