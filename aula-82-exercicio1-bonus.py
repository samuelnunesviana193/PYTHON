velocidade = float( input("a velocidade daquele onix, por favor: "))

if velocidade > 80:
    print("aquele onix levará uma multa de",7 * (velocidade - 80),"reais")
else:
    print("sem multas")