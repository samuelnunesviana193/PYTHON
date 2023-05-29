viagem = float( input("qual a distancia da viagem entre a casa o fulano e a casa do beutrano?: "))

if viagem <= 200:
    preco = viagem * 0.50
    print(f"a viagem da casa do fulano até a casa do beutrano custará {preco:.2f} reais, em relação a passagem do busão")
else:
    preco = viagem * 0.45
    print(f"a viagem da casa do fulano até a casa do beutrano custará {preco:.2f} reais, em relação a passagem do busão")