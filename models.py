from pydantic import BaseModel, Field


class prestacoesFixas(BaseModel):
    meses: int = Field(..., ge=1)
    taxaJuros: float = Field(..., ge=0)
    valor: float = Field(..., ge=0)

# test
r = prestacoesFixas(meses=12, taxaJuros=0.02, valor=500)
