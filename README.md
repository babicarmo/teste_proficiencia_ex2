# Exercício 2 - Teste de Proficiência

Este repositório contém o **Exercício 2** do teste de proficiência, que analisa blocos de carnaval do Rio de Janeiro em 2018.

## Objetivo

Filtrar blocos por bairro e exibir a lista de blocos por dia utilizando Python e Pandas. O usuário também pode optar por exportar os resultados para CSV.

## Estrutura do projeto

exercicio2/
    dados/
        blocos_carnaval_2018.csv # Arquivo de dados
script_exercicio2.py # principal 


## Como usar

1. Execute o script `script_exercicio2.py` no Python.
2. Digite o nome do bairro quando solicitado.
3. O script exibirá os blocos por dia no bairro informado.
4. Opcionalmente, você pode exportar o resultado para CSV.

## Observações

- O script ignora diferenças entre maiúsculas e minúsculas ao filtrar o bairro.
- O arquivo CSV exportado terá o nome `blocos_<bairro>.csv`.
