import requests
import pandas as pd
from io import StringIO
from bs4 import BeautifulSoup as bs

#Função generica de busca no site EMBRAPA
def get_data(url:str):
    response = requests.get(url)
    html = response.text
    soup = bs(html,'html.parser')

    table = soup.find_all('table',class_='tb_base tb_dados')
    if not table:
        raise ValueError(f"Nenhuma tabela encontrada")

    table_html = StringIO(str(table))

    df = pd.read_html(table_html, flavor='bs4')[0]

    dict = df.to_dict(orient="records")
    valid = [v for k,v in dict[-1].items() if 'total' not in str(v).lower()]

    if '0' not in valid:
        data = df.to_dict(orient="records")
    else:
        data = [{'Response':'Sem dados para o Ano solicitado'}]

    return data