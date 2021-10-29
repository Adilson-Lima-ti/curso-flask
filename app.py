#Index

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Índice das aulas</h1><br><h2> Aula 02 - Craindo Rotas e Configurações</h2><br><h2> Aula 03 - Criando url dinamicas</h2><br><h2> Aula 04 - Construção de URL</h2><br><h2> Aula 05 - Web Arquivos Estáticos</h2><br><h2> Aula 06 - Métodos HTTP</h2><br><h2>Aula 07 - Objetos de Requisição</h2><br><h2> Aula 08 - Redirecionamento e erros</h2><br><h2>Aula 09 - Templates com jinja2 interação com if e com for</h2><br><h2>Aula 10 - Enviando dados para template</h2><br><h2>Aula 12 - Session</h2><br><h2>Aula 14 - CRUD em Flask com SQLAlchemy</h2>"


if __name__ == '__main__':
    app.run(debug=True)
