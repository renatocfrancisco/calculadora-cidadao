# calculadora-cidadao

![Python](https://img.shields.io/badge/Python-FFD43B?style=flat&logo=python&logoColor=blue) ![Github Copilot](https://img.shields.io/badge/Copilot-000000?style=flat&logo=githubcopilot&logoColor=white) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


Financiamento de Prestações Fixas

![Calculo - q0 = (((1 - (1 + j) ** -n)) / j) * p](img/image_calc_met_financiamento.png)

Fonte: [bcb.gov.br](https://www3.bcb.gov.br/CALCIDADAO/publico/exibirMetodologiaFinanciamentoPrestacoesFixas.do?method=exibirMetodologiaFinanciamentoPrestacoesFixas)

## Comandos

```shell
uv init
uv add fastapi[all]
uv run uvicorn main:app
```

```shell
python -m venv venv
venv\Scripts\activate
pip install fastapi[all]
uvicorn main:app
````

