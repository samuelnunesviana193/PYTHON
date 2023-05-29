def contagem_regressiva(num):
    for num in range (num, -1, -1):
        print (num)

nr = int (input("digite a contagem regressiva: "))
print (contagem_regressiva (nr))