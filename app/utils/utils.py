import requests
import pandas as pd
import os
from io import StringIO
from bs4 import BeautifulSoup as bs

#Função generica de busca no site EMBRAPA
def get_data(url:str) -> list[dict]:
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
        data = df[:-1].to_dict(orient="records")
    else:
        data = [{'Response':'Sem dados para o Ano solicitado'}]

    return data

#Função generica para uso em Fallback
def get_data_fallback(path: str, filtro: int , columns: list[str], delimiter: str) -> list[dict]:
            """
            Lê um CSV usado de Fallback e retorna dados filtrando colunas que contenham o valor do parâmetro `filtro`.
            
            Args:
                path (str): Caminho do arquivo CSV.
                filtro (int): Valor usado para filtrar colunas (ex: ano).
                columns (list[str]): Nomes finais das colunas.
                delimiter (str): Delimitador do CSV.

            Returns:
                list[dict]: Dados formatados. Retorna uma mensagem padrão se houver erro.
            """
            try:
                df = pd.read_csv(path, sep=delimiter)
                select = [columns[0]] + [col for col in df.columns if str(filtro) in col]
                df = df[select]
                df.columns = columns
                return df.to_dict(orient="records")                
            except:
               return [{'Response':'Sem dados para o Ano solicitado'}]

#Define a raiz do projeto, subindo um nível a partir da pasta atual
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def get_file_path(*subpaths) -> str:
    """
    Gera caminho absoluto a partir da raiz do projeto.
    """
    return os.path.join(BASE_DIR, *subpaths)