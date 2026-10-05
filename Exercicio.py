## sequancia de fibonacci
numero = float(input("insira um numero maior que 0: "))

def gerar_fibonacci(n):
    sequencia = [0, 1]
    
    for i in range(2, n):
        proximo_termo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo_termo)
        
    return sequencia[:n]

print(gerar_fibonacci(15))

if numero in gerar_fibonacci(15):
    print("O número inserido pertence à sequência de Fibonacci.")
else:
    print("O número inserido não pertence à sequência de Fibonacci.")