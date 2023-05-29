def verificar_var (n):
    if n % 2 == 0:
        return True
    else:
        return False
    
n = int (input("digite um valor : "))
print(verificar_var(n))