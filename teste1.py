class Pessoa:
    def __init__(self, nomex, idadex, profissaox):
        self.nome = nomex
        self.idade = idadex
        self.profissao = profissaox


usuario1 = Pessoa("Leo", 20, "estudante")
usuario2 = Pessoa("João", 32, "Engenheiro")
print(usuario1.nome)


