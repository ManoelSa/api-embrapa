# API de Scraping - Vitivinicultura Embrapa

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
  - `GET /embrapa-exportacao` — Dados de exportação de derivados de uva  
- **Formato de resposta:** JSON  
- **Hospedagem:** A API está disponível publicamente via [Vercel](https://vercel.com/) para fins de estudo e experimentação. 
- **Foco geográfico:** Estado do **Rio Grande do Sul**, conforme dados da fonte

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

url_get = 'https://api-embrapa-gamma.vercel.app/embrapa-producao/2021'

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(url=url_get, headers=headers)
dados = response.json()
```
---

> ℹ️ _Aviso: Esta API tem fins educacionais e informativos. Certifique-se de que o uso respeita os termos e a política de dados da Embrapa._


