import random

class Cliente:
    def __init__(self, nome, poltrona):
        self.nome = nome
        self.poltrona = poltrona
        self.clientes = {}
        self.pedidos = {}

    def add_cliente(self, nome, poltrona):
        self.clientes[nome] = poltrona

    def register_pedido(self, nome, num_pedido, poltrona, tipo_pedido, pedido, forma_pagamento):
        self.pedidos[num_pedido] = [nome, poltrona, tipo_pedido, forma_pagamento, pedido]

    def cardapio(self, opc_pedido):
        if opc_pedido == 1: 
            self.lanches = {"X-Burguer": 10.00, "X-Salada": 12.00, "X-Egg": 13.00, "X-Bacon": 14.00, "X-Tudo": 18.00 }
            return self.lanches
        if opc_pedido == 2: 
            self.acompanhamentos = {"Batata Frita Pequena": 5.00, "Batata Frita Média": 6.00, "Batata Frita Grande": 8.00, "Nuggets": 7.00, "Salada": 4.50} 
            return self.acompanhamentos
        if opc_pedido == 3: 
            self.refrigerantes = {"Coca-Cola": 8.00, "Coca-Cola Zero": 7.00, "Guaraná": 7.00, "Pepsi": 8.00, "Fanta Uva": 7.00}
            return self.refrigerantes
        if opc_pedido == 4: 
            self.sucos = {"Laranja": 8.00, "Uva": 8.00, "Maracujá": 8.00, "Abacaxi": 8.00, "Morango": 8.00}
            return self.sucos
        if opc_pedido == 5: 
            self.sobremesas = {"Casquinha (Baunilha, Chocolate ou Mista)": 3.00, "Picolé": 1.50, "Tortinhas (Maçã, Banana)": 6.00}
            return self.sobremesas
       
    def menu_cliente(self, nome, poltrona):
        while True:
            lista_nums_pedidos = []
            preço_final = 0

            print("\nSelecione a forma de entrega/retirada:")
            print("    - Delivery")
            print("    - Balcão")

            try:
                tipo_pedido = input("---> ").title()
            except ValueError:  
                print("\n* Opção Inválida! Tente Novamente. *")
                continue

            if tipo_pedido == "Delivery" or tipo_pedido == "Balcão": 
                list_pedido = []        

                self.add_cliente(nome, poltrona)

                while True:
                    index_cardapio = 1

                    print("\nCardápio:")
                    print("1 - Lanche")
                    print("2 - Acompanhamento")
                    print("3 - Refrigerante")
                    print("4 - Suco")
                    print("5 - Sobremesa")

                    try:
                        opc_pedido = int(input("---> "))
                        if opc_pedido < 1 or opc_pedido > 5: 
                            print("\n* Opção Inválida! Tente Novamente. *")
                            continue
                    except ValueError:
                        print("\n* Opção Inválida! Tente Novamente. *")
                        continue

                    cardapio = self.cardapio(opc_pedido)
                    print("\n Opções:")
                    
                    for i in cardapio.keys():
                        print(f"    • {i} - R$ {cardapio[i]}")

                    pedido = input("O que deseja? ").lower().strip()                   

                    for i in cardapio.keys():
                        if pedido in i.lower():                           
                            if pedido == "casquinha":
                                while True:
                                    print("\nQual sabor de casquinha você deseja?")
                                    print("    - Baunilha")
                                    print("    - Chocolate")
                                    print("    - Mista")

                                    try:
                                        input_sabor = input("---> ").title().strip()
                                        if input_sabor != "Baunilha" and input_sabor != "Chocolate" and input_sabor != "Mista": 
                                            print("\n* Opção Inválida! Tente Novamente. *")
                                            continue
                                    except ValueError:
                                        print("\n* Opção Inválida! Tente Novamente. *")
                                        continue

                                    sabor = "Casquinha " + input_sabor
                                    list_pedido.append(sabor)
                                    preço_final += cardapio[i]
                                    break
                            elif pedido == "tortinha":
                                while True:
                                    print("\nQual sabor de tortinha você deseja?")
                                    print("    - Maçã")
                                    print("    - Banana")

                                    try:
                                        input_sabor = input("---> ").title().strip()
                                        if input_sabor != "Maçã" and input_sabor != "Maça" and input_sabor != "Banana": 
                                            print("\n* Opção Inválida! Tente Novamente. *")
                                            continue
                                    except ValueError:
                                        print("\n* Opção Inválida! Tente Novamente. *")
                                        continue

                                    sabor = "Tortinha " + input_sabor
                                    list_pedido.append(sabor)
                                    preço_final += cardapio[i]
                                    break
                            else:
                                list_pedido.append(i)
                                preço_final += cardapio[i]
                            print("\n* Item adicionado com sucesso! *\n")
                            break
                        elif pedido != i and index_cardapio == len(cardapio): 
                            print("\n* Este item não existe no cardápio, tente novamente! *\n")
                            break
                        index_cardapio += 1

                    while True:
                        loop_aux = input("Deseja mais alguma coisa (Sim | Não)? ").lower().strip()

                        if loop_aux == "sim": break
                        elif loop_aux == "não" or loop_aux == "nao":
                            forma_pagamento = ""
                            
                            print("\nPedido:")
                            for i in list_pedido:
                                print(f"    - {i}")

                            print(f"• Total: R$ {preço_final}\n")
                            while True:
                                print("Forma de Pagamento:")
                                print("1- Máquina de Cartão")
                                print("2- Dinheiro")

                                try:
                                    input_forma_pag = int(input("---> "))             
                                except ValueError:
                                    print("\n* Opção Inválida! Tente Novamente. *")
                                    continue

                                if input_forma_pag == 1:
                                    forma_pagamento = "Máquina de Cartão"
                                    if tipo_pedido == "Balcão":
                                        print("\n• Ok! O pagamento é efetuado na hora de retirar o pedido, portanto, não se esqueça de ter o cartão em mãos.\n")
                                    break
                                elif input_forma_pag == 2:
                                    forma_pagamento = "Dinheiro"
                                    input_troco = input("\nIrá precisar de troco (Sim | Não)? ").lower().strip()
                                    if input_troco == "sim":
                                        troco = input("    - Quanto? R$ ")
                                        if tipo_pedido == "Balcão":
                                            print("\n• Ok! O pagamento é efetuado na hora de retirar o pedido, portanto, não se esqueça de ter o dinheiro em mãos.\n")
                                        break
                                    elif input_troco == "nao" or "não":
                                        if tipo_pedido == "Balcão":
                                            print("\n• Ok! O pagamento é efetuado na hora de retirar o pedido, portanto, não se esqueça de ter o dinheiro em mãos.\n")
                                        break

                            num_pedido = random.randint(100, 10000)

                            for i in lista_nums_pedidos:
                                if num_pedido == i:
                                    num_pedido = random.randint(100, 10000)
                                    continue   

                            lista_nums_pedidos.append(num_pedido)
                            self.register_pedido(nome, num_pedido, poltrona, tipo_pedido, list_pedido, forma_pagamento)

                            print(f'\n# Número do pedido: {num_pedido}')

                            if tipo_pedido == "Delivery":
                                print("Seu pedido foi registrado, aguarde o pedido ficar pronto e ele será entregue na sua poltrona por um de nossos garçons!")
                            else:
                                print("Seu pedido foi registrado, você pode retirá-lo no balcão apresentando o número da sua poltrona e o comprovante!")
                            
                            print("Obrigado e até mais!")
                            exit() 
                        else:
                            print("\n* Opção Inválida! Tente Novamente. *\n")
                            continue
            else:
                print("\n* Opção Inválida! Tente Novamente. *")
                continue      

if __name__ == "__main__":
    
    print("Informe seus dados:")
    nome = input("  - Nome: ")
    poltrona = input("  - Poltrona: ")

    c = Cliente(nome, poltrona)

    c.menu_cliente(nome, poltrona)
