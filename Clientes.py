class Cliente:
    def __init__(self):
        self.clientes = {}
        self.pedidos = {}

    def add_cliente(self, nome, poltrona):
        self.clientes[nome] = poltrona

    def register_pedido(self, nome, poltrona, num_pedido, tipo_pedido, pedido, forma_pagamento):
        self.pedidos[num_pedido] = [nome, poltrona, tipo_pedido, forma_pagamento, pedido]
    
    def get_clientes(self):
        return self.clientes

    def get_pedidos(self):
        return self.pedidos

    def buscar_cliente(self, input_busca):
        for i, j in self.clientes.items():
            if input_busca == i or input_busca == j:
                return True
            else:
                continue
        return False

    def buscar_pedido(self, input_busca):
        for i, j in self.pedidos.items():
            if input_busca == i or input_busca == j:
                return True
            else:
                continue
        return False

    def excluir_cliente(self, nome_cliente):
        return self.clientes.pop(nome_cliente)

    def cancelar_pedido(self, numero_pedido):
        return self.pedidos.pop(numero_pedido)
         
    def listar_pedidos(self):
        for i,j in self.pedidos.items():
            print("\n" + 2 * "----------------------")
            print(f"Cliente: {j[0]} | Poltrona: {j[1]}")
            print("Informações do pedido:")
            print(f"    • Número do pedido: {i}")
            print(f"    • Tipo de entrega/retirada: {j[2]}")
            print(f"    • Forma de pagamento: {j[3]}")
            print("Pedido:")
            for x in j[4]:
                print(f"    • {x}")

c = Cliente()