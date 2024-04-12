class Pessoa:
    def __init__(self, nome, idadex, profissaox):
        self.nome = nome
        self.idade = idadex
        self.profissao = profissaox


usuario1 = Pessoa("Leo", 20, "estudante")
usuario2 = Pessoa("João", 32, "Engenheiro")
print(usuario1.idade)
print(usuario2.nome)


