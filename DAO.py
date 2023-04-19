from Models import *


class DaoProduto:
    produtos = None

    @classmethod
    def salvar(cls, produto: Produto):
        with open('produtos.txt', 'a') as arq:
            arq.writelines(produto.nome + ":" + produto.categoria.nome)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('produtos.txt', 'r') as arq:
            cls.produtos = arq.readlines()
        cls.produtos = list(map(lambda x: x.replace('\n', ''), cls.produtos))
        return cls.produtos


print(DaoProduto.ler())
