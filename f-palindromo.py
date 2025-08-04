# Solicita uma palavra ao usuário
palavra = input("Digite uma palavra: ")

# Remove espaços e converte para minúsculas (opcional, para tornar mais robusto)
palavra_formatada = palavra.replace(" ", "").lower()

# Inverte a palavra
palavra_invertida = palavra_formatada[::-1]

# Compara a palavra original com a invertida
if palavra_formatada == palavra_invertida:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
