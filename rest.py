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

    def imprimir_conta(self):
        total = 0
        print("Conta:")
        for pedido in self.pedidos:
            preco_unitario = self.menu[pedido.nome]
            total_pedido = preco_unitario * pedido.quantidade
            print(f"{pedido.quantidade}x {pedido.nome}: R${total_pedido:.2f}")
            total += total_pedido
        print(f"Total: R${total:.2f}")


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

# Imprimir conta
restaurante.imprimir_conta()
