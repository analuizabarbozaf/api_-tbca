from fastapi import FastAPI, HTTPException
import requests
app = FastAPI()
TBCA_URL = "https://www.tbca.net.br/base-dados/composicao_alimentos.php"
@app.get("/buscar")
def buscar_alimento(nome: str):
    try:
        # Simula uma consulta à TBCA (a API oficial da TBCA não é aberta)
        response = requests.get(TBCA_URL)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Erro ao acessar TBCA")
        # Aqui precisaria de um scraper real para extrair os dados certos da TBCA
        dados_mock = {
            "nome": nome,
            "quantidade": "100g",
            "carboidratos": 25,
            "proteinas": 10,
            "lipidios": 5,
            "medida_caseira": [
                {"tipo": "unidade", "peso": "80g"},
                {"tipo": "fatia", "peso": "30g"},
                {"tipo": "colher de sopa", "peso": "15g"}
            ]
        }
        return {"status": "sucesso", "dados": dados_mock}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))