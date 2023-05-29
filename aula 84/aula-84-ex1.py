lg = int( input("informe a largura do terreno do fulano: "))
cp = int( input("informe o comprimento do terreno do fulano: "))

def area(lg, cp):
    total = lg*cp 
    return total
print("a área do terreno do fulano é",area(lg, cp),"metros quadrados")