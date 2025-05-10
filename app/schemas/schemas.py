from pydantic import BaseModel   
from typing import Literal
from fastapi import Path
from datetime import datetime


class SubProcessamento(BaseModel):
    ano:int = Path(..., ge=1900, le=datetime.now().year) 
    choice: Literal['viniferas',
                    'americanas_hibrida',
                    'uvas_mesa',
                    'sem_classificacao'] = 'viniferas'
    
class SubImportacao(BaseModel):
    ano:int = Path(..., ge=1900, le=datetime.now().year) 
    choice: Literal['vinhos_mesa',
                    'espumantes',
                    'uvas_frescas',
                    'uvas_passas',
                    'suco_uva'] = 'vinhos_mesa'

class SubExportacao(BaseModel):
    ano:int = Path(..., ge=1900, le=datetime.now().year) 
    choice: Literal['vinhos_mesa',
                    'espumantes',
                    'uvas_frescas',
                    'suco_uva'] = 'vinhos_mesa'