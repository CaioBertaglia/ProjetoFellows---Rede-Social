from flask import Blueprint, render_template, request, redirect, flash, url_for
from projeto_fellows import db, bcrypt
from projeto_fellows.models import Usuario, Empresa
import os

# Define o Blueprint para as rotas
views = Blueprint('views', __name__)

# Página inicial
@views.route("/")
def home():
    return render_template("fellows.html")

# Cadastro de Pessoa Física ou Jurídica
@views.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form['name']
        email = request.form['email']
        senha = request.form['password']
        tipo = request.form['type']
        senha_hash = bcrypt.generate_password_hash(senha).decode('utf-8')

        # Criar novo usuário
        novo_usuario = Usuario(nome=nome, email=email, senha=senha_hash, tipo=tipo)
        db.session.add(novo_usuario)
        db.session.commit()

        # Redireciona para o cadastro de jurídica ou modal de sucesso
        if tipo == "juridica":
            return redirect(url_for("views.cadastro_juridica", user_id=novo_usuario.id))
        else:
            flash("Cadastro realizado com sucesso!", "success")
            return render_template("cadastro.html")

    return render_template("cadastro.html")

# Cadastro de Pessoa Jurídica
@views.route("/cadastro-juridica/<int:user_id>", methods=["GET", "POST"])
def cadastro_juridica(user_id):
    if request.method == "POST":
        razao_social = request.form['razao-social']
        cnpj = request.form['cnpj']
        cnpj_file = request.files['cnpj-file']

        # Salvar o arquivo
        file_path = os.path.join("static/uploads", cnpj_file.filename)
        cnpj_file.save(file_path)

        # Criar registro da empresa
        nova_empresa = Empresa(
            razao_social=razao_social, cnpj=cnpj, cnpj_file=file_path, usuario_id=user_id
        )
        db.session.add(nova_empresa)
        db.session.commit()

        flash("Cadastro da empresa realizado com sucesso!", "success")
        return redirect(url_for("views.home"))

    return render_template("cadastro-juridica.html")
