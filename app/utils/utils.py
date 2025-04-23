import requests
import pandas as pd
from io import StringIO
from bs4 import BeautifulSoup as bs

#Função generica de busca no site EMBRAPA
def get_data(url:str):
    """
    Realiza o scraping de uma tabela HTML a partir de uma URL e retorna os dados em formato de lista de dicionários.
    Args:
        url (str): URL da página contendo a tabela a ser extraída.

    Returns:
        list[dict]: Lista de dicionários com os dados da tabela ou uma mensagem indicando ausência de dados.

    Raises:
        ValueError: Se nenhuma tabela com a classe esperada for encontrada na página.
    """
    response = requests.get(url)
    html = response.text
    soup = bs(html,'html.parser')

    table = soup.find_all('table',class_='tb_base tb_dados')
    if not table:
        raise ValueError("Nenhuma tabela encontrada")

    table_html = StringIO(str(table))

    df = pd.read_html(table_html, flavor='bs4')[0]

    dict = df.to_dict(orient="records")
    valid = [v for k,v in dict[-1].items() if 'total' not in str(v).lower()]

    if '0' not in valid:
        data = df.to_dict(orient="records")
    else:
        data = [{'Response':'Sem dados para o Ano solicitado'}]

    return data