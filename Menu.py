import Clientes

def cardapio(opc_pedido):
    if opc_pedido == 1: 
        lanches = {"X-Burguer": 10.00, "X-Salada": 12.00, "X-Egg": 13.00, "X-Bacon": 14.00, "X-Tudo": 18.00 }
        return lanches
    if opc_pedido == 2: 
        acompanhamentos = {"Batata Frita Pequena": 5.00, "Batata Frita Média": 6.00, "Batata Frita Grande": 8.00, "Nuggets": 7.00, "Salada": 4.50} 
        return acompanhamentos
    if opc_pedido == 3: 
        refrigerantes = {"Coca-Cola": 8.00, "Coca-Cola Zero": 7.00, "Guaraná": 7.00, "Pepsi": 8.00, "Fanta Uva": 7.00}
        return refrigerantes
    if opc_pedido == 4: 
        sucos = {"Laranja": 8.00, "Uva": 8.00, "Maracujá": 8.00, "Abacaxi": 8.00, "Morango": 8.00}
        return sucos
    if opc_pedido == 5: 
        sobremesas = {"Casquinha (Baunilha, Chocolate ou Mista)": 3.00, "Picolé": 1.50, "Tortinhas (Maçã, Banana)": 6.00}
        return sobremesas

def tela_pagamento():
    forma_pagamento = ""
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
            return forma_pagamento
        elif input_forma_pag == 2:
            forma_pagamento = "Dinheiro"
            input_troco = input("\nIrá precisar de troco (Sim | Não)? ").lower().strip()
            if input_troco == "sim":
                global troco
                troco = input("    - Quanto? R$ ")   
                return forma_pagamento
            elif input_troco == "nao" or "não":
                return forma_pagamento

def adicionar_pedido(preço_final):
    index_cardapio = 1

    for i in exibir_cardapio.keys():
        if pedido in i.lower():                           
            if pedido == "casquinha":
                while True:
                    print(f"\nQual o sabor das casquinhas?")
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

                    sabor = str(quantidade) + "x - Casquinha " + input_sabor
                    list_pedido.append(sabor)
                    preço_final += (exibir_cardapio[i] * quantidade)
                    break
            elif pedido == "tortinha":
                while True:
                    print(f"\nQual o sabor das tortinhas?")
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

                    sabor = str(quantidade) + "x - Tortinha " + input_sabor
                    list_pedido.append(sabor)
                    preço_final += (exibir_cardapio[i] * quantidade)
                    break
            else:
                item = str(quantidade) + "x - " + i
                list_pedido.append(item)
                preço_final += (exibir_cardapio[i] * quantidade)
            print("\n* Item adicionado com sucesso! *\n")
            return preço_final
        elif pedido != i and index_cardapio == len(exibir_cardapio): 
            print("\n* Este item não existe no cardápio, tente novamente! *\n")
            break
        index_cardapio += 1


if __name__ == "__main__":
    aux_cliente = Clientes.c
    lista_clientes = []
    lista_pedidos = []
    num_pedido = 0

    while True:
        print("\nO que deseja?")
        print("1 - Fazer um pedido")
        print("2 - Cancelar um pedido")
        print("3 - Ver todos os pedidos")
        print("4 - Buscar cliente ou pedido específico")
        print("5 - Sair")
        
        try:
            input_opcao = int(input("---> "))
        except ValueError:
            print("\n* Opção Inválida! Tente Novamente. *")
            continue

        if input_opcao == 1:
            while True:
                preço_final = 0
                
                print("\nInforme seus dados:")
                nome = input("  - Nome: ")
                poltrona = input("  - Poltrona: ")

                aux_cliente.add_cliente(nome, poltrona)
                cliente = aux_cliente.get_clientes()
                lista_clientes.clear()
                lista_clientes.append(cliente)

                while True:
                    print("\nSelecione a forma de entrega/retirada:")
                    print("    - Delivery")
                    print("    - Balcão")

                    try:
                        tipo_pedido = input("---> ").title()
                        if tipo_pedido != "Delivery" and tipo_pedido != "Balcão":
                            print("\n* Opção Inválida! Tente Novamente. *")
                            continue
                    except ValueError:  
                        print("\n* Opção Inválida! Tente Novamente. *")
                        continue
                    break

                if tipo_pedido == "Delivery" or tipo_pedido == "Balcão": 
                    list_pedido = []        

                    while True:
                        fim_processo = False

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

                        exibir_cardapio = cardapio(opc_pedido)
                        print("\n Opções:")
                                
                        for i in exibir_cardapio.keys():
                            print(f"    • {i} - R$ {exibir_cardapio[i]}")

                        pedido = input("O que deseja? ").lower().strip()  
                        quantidade = int(input("Quantos? "))                

                        preço_final = adicionar_pedido(preço_final)

                        while True:
                            loop_aux = input("Deseja mais alguma coisa (Sim | Não)? ").lower().strip()

                            if loop_aux == "sim": break
                            elif loop_aux == "não" or loop_aux == "nao":
                                forma_pagamento = ""
                                        
                                print("\nPedido:")
                                for i in list_pedido:
                                    print(f"    - {i}")

                                print(f"• Total: R$ {preço_final}\n")
                                
                                forma_pagamento = tela_pagamento()

                                num_pedido += 1 

                                aux_cliente.register_pedido(nome, poltrona, num_pedido, tipo_pedido, list_pedido, forma_pagamento)

                                print(f'\n# Número do pedido: {num_pedido}')

                                if tipo_pedido == "Delivery":
                                    print("Seu pedido foi registrado! Aguarde o pedido ficar pronto e ele será entregue na sua poltrona por um de nossos garçons!")
                                else:
                                    print("Seu pedido foi registrado! Você pode retirá-lo no balcão apresentando o número da sua poltrona e o comprovante!")
                                        
                                print("Obrigado e até mais!")  

                                fim_processo = True

                                break
                            else:
                                print("\n* Opção Inválida! Tente Novamente. *\n")
                                continue
                        
                        if fim_processo is True: break     
                                   
                    print("\nVocê deseja:")    
                    print("1 - Voltar para o ínicio")
                    print("2 - Encerrar")  

                    try:
                        aux_programa = int(input("---> "))
                        if aux_programa < 1 or aux_programa > 2:
                            print("\n* Opção Inválida! Tente Novamente. *")
                            continue
                    except ValueError:  
                        print("\n* Opção Inválida! Tente Novamente. *")
                        continue

                    if aux_programa == 1: break     
                    else: 
                        print("\n* Obrigado. Volte sempre! *\n")
                        exit() 

                else:
                    print("\n* Opção Inválida! Tente Novamente. *")
                    continue   

        elif input_opcao == 2:
            pedido = aux_cliente.get_pedidos()

            while True:               
                try:
                    numero_pedido = int(input('\nInforme o número do pedido que deseja cancelar ou digite "0" para sair: '))
                    if pedido[numero_pedido]:
                        aux_cliente.cancelar_pedido(numero_pedido)
                        print("\nPedido cancelado com sucesso!")
                        break
                    elif numero_pedido == 0: break
                except ValueError:
                    print("\n* Opção Inválida! Tente Novamente. *")
                    continue
                except KeyError:
                    print("\n* Pedido não encontrado! Tente novamente. *")
                    continue        
        
        elif input_opcao == 3:
            if aux_cliente.get_pedidos():
                aux_cliente.listar_pedidos()
                print("\n" + 2 * "----------------------")
            else:
                print("\n* Você não fez nenhum pedido! *")

        elif input_opcao == 4:
            while True:
                print("\n• Você deseja buscar um cliente ou pedido?")
                input_busca = input("---> ").title()
                if input_busca == "Cliente":
                    input_cliente = input("\n- Digite o nome do cliente: ").title()
                    busca = aux_cliente.buscar_cliente(input_cliente)
                    if busca is True:
                        print("\nCliente encontrado!")
                        print(f"- Nome: {input_busca} | - Poltrona: {aux_cliente.get_clientes()[input_cliente]}")
                        break
                    else: 
                        print("Cliente não encontrado!")
                        break
                elif input_busca == "Pedido":
                    input_pedido = int(input("\n- Digite o número do pedido: "))
                    busca = aux_cliente.buscar_pedido(input_pedido)   
                    if busca is True:
                        print("\nPedido encontrado!")
                        print("Informações do pedido:")
                        print(f"    • Número do pedido: {input_pedido}")
                        print(f"    • Tipo de entrega/retirada: {aux_cliente.get_pedidos()[input_pedido][2]}")
                        print(f"    • Forma de pagamento: {aux_cliente.get_pedidos()[input_pedido][3]}")
                        print("Pedido:")
                        for x in aux_cliente.get_pedidos()[input_pedido][4]:
                            print(f"    • {x}")
                        break
                    else: 
                        print("Pedido não encontrado!")
                        break
                else:
                    print("\n* Opção Inválida! Tente Novamente. *")
                    continue

        elif input_opcao == 5: 
            print("\n* Obrigado. Volte sempre! *\n")
            exit()

        else:
            print("\n* Opção Inválida! Tente Novamente. *")
            continue                

        continue 
