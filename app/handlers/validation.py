from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from http import HTTPStatus

async def validation_handler(request: Request, exc: RequestValidationError):
    """
    Manipula erros de validação de requisições da API.

    Args:
        request (Request): A requisição que gerou o erro.
        exc (RequestValidationError): Detalhes do erro de validação.

    Returns:
        JSONResponse: Resposta com código HTTP 422 e mensagem customizada.
    """
    return JSONResponse(
        status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        content={"detail": "Ano inválido. Insira um ano entre 1900 e o ano atual."}
    )
