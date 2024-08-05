
## O que é blueprint no Flask?
- Conceito mais avançado
- A ideia de criar um arquivo na pasta de controllers e comece a declarar todas as nossas rotas específicas por módulos. 
- Na documentação do flask, fala-se em blueprints e views. Pasta de controller: roteamento de rotas. Pasta de view: modelo de resposta.


## Expressões no código


| Parâmetro     | Descrição                           |
| :---------- | :---------------------------------- |
| `nullable` | Não permite números nulos |
|`ForeignKey`| Tipo para representar a chave estrangeira |
| `.scalars` | acessa o primeiro índice da tupla e vai retornar o objeto para dentro dessa tupla. 

## Comandos

| Parâmetro     | Descrição                           |
| :---------- | :---------------------------------- |
| `poetry run flask --app app run` | roda o flask no poetry | 
| `poetry run flask --app app run --debug`| roda o servidor com o debugg funcionando
| `poetry run flask --app src.app run --debug ` | roda o servidor com debugg funcionando dentro da pasta src 
| `poetry run flask --app src.app init-db` | inicializa o banco de dados dentro da pasta src, especificamente o arquivo app |


### Diferença entre patch e put
| Parâmetro     | Descrição                           |
| :---------- | :---------------------------------- |
| PATCH | alteração parcial |
| PUT| você fala para o usuário que vai atualizar o objeto inteiro |
