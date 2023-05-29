nota1 = float( input("informe a nota 1: ") ) 
nota2 = float( input("informe a nota 2: ") )
nota3 = float( input("informe a nota 3: ") )

media = (nota1 + nota2 + nota3)/3

if media >= 6:
    print("aprovado")
else:
    if media > 5:
        print("recuperação")
    else:
        print("reprovado")

print("Sua media foi: {:.2f}".format(media))
    