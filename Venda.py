
import json
from Produto import Produto

class Venda:
    def __init__(self, dataVenda):
        self.__produtos = []
        self.__dataVenda = dataVenda
        self.__total = 0.0

    def get_produtos(self):
        return self.__produtos
        
    def get_dataVenda(self):
        return self.__dataVenda

    def get_total(self):
        return self.__total

    def set_dataVenda(self, dataVenda):
        self.__dataVenda = dataVenda

    def calcularTotal(self):
        total = 0.0
        for produto in self.__produtos:
            total += produto.get_preco() * produto.get_quantidade()
        return total

    def removerProduto(self, nome):
        for produto in self.__produtos:
            if produto.get_nome() == nome:
                self.__produtos.remove(produto)
                print(f"Produto {nome} removido.")
                return
        print(f"Produto {nome} não encontrado.")

    def listarProdutos(self):
        if not self.__produtos:
            print("Nenhum produto na venda.")
        else:
            print(f"\nProdutos na Venda do dia {self.__dataVenda}:")
            for produto in self.__produtos:
                print(f"Nome: {produto.get_nome()}, Preço: R${produto.get_preco():.2f}, Quantidade: {produto.get_quantidade()}")

   
    def to_dict(self):
        produtos_dict = [produto.__dict__ for produto in self.__produtos] 
        return {
            "dataVenda": self.__dataVenda,
            "produtos": produtos_dict,
            "total": self.calcularTotal()
        }

  
    def salvarEmJson(self, arquivo):
        dados_em_json = json.dumps(self.to_dict(), ensure_ascii=False, indent=4)
        with open(arquivo, 'w') as f:
            f.write(dados_em_json)
        print(f"Venda salva no arquivo {arquivo}.")
