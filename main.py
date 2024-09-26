from typing import Union
from bs4 import BeautifulSoup
from fastapi import FastAPI, Security
from requests import post, get
from fastapi import HTTPException
from functions import financiamentoPrestacoesFixas
from models import prestacoesFixas

app = FastAPI()

@app.get("/")
def root():
    return {"status": "OK"}


@app.post("/calculo")
def calculo_prestacao_fixas(request: prestacoesFixas):

    if not isinstance(request, prestacoesFixas):
        raise HTTPException(status_code=400, detail="Invalid request")

    return financiamentoPrestacoesFixas(request.meses, request.taxaJuros, request.valor)
