# wb-cat-api

## Sobre este repo


## Requisitos

Para usar esse repositório é necessário seguir os pré-requisitos listados abaixo:

| Name 	| Version 	|
|:----:	|---------	|
| Ubuntu | 18.04 + |
| Docker | 19.03 + |
| git    | 02.17 + |
| Docker Compose | 01.17 + |
| RAM | 8Gb +|

## Arquitetura da aplicação

Este projeto foi criado usandos:
- Flask : Um framework web para ser usado junto ao Python
- Python : Linguagem de programação
- MySQL : Banco de Dados
- ElasticSearch : Indexador de documentos 
- Kibana : Interface Web para o Elastic

Usando o Flask foi criado toda a aplicação WEB com algumas funções como por exemplo, buscar um gato de uma determinada raça, listar todas as origens de gatos, buscar imagem de gatos com chapéus dentre outras funções.

Usando o Python criamos o script que irá popular nosso banco de dados consumindo a API de Gatos

MySQL foi usado para armazenar todas as informações sobre os gatos 

ElasticSearch foi usado como ferramenta de Log e Auditoria 

Kibana foi usado para que o usuário possa interagir com os dados coletados e visualizar as LOGS que o sistema gerou e para acompanhar todas as atividades do sistema no Dashboard de 'monitoria'

Abaixo segue o fluxo que o projeto segue:


OBS: No elastic foi feito algumas mudanças em relação aos MAPPINGS para se adequar há aplicação a mudança no caso ocorreu no campo @timestamp que é criado como 'texto' e nós alteramos para date.

## Como usar

Basta executar o script na raiz do projeto [wb-cat.sh](./wb-cat.sh) esse script irá fazer todo o trabalho de *"start"* dos ambientes caso queira saber mais sobre a execução dele execute **wb-cat.sh --help ou -h**

## Manual

## Obrigado :)
Wallace Bruno Gentil
w.brunoge@gmail.com
