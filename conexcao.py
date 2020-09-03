from pymongo import MongoClient
#pip install pymongo

class MongoConnect():
    pessoa = None

    def __init__(self):
        self.cliente = MongoClient('localhost', 27017)
        self.banco = self.cliente.teste  # nome do banco
        self.aluno = self.banco.aluno  # nome da coleção


    def save(self, json):
        try:
            retorno= self.aluno.insert_one(json)
            volta=self.aluno.find_one({"_id": retorno.inserted_id})
            return volta

        except Exception as e:
            print("problema ao salvar registro")
            print(json)
            print(e)


    def ler (self, query=None, projection=None):
        for pessoa in self.aluno.find(query, projection):
            return pessoa
            # print(pessoa)


    def att(self, query,field):
        try:
            self.aluno.update(query, field)

        except Exception as e:
            print("problema ao atualizar o registro")
            print(json)
            print(e)


    def deleta(self,query):
        try:
            self.aluno.remove(query)
        except Exception as e:
            print("problema ao deletar o registro")
            print(query)
            print(e)
