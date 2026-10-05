## sequancia de fibonacci
numero = int(input("insira um numero maior que 0: "))

def gerar_fibonacci(n):
    sequencia = [0, 1]
    
    for i in range(numero - 2):
        proximo_termo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo_termo)
        
    return sequencia[:n]

print(gerar_fibonacci(numero))

if numero in gerar_fibonacci(numero):
    print("O número inserido pertence à sequência de Fibonacci.")
else:
    print("O número inserido não pertence à sequência de Fibonacci.")