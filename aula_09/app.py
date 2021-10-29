#Aula 09 - Templates com jinja2 interação com if e com for
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    vlr1 = 50
    vlr2 = 10

    query = request.args.to_dict()
    return render_template('modelo.html', x=vlr1, y=vlr2, query=query)

if __name__ == '__main__':
    app.run(debug=True)