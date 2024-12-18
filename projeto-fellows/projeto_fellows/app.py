from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


# Inicialização do Flask e das extensões
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fellows.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'sua_chave_secreta'

# Inicializa o banco de dados e o Bcrypt
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Importa as rotas
from projeto_fellows import views

if __name__ == "__main__":
    app.run(debug=True)

