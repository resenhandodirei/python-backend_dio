import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

connection = sqlite3.connect(ROOT_PATH / 'my_database.sqlite')
cursor = connection.cursor()
cursor.row_factory = sqlite3.Row

def create_table(cursor):
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(100), email VARCHAR(150))'
    )
    connection.commit()

def registry(connection, cursor, name, email):
    data = (name, email)
    cursor.execute("INSERT INTO clients(name, email) VALUES(?, ?);", data)
    connection.commit()

def update_registry(connection, cursor, name, email, id):
    data = (name, email, id)
    cursor.execute('UPDATE clients SET name=?, email=? WHERE id=?;', data)
    connection.commit()

def delete_registry(connection, cursor, id):
    data = (id, )
    cursor.execute("DELETE FROM clients WHERE id=?;", data)
    connection.commit()

def insert_many(connection, cursor, dados):
    cursor.executemany('INSERT INTO clients (name, email) VALUES (?, ?)', dados)
    connection.commit()

def recuperate_clients(cursor, id):
    cursor.execute('SELECT * FROM clients WHERE id=?', (id,))
    result = cursor.fetchone()
    return result

def list_clients(cursor):
    cursor.execute('SELECT * FROM clients ORDER BY name DESC;')
    return cursor.fetchall()

# Cria a tabela
create_table(cursor)

# Dados a serem inseridos
dados = [
    ('Guilherme', 'gui@teste.com'),
    ('Larissa', 'larissa@exemplo.com'),
    ('João', 'joao@dominio.com'),
    ('Maria', 'maria@teste.com'),
    ('Carlos', 'carlos@exemplo.com'),
    ('Ana', 'ana@dominio.com'),
    ('Pedro', 'pedro@teste.com'),
    ('Fernanda', 'fernanda@exemplo.com'),
    ('Rafael', 'rafael@dominio.com'),
    ('Juliana', 'juliana@teste.com')
]

# Insere os dados
insert_many(connection, cursor, dados)

# Atualiza um registro
update_registry(connection, cursor, "Larissa", "larissa@teste.com", 1)

# Recupera um cliente específico
client = recuperate_clients(cursor, 1)
if client:
    print("Cliente recuperado:", {"id": client[0], "name": client[1], "email": client[2]})
else:
    print("Cliente com id 1 não encontrado.")

# Lista todos os clientes
clients = list_clients(cursor)
print("Lista de clientes:")
for client in clients:
    print({"id": client[0], "name": client[1], "email": client[2]})

id_client = input("Inform the client id: ")
cursor.execute(f"SELECT * FROM clients WHERE id=?", (id_client,))
client = cursor.fetchall()

for client in clients: 
    print(dict(client))


try: 
    cursor.execute("DELETE FROM clients WHERE id=8;")
    connection.commit()

    cursor.execute("INSERT INTO clients (name, email) VALUES (?, ?)"), ("Teste 3", "teste3@gmail.com")
    cursor.execute("INSERT INTO clients (name, email) VALUES (?, ?)"), ("Teste 4", "teste4@gmail.com")
    connection.commit()
except Exception as exc: 
    print(f"Ops! Um erro ocorreu! {exc}")
    connection.rollback()


# Fecha a conexão
connection.close()

