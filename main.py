lista_de_frutas = []
print("~~"*2)
print("MENU")
print("~~"*2)
while True:
        pergunta = int(input("O que tu quer aqui? \n(1) para add alguma fruta \n(2) frutas na lista\n(3) sair\n  "))
        if pergunta == 1:
            fruta = input("Escreva o nome de uma fruta: ")
            lista_de_frutas.append(fruta)
            pergunta2= int(input("(1) add outra fruta\n(2) volta ao menu principal\n     "))
            while True:
                if pergunta2 == 1:
                    pergunta2 = input("Digite o nome de alguma outra fruta: ")
                    lista_de_frutas.append(pergunta2)
                    break
                elif pergunta2 ==2:
                        break
        elif pergunta == 2:
            if len(lista_de_frutas) == 0:
                print("Não há nada aqui, você precisa add algo antes")
            else:
                print(lista_de_frutas)
        elif pergunta == 3:
            print("><"*6)
            print("Adeus, otário")
            print("><"*6)
            break
            #Uso do try ao invés dessa gambiarra para tratamento de dados
        elif pergunta > 3 or pergunta <= 0  :
            print("Esse comando não existe, escolha uma opção válida")


