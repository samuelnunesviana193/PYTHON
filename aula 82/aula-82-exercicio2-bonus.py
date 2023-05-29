nota = float( input("qual foi a nota do fulano?: "))

if nota <= 50:
    print("fulano ganhou um certificado de participação")
if 50 < nota <= 60:
    print("fulano ganhou um certificado de menção honrosa")
if 60 < nota <= 70:
    print("fulano ganhou uma medalha de bronze")
if 70 < nota <= 90:
     print("fulano ganhou uma medalha de prata")
if 90 < nota <= 100:
     print("fulano ganhou uma medalha de ouro")