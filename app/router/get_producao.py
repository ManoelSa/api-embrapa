import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from io import StringIO
from fastapi import APIRouter
from http import HTTPStatus

router = APIRouter()


@router.get('/embrapa-producao/{ano}',status_code=HTTPStatus.OK)
def get_poducao(ano:int):
    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02&ano={ano}'

    response = requests.get(url)
    html = response.text
    soup = bs(html,'html.parser')

    table = soup.find_all('table',class_='tb_base tb_dados')
    if not table:
        raise ValueError(f"Nenhuma tabela encontrada para o ano {ano}")

    table_html = StringIO(str(table))

    table_html = StringIO(str(table))
    df = pd.read_html(table_html, flavor='bs4')[0]
    valida = df.rename(columns={'Quantidade (L.)':'qtd'})
    if len(valida.query("Produto == 'Total' and qtd > '0'")):
        dicionario = df.to_dict(orient="records")
    else:
        dicionario = [{'Response':'Sem dados para o Ano solicitado',
                       'Resumo':{'Ano':ano,'Total Registros':0}}]

    #dicionario = df.to_dict(orient="records")
    return dicionario