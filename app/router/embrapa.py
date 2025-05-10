from fastapi import APIRouter, Depends, Path
from http import HTTPStatus
from app.utils.utils import get_data, get_data_fallback, get_file_path
from app.schemas.schemas import SubProcessamento, SubImportacao, SubExportacao
from app.config.security import verify_token
from datetime import datetime
import logging

router = APIRouter()

@router.get("/")
async def home():
    """
    Página de boas vindas.

    """
    return "Bem Vindo a API Embrapa!"

@router.get('/embrapa-producao/{ano}',status_code=HTTPStatus.OK)
async def get_poducao(ano:int = Path(..., ge=1900, le=datetime.now().year), token: str = Depends(verify_token)):
    """
    Retorna dados da produção de vinhos, sucos e derivados do Rio Grande do Sul.

    Args:
        ano (int): Ano a ser consultado.
        token (str): Token JWT para autenticação, obtido via login. Fornecido automaticamente via Depends.

    Returns:
        list[dict]: Retorna os dados processados ou uma mensagem informando `Sem dados para o Ano solicitado`.
    """
    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02&ano={ano}'
    try:
        data = get_data(url)
        logging.warning("Rota Online")     
        return data
    except:
        path = get_file_path('files', 'Producao.csv')
        columns=['produto','Quantidade (L.)']
        delimiter = ';'
        data = get_data_fallback(path=path, filtro=ano, columns=columns, delimiter=delimiter)
        logging.warning(f"Rota Alternativa: {path}")   
        return data


@router.get('/embrapa-processamento/',status_code=HTTPStatus.OK)
async def get_processamento(itens:SubProcessamento = Depends(), token: str = Depends(verify_token)):
    """
    Retorna informações sobre quantidade de uvas processadas no Rio Grande do Sul.

    Args:
        itens (SubProcessamento): Objeto com o tipo de item ('choice') e o ano da consulta.
        token (str): Token JWT para autenticação, obtido via login. Fornecido automaticamente via Depends.

    Returns:
        list[dict]: Retorna os dados processados ou uma mensagem informando `Sem dados para o Ano solicitado`.
    """
    mapping = {
            "viniferas": "subopt_01",
            "americanas_hibrida": "subopt_02",
            "uvas_mesa": "subopt_03",
            "sem_classificacao": "subopt_04"
        }
    sub = mapping.get(itens.choice)

    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao={sub}&opcao=opt_03&ano={itens.ano}'
    data = get_data(url)    
    return data

@router.get('/embrapa-comercializacao/{ano}',status_code=HTTPStatus.OK)
async def get_comercializacao(ano:int = Path(..., ge=1900, le=datetime.now().year), token: str = Depends(verify_token)):
    """
    Retorna dados de comercialização de vinhos e derivados no Rio Grande do Sul.

    Args:
        ano (int): Ano a ser consultado.
        token (str): Token JWT para autenticação, obtido via login. Fornecido automaticamente via Depends.

    Returns:
        list[dict]: Retorna os dados processados ou uma mensagem informando `Sem dados para o Ano solicitado`.
    """
    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04&ano={ano}'
    data = get_data(url)    
    return data

@router.get('/embrapa-importacao/',status_code=HTTPStatus.OK)
async def get_importacao(itens:SubImportacao = Depends(), token: str = Depends(verify_token)):
    """
    Retorna dados sobre importação de derivados de uva.

    Args:
        itens (SubImportacao): Objeto com o tipo de item ('choice') e o ano da consulta.
        token (str): Token JWT para autenticação, obtido via login. Fornecido automaticamente via Depends.

    Returns:
        list[dict]: Retorna os dados processados ou uma mensagem informando `Sem dados para o Ano solicitado`.
    """
    mapping = {
            "vinhos_mesa": "subopt_01",
            "espumantes": "subopt_02",
            "uvas_frescas": "subopt_03",
            "uvas_passas": "subopt_04",
            "suco_uva": "subopt_05"
        }
    sub = mapping.get(itens.choice)

    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao={sub}&opcao=opt_05&ano={itens.ano}'
    data = get_data(url)    
    return data


@router.get('/embrapa-exportacao/',status_code=HTTPStatus.OK)
async def get_exportacao(itens:SubExportacao = Depends(), token: str = Depends(verify_token)):
    """
    Retorna dados de exportação de derivados de uva.

    Args:
        itens (SubExportacao): Objeto com o tipo de item ('choice') e o ano da consulta.
        token (str): Token JWT para autenticação, obtido via login. Fornecido automaticamente via Depends.

    Returns:
        list[dict]: Retorna os dados processados ou uma mensagem informando `Sem dados para o Ano solicitado`.
    """
    mapping = {
            "vinhos_mesa": "subopt_01",
            "espumantes": "subopt_02",
            "uvas_frescas": "subopt_03",
            "suco_uva": "subopt_04"
        }
    sub = mapping.get(itens.choice)

    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao={sub}&opcao=opt_06&ano={itens.ano}'
    data = get_data(url)    
    return data