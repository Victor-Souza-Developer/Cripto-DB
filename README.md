 -> Crypto Market Tracker

 Projeto backend desenvolvido em Python para coleta, persistência e visualização de dados do mercado de criptomoedas.

## Objetivo ##

 Consumir dados de criptomoedas em tempo real através da API da CoinGecko, armazenar historicamente em PostgreSQL e futuramente disponibilizar dashboards interativos.

## Demonstração Online ##

 Acesse a aplicação:
 
 https://cripto-db-production-2bdb.up.railway.app/

## Funcionalidade ##

 - Coleta automática de dados da CoinGecko
 
 - Armazenamento histórico em PostgreSQL
 
 - Dashboard interativo com Streamlit
 
 - Visualização de preços por criptomoeda
 
 - Indicadores de variação nas últimas 24 horas
 
 - Atualização periódica dos dados

## Tecnologias ##

 - Python
 - Requests
 - PostgreSQL
 - Docker
 - DBeaver
 - Streamlit (em desenvolvimento)

## Arquitetura ##

 O projeto segue princípios de Clean Architecture:
 
 ```text
 src/
 ├── main/         # orquestração da aplicação
 ├── domain/       # entidades e regras de negócio
 ├── use_cases/    # casos de uso
 ├── infra/        # banco de dados e APIs externas
 ├── interfaces/   # interfaces futuras (API/Dashboard)

