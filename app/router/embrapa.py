from fastapi import APIRouter, Depends
from http import HTTPStatus
from app.utils.utils import get_data
from app.schemas.schemas import SubProcessamento, SubImportacao, SubExportacao
from app.config.security import verify_token
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@router.get("/")
async def home():
    return "Bem Vindo a API Embrapa!"

@router.get('/embrapa-producao/{ano}',status_code=HTTPStatus.OK)
async def get_poducao(ano:int, token: str = Depends(oauth2_scheme)):
    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02&ano={ano}'
    data = get_data(url)    
    return data


@router.get('/embrapa-processamento/',status_code=HTTPStatus.OK)
async def get_processamento(itens:SubProcessamento = Depends()):
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
async def get_comercializacao(ano:int):
    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04&ano={ano}'
    data = get_data(url)    
    return data

@router.get('/embrapa-importacao/',status_code=HTTPStatus.OK)
async def get_importacao(itens:SubImportacao = Depends()):
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
async def get_exportacao(itens:SubExportacao = Depends()):
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