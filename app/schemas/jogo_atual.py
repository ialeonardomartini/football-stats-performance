from pydantic import BaseModel
from datetime import date, time

class JogoAtualSchema(BaseModel):
    temporada: int
    rodada: str
    dia_semana: str
    data: date
    hora: time | None
    mandante: str
    visitante: str
    placar: str | None
    publico: str | None
    estadio: str | None

    class Config:
        from_attributes = True