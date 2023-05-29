num1 = float(input("digite um número: "))
num2 = float(input("digite um número pela segunda vez: "))
num3 = float(input("digite um número pela terceira vez: "))

def maior (num1, num2, num3):
    if num1 > (num2 and num3):
        return num1
    if num2 > (num1 and num3):
        return num2
    if num3 > (num1 and num2):
        return num3

print("o maior número é:", maior(num1, num2, num3))