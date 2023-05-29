salario = float( input("qual o salário da fulana?: "))

if salario >= 8250:
    print("fulana terá um aumento de 10%, e passará a ganhar",salario * 1.1,"reais")
else:
    print("fulana terá um aumento de 15%, e passará a ganhar",salario * 1.15,"reais")
