import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime
from flask_migrate import Migrate
import sqlalchemy as sa
import click

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
migrate = Migrate()


class User(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(sa.String, unique=True, nullable=False)

    active: Mapped[bool] = mapped_column(sa.Boolean, default=True)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r})"


class Post(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    title: Mapped[str]=mapped_column(sa.String, nullable=False)
    body: Mapped[str] = mapped_column(sa.String, nullable=False)
    created: Mapped[datetime] = mapped_column (sa.DateTime, server_default=sa.func.now())
    author_id: Mapped[int] = mapped_column(sa.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f"Post(id={self.id!r}, title={self.title!r}, author_id={self.author_id!r})"

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # Use o diretório da instância para o banco de dados
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(app.instance_path, 'blog.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False  # Desativa o rastreamento de modificações
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # Garante que o diretório da instância exista
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Registra comandos CLI
    app.cli.add_command(init_db_command)


    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)

    from src.controllers import user

    app.register_blueprint(user.app)

    return app

@click.command('init-db')
def init_db_command():
    """Limpa os dados existentes e cria novas tabelas."""
    app = create_app()
    with app.app_context():
        db.create_all()
    click.echo('Banco de dados inicializado.')

