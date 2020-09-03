from flask import Flask, request, jsonify
from service import Aluno


aluno=Aluno()


app = Flask(__name__)

@app.route("/")
def index():
    return "isso é um printII!"

@app.route("/minhaaplicacao/<nome>", methods=['GET'])#lsitar
def get(nome):
    volta=aluno.ler(nome)
    return volta
    # return aluno.pessoa

@app.route("/minhaaplicacao", methods=['POST'])#cadastra
def post():
    data = request.json
    result = aluno.save(data)
    disc_retorno={"id":str(result["_id"]), "nome": result["nome"],
                  "sobrenome": result["sobrenome"],
                  "curso":result["curso"] }
    return jsonify(disc_retorno)

@app.route("/minhaaplicacao/<nome>", methods=['PUT'])#atualisa
def put(nome):
    data = request.json
    aluno.att(nome,data)

    return "att com sucesso"

@app.route("/minhaaplicacao/<nome>", methods=['DELETE'])#deleta
def delete(nome):
    aluno.deleta(nome)
    return "deletado"



if __name__ == '__main__':
    app.run(debug=True)