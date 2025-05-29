# API de Scraping - Vitivinicultura Embrapa

## Diagrama da Arquitetura
<img src='https://github.com/ManoelSa/api-embrapa/blob/main/diagrama_embrapa.PNG'>

## Objetivo

Esta API realiza o scraping de informações disponíveis no portal da Embrapa sobre a vitivinicultura no Brasil, com foco especial nos dados do Estado do Rio Grande do Sul — responsável por mais de 90% da produção nacional. Através de endpoints organizados por categoria, a aplicação permite consultar dados estruturados sobre produção, processamento, comercialização, importação e exportação de uvas, vinhos, sucos e derivados.

## Visão Geral

O site original apresenta os dados de forma tabular e estática, dificultando seu consumo por aplicações automatizadas. Esta API extrai essas informações diretamente das páginas:

- [`Produção`](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02)
- [`Processamento`](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03)
- [`Comercialização`](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04)
- [`Importação`](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05)
- [`Exportação`](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06) 

Através da API, os dados são disponibilizados em formato JSON, facilitando seu consumo por dashboards, ferramentas analíticas, bancos de dados e integrações com outros sistemas.

## Principais Funcionalidades

- 🍇 Extração automatizada dos dados da vitivinicultura brasileira diretamente do site da Embrapa  
- 🚀 Backend em FastAPI. 
- 🔄 Dados organizados por categoria: produção, processamento, comercialização, importação e exportação  
- 📤 Respostas em JSON estruturado, prontas para consumo  
- 🔧 Código modular e fácil de manter  
- 🔐 Autenticação com **usuário e senha via JWT**, exigida para acessar qualquer endpoint 
- ❌ Tratamento básico de exceções para falhas na página ou dados inconsistentes  

## Detalhes de Implementação

- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)  
- **Scraping:** `requests`, `BeautifulSoup` e `pandas` para leitura e tratamento das tabelas HTML.
- **Autenticação:**  
  - Login via `POST /login` com `username` e `password`  
  - Geração de token JWT válido por tempo limitado  
  - Todos os endpoints de dados requerem o token no header `Authorization: Bearer <token>`  
- **Endpoints disponíveis:**  
  - `GET /embrapa-producao` — Retorna dados da produção de vinhos, sucos e derivados do Rio Grande do Sul. 
  - `GET /embrapa-processamento` — Informações sobre quantidade de uvas processadas no Rio Grande do Sul.  
  - `GET /embrapa-comercializacao` — Dados de comercialização de vinhos e derivados no Rio Grande do Sul.  
  - `GET /embrapa-importacao` — Dados sobre importação de derivados de uva.  
  - `GET /embrapa-exportacao` — Dados de exportação de derivados de uva.  
- **Formato de resposta:** JSON  
- **Hospedagem:** A API está disponível publicamente via [Vercel](https://vercel.com/) para fins de estudo e experimentação. 
- **Foco geográfico:** Estado do **Rio Grande do Sul**, conforme dados da fonte

## Fluxo de Autenticação e Acesso

```text
[Usuário] --(username/password)--> /login 
          <-- access_token

[Usuário] --(Authorization: Bearer <token>)--> /<rota>
              |
              v
     [verify_token] valida o token
              |
              v
     [endpoint] executa scraping e retorna dados em JSON

```
## Exemplos de uso Localmente 

```bash
# 1. Clone o repositório
git clone https://github.com/ManoelSa/api-embrapa.git
cd seu-repositorio

# 2. (Opcional) Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure as variáveis de ambiente (exemplo em .env criado na raiz do projeto)
APP_USER='<seu_usuario>'
APP_PASS='<sua_senha>'
SECRET_KEY='<sua_key>'
ALGORITHM='HS256'
ACCESS_TOKEN_EXPIRE_MINUTES=15

# 5. Execute o servidor FastAPI
uvicorn main:app --reload
```
## Possível erro ao Iniciar o Seridor Local 
```python
# Em caso de erros ao inciar o servidor, altere os imports
# main.py
# DE:
from app.router import embrapa
from app.config import security
from app.handlers.validation import validation_handler

# PARA:
from router import embrapa
from config import security
from handlers.validation import validation_handler

# embrapa.py
# DE:
from app.utils.utils import get_data
from app.schemas.schemas import SubProcessamento, SubImportacao, SubExportacao
from app.config.security import verify_token

# PARA:
from utils.utils import get_data
from schemas.schemas import SubProcessamento, SubImportacao, SubExportacao
from config.security import verify_token

```
## Documentação e Testes

### Documentação Local

Após iniciar o servidor localmente, você pode acessar a documentação interativa da API:

- **API Local**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Documentação Swagger**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Documentação Redoc (alternativa)**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Documentação Online

Se preferir acessar a API e a documentação diretamente na versão hospedada, acesse:

- **API Online**: [https://api-embrapa-gamma.vercel.app](https://api-embrapa-gamma.vercel.app)
- **Documentação Swagger**: [https://api-embrapa-gamma.vercel.app/docs](https://api-embrapa-gamma.vercel.app/docs)
- **Documentação Redoc (alternativa)**: [https://api-embrapa-gamma.vercel.app/redoc](https://api-embrapa-gamma.vercel.app/redoc)

## Exemplos de chamadas à API com Python 
🔐 1. Obter Token de Autenticação (Login):

```python
import requests

login = 'https://api-embrapa-gamma.vercel.app/login'

data = {
    "username": "seu_usuario",
    "password": "sua_senha"
}

response = requests.post(url=login, data=data)
token = response.json()['access_token']

print("Token JWT:", token)

```
📥 2. Consulta aos dados protegidos (GET com Token)

```python
import requests

url_get = 'https://api-embrapa-gamma.vercel.app/embrapa-producao/{ano}'

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(url=url_get, headers=headers)
dados = response.json()
```
---

> ℹ️ _Aviso: Esta API tem fins educacionais e informativos. Certifique-se de que o uso respeita os termos e a política de dados da Embrapa._


