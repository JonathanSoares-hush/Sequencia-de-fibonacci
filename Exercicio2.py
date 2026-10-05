## numeros triangulares

numero = int(input("Insira um numero aleatório maior que 0:"))

def numeros_triangulares(n):
    triangulares = []

    for i in range(1, n + 1):
        triangular = (i * (i + 1)) // 2
        triangulares.append(triangular)
    return triangulares

print(numeros_triangulares(numero))

if numero in numeros_triangulares(numero):
    print("O numero inserido pertence à sequencia de numeros triangulares.")
else:
    print("O numero inserido não pertence à sequencia de numeros triangulares.")
