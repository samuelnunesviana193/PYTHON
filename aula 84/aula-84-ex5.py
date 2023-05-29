def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def maior_numero(a, b):
    return max(a, b)

def menor_numero(a, b):
    return min(a, b)

def exibir_menu():
    print("Menu:")
    print("a. Somar")
    print("b. Multiplicar")
    print("c. Maior número")
    print("d. Menor número")

exibir_menu()
opcao = input("Digite a opção desejada: ")

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if opcao == 'a':
    resultado = somar(valor1, valor2)
elif opcao == 'b':
    resultado = multiplicar(valor1, valor2)
elif opcao == 'c':
    resultado = maior_numero(valor1, valor2)
elif opcao == 'd':
    resultado = menor_numero(valor1, valor2)
else:
    print("Opção inválida!")

if opcao in ['a', 'b', 'c', 'd']:
    print("Resultado:", resultado)