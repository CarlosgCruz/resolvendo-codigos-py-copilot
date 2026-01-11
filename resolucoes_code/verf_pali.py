palavra = input("Digite uma palavra: ").lower()

palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo!")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
    print(f"O inverso de {palavra} é {palavra_invertida}.")
