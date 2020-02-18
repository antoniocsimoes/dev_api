from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/<int:id>')
def pessoa(id):
    return jsonify({'id':id, 'nome':'Rafael', 'profissao':'Desenvolvedor'}) #retorna um json

# @app.route('/soma/<int:valor1>/<int:valor2>/')
# def soma(valor1, valor2):
#     return jsonify({'soma': valor1 + valor2})

@app.route('/soma', methods=['POST', 'GET'])
def soma():
    if request.method == 'POST':
        #dados =request.data #retorna as informações do body como string
        dados = json.loads(request.data) #converte para o formato json
        print(dados)
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 10 + 10    
    return jsonify({'soma':total})

if __name__ == "__main__":
    app.run(debug=True)