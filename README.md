
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
| `flask --app src.app db init` | 
| `flask --app src.app db migrate -m "Initial migration"` | 
| `flask --app src.app db upgrade` | 
| `flask --app src.app db migrate -m "Add active attr in user."`| 
| `poetry add 'flask-jwt-extended=*'` | download do jwt | 


### Diferença entre patch e put
| Parâmetro     | Descrição                           |
| :---------- | :---------------------------------- |
| PATCH | alteração parcial |
| PUT| você fala para o usuário que vai atualizar o objeto inteiro |

### Diferença entre autenticação e autorização
| Parâmetro     | Descrição                           |
| :---------- | :---------------------------------- |
| Autenticação | processo de verificar a identidade de um usuário. É feito por meio de um nome de usuário e de senha, mas também pode incluir outros métodos, como tokens ou impressões digitais. |
| Autorização | a autorização determina quais recursos um usuário autenticado tem permissão para acessar. É sobre o que você está autorizado a fazer. |


### O que é JWT (JSON Web Tokens)?
É um padrão aberto (RFC 7519) que define uma maneira compacta e independente de transmitir informações de forma segura entre as partes como um objeto JSON. 

#### Características do JWT
Compacto: Pode ser enviado através de uma URL, parâmetro POST ou no cabeçalho HTTP. 

Autocontido: A carga útil contém todas as informações necessárias sobre o usuário, evitando a necessidade de consultar o banco de dados mais de uma vez.

### Terminal python 
| Comando     | Descrição                           |
| :---------- | :---------------------------------- |
| exit() | para sair do prompt do python e voltar ao terminal |
| quit() | para sair do prompt do python e voltar ao terminal |
| ctrl + D | para sair do prompt do python e voltar ao terminal |