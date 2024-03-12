import time
import os
import math



print("\n \033[1mCalculator\033[0m \n")
sistema = 0
while sistema != "7" and sistema != "8":

    sistema = input("Qual seu Sistema Operaional? \n7-Mac/Linux \n8-Windows \n:")
    def limpar_terminal():
        if sistema == "7":
            os.system('clear')  # No macOS ou Linux, use 'clear' para limpar o terminal
        elif sistema == "8":
            os.system('cls')  # No macOS ou Linux, use 'clear' para limpar o terminal
        else:
            pass
   

    limpar_terminal()
    
    if sistema == "7" or sistema == "8":
        sistema = int(sistema)       
        break
    else:
        limpar_terminal()
        print("Você digitou uma string! Por favor, digite um número.")


def calculator():
    def limpar_terminal():
        if sistema == "7":
            os.system('clear')  # No macOS ou Linux, use 'clear' para limpar o terminal
        elif sistema == "8":
            os.system('cls')  # No macOS ou Linux, use 'clear' para limpar o terminal
        else:
            pass
    limpar_terminal()
    Type_Calculator = input("Select \n 1-Multiplicação \n 2-Divisão \n 3-Soma \n 4-Subtração\n 5-Raiz Quadrada \n 6-Potência \n:")



    while True:
        if Type_Calculator == "3":
            number_1 = int(input('Digite o numero 1:'))
            number_2 = int(input('Digite o numero 2:'))
            time.sleep(1)
            print(f"Seu resultado é {number_1} + {number_2} = {number_1 + number_2}")
            break

        elif Type_Calculator == "1":
            number_1 = int(input('Digite o numero 1:'))
            number_2 = int(input('Digite o numero 2:'))
            time.sleep(1)
            print(f"Seu resultado é {number_1} x {number_2} = {number_1 * number_2}")   
            break

        elif Type_Calculator == "2":
            number_1 = int(input('Digite o numero 1:'))
            number_2 = int(input('Digite o numero 2:'))
            time.sleep(1)
            print(f"Seu resultado é {number_1} / {number_2} = {round(number_1 / number_2)}")
            break

        elif Type_Calculator == "4":
            number_1 = int(input('Digite o numero 1:'))
            number_2 = int(input('Digite o numero 2:'))
            time.sleep(1)
            print(f"Seu resultado é {number_1} - {number_2} = {number_1 - number_2}")
            break

        elif Type_Calculator == "5":
            number_1 = int(input('Digite o numero:'))
            time.sleep(1)
            print(f"Seu resultado é √{number_1} = {math.sqrt(number_1)}")
            break

        elif Type_Calculator == "6":
            number_1 = int(input('Digite o numero 1:'))
            expoente = int(input('Digite o expoente:'))
            time.sleep(1)
            print(f"Seu resultado é {number_1} elevado à {expoente} = {number_1 ** expoente}")
            break
        else:
            calculator()
            break
        
     
        
    time.sleep(4)
    retornar = int(input("Voce deseja fazer outra operação?\n 7-Sim\n 8-Não\n:"))

    if retornar == 7:
        limpar_terminal()
        calculator()
    else:    
        limpar_terminal()
        
calculator()





