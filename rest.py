class Pedido:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

class Restaurante:
    def __init__(self, nome):
        self.nome = nome
        self.menu = {}
        self.pedidos = []

    def adicionar_item_menu(self, nome, preco):
        self.menu[nome] = preco

    def fazer_pedido(self, nome, quantidade):
        if nome in self.menu:
            self.pedidos.append(Pedido(nome, quantidade))
            print(f"Pedido de {quantidade}x {nome} feito com sucesso!")
        else:
            print("Desculpe, esse item não está no menu.")

    def imprimir_fatura(self):
        total = 0
        print("Fatura:")
        for pedido in self.pedidos:
            preco_unitario = self.menu[pedido.nome]
            total_pedido = preco_unitario * pedido.quantidade
            print(f"{pedido.quantidade}x {pedido.nome}: R${total_pedido:.2f}")
            total += total_pedido
        print(f"Total: R${total:.2f}")

    def calcular_total_vendas(self):
        total_vendas = sum([self.menu[item] * pedido.quantidade for pedido in self.pedidos for item in self.menu])
        return total_vendas

    def adicionar_novo_item(self, nome, preco):
        if nome not in self.menu:
            self.menu[nome] = preco
            print(f"Novo item '{nome}' adicionado ao menu com sucesso!")
        else:
            print("Este item já existe no menu.")


# Exemplo de uso:
restaurante = Restaurante("Meu Restaurante")

# Adicionar itens ao menu
restaurante.adicionar_item_menu("Hamburguer", 10)
restaurante.adicionar_item_menu("Batata Frita", 5)
restaurante.adicionar_item_menu("Refrigerante", 3)

# Fazer pedidos
restaurante.fazer_pedido("Hamburguer", 2)
restaurante.fazer_pedido("Batata Frita", 1)
restaurante.fazer_pedido("Cachorro Quente", 1)  # Item não existente

# Imprimir fatura
restaurante.imprimir_fatura()

# Calcular total de vendas
total_vendas = restaurante.calcular_total_vendas()
print(f"Total de vendas: R${total_vendas:.2f}")

# Adicionar novo item ao menu
restaurante.adicionar_novo_item("Cachorro Quente", 7)
