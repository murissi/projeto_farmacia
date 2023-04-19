class Categoria:
    def __init__(self, nome):
        self.nome = nome


class Produto:
    def __init__(self, nome, categoria: Categoria):
        self.nome = nome
        self.categoria = categoria
