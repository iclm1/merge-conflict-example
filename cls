[1mdiff --git a/rest.py b/rest.py[m
[1mindex 3b0da5f..d0f73e3 100644[m
[1m--- a/rest.py[m
[1m+++ b/rest.py[m
[36m@@ -19,9 +19,9 @@[m [mclass Restaurante:[m
         else:[m
             print("Desculpe, esse item não está no menu.")[m
 [m
[31m-    def imprimir_conta(self):[m
[32m+[m[32m    def imprimir_fatura(self):[m
         total = 0[m
[31m-        print("Conta:")[m
[32m+[m[32m        print("Fatura:")[m
         for pedido in self.pedidos:[m
             preco_unitario = self.menu[pedido.nome][m
             total_pedido = preco_unitario * pedido.quantidade[m
[36m@@ -29,6 +29,17 @@[m [mclass Restaurante:[m
             total += total_pedido[m
         print(f"Total: R${total:.2f}")[m
 [m
[32m+[m[32m    def calcular_total_vendas(self):[m
[32m+[m[32m        total_vendas = sum([self.menu[item] * pedido.quantidade for pedido in self.pedidos for item in self.menu])[m
[32m+[m[32m        return total_vendas[m
[32m+[m
[32m+[m[32m    def adicionar_novo_item(self, nome, preco):[m
[32m+[m[32m        if nome not in self.menu:[m
[32m+[m[32m            self.menu[nome] = preco[m
[32m+[m[32m            print(f"Novo item '{nome}' adicionado ao menu com sucesso!")[m
[32m+[m[32m        else:[m
[32m+[m[32m            print("Este item já existe no menu.")[m
[32m+[m
 [m
 # Exemplo de uso:[m
 restaurante = Restaurante("Meu Restaurante")[m
[36m@@ -43,5 +54,12 @@[m [mrestaurante.fazer_pedido("Hamburguer", 2)[m
 restaurante.fazer_pedido("Batata Frita", 1)[m
 restaurante.fazer_pedido("Cachorro Quente", 1)  # Item não existente[m
 [m
[31m-# Imprimir conta[m
[31m-restaurante.imprimir_conta()[m
[32m+[m[32m# Imprimir fatura[m
[32m+[m[32mrestaurante.imprimir_fatura()[m
[32m+[m
[32m+[m[32m# Calcular total de vendas[m
[32m+[m[32mtotal_vendas = restaurante.calcular_total_vendas()[m
[32m+[m[32mprint(f"Total de vendas: R${total_vendas:.2f}")[m
[32m+[m
[32m+[m[32m# Adicionar novo item ao menu[m
[32m+[m[32mrestaurante.adicionar_novo_item("Cachorro Quente", 7)[m
