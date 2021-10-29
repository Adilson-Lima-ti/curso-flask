#Aula 07 - Objetos de Requisição
#http://127.0.0.1:5000/?nome=Adilson%20Lima&idade=10 no link teste tem que enviar dados

from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    #print(request.method, request.args)
    t1 = request.args.to_dict()
    t2 = dict(request.args)
    return json.dumps(t1, t2)

if __name__ == '__main__':
    app.run(debug=True)

#http://127.0.0.1:5000/?nome=Adilson%20Lima&idade=10 no navegador tem que enviar dados