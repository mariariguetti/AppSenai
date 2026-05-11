import requests

base_url = "https://viacep.com.br/ws/"

def get_cep(cep):
    url = f"{base_url}{cep}/json"
    dados = requests.get(url)
    return dados.json()