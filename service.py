from pymongo import MongoClient

from conexcao import MongoConnect

class Aluno():

    conexao= None
    # pessoa = None

    def __init__(self):
        self.conexao = MongoConnect()

    def save(self, json):
        # aluno = {'nome': nome, 'sobrenome': sobrenome, 'curso': curso}
        return self.conexao.save(json)


    def att(self,nome,json):
        # aluno = {'nome': nome, 'sobrenome': sobrenome, 'curso': curso}
        self.conexao.att({"nome": nome}, {"$set": json})

    def deleta(self, nome):
        self.conexao.deleta({"nome": nome})


    def ler(self, acha):
         volta_ler=self.conexao.ler({"nome":acha},{"_id":0})
         return volta_ler

         # return self.conexao.pessoa

