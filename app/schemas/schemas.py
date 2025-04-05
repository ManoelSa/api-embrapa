from pydantic import BaseModel   
from typing import Literal


class SubProcessamento(BaseModel):
    ano:int
    choice: Literal['viniferas',
                    'americanas_hibrida',
                    'uvas_mesa',
                    'sem_classificacao'] = 'viniferas'
    
class SubImportacao(BaseModel):
    ano:int
    choice: Literal['vinhos_mesa',
                    'espumantes',
                    'uvas_frescas',
                    'uvas_passas',
                    'suco_uva'] = 'vinhos_mesa'

class SubExportacao(BaseModel):
    ano:int
    choice: Literal['vinhos_mesa',
                    'espumantes',
                    'uvas_frescas',
                    'suco_uva'] = 'vinhos_mesa'