# Quality Assurance Developer - Desafio Técnico
## Qual o desafio?
1. Construção de cenários de teste e automação para SPA (Single Page Application)
1. Construção de cenários de teste e automação para API REST

- Para o desafio 1 foi utilizado a página de inscrição [aqui](https://staging.app.betrybe.com/registration)

- Para o desafio 2 foi utilizado a api disponível [aqui](https://github.com/workforce-data-initiative/skills-api/wiki/API-Overview)

## Documentação
- A automatização foi feita utilizando a linguagem Python 3.8, com as bibliotecas Selenium, Unittest, Request e Docker.
- Para o desafio 1, optei por documentá-lo numa planilha disponível [aqui](https://docs.google.com/spreadsheets/d/1hcY6FdQRpDHv2tyX1igscUWxdQNrfLTO_6LdIl6lGTc/edit#gid=0)
- Para o desafio 2, segue a documentação:

- Foi utilizado o endpoint: `/jobs/autocomplete`
  - `200` - Foi encontrado a coleção de job titles que corresponde com a busca;
  - `400` - Request mal formulado, faltando parâmetros ou parâmtro incorreto;
  - `404` - Não foi encontrado a coleção de job titles que corresponde com a busca
  - Utilizei a string `soft` para as requests





|TITULO|DESCRIÇÃO|RESULTADO ESPERADO|RESULTADO OBTIDO|STATUS|
| --- | --- | --- | --- | --- |
|Teste API 1|Teste da API com uma requisição correta, usando o parâmetro begins_with|Recebimento do código 200|Recebido o código 200| Aprovado|
|Teste API 2|Teste da API com uma requisição correta, usando o parâmetro contains|Recebimento do código 200|Recebido o código 200| Aprovado|
|Teste API 3|Teste da API com uma requisição correta, usando o parâmetro ends_with|Recebimento do código 404|Recebido o código 404| Aprovado|
|Teste API 4|Teste da API sem especificar nenhum parâmetro|Recebimento do código 400|Recebido o código 400| Aprovado|
|Teste API 5|Teste da API procurando um job que não existe na API|Recebimento do código 404|Recebido o código 404| Aprovado|

- Foram realizados 23 testes no total com 3 erros indentificados.