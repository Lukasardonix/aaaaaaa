def maior_fator_primo(numero):
    
    def eh_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    maior_fator = -1
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0 and eh_primo(i):
            maior_fator = i
    if eh_primo(numero) and numero > maior_fator:
        maior_fator = numero

    return maior_fator

numero_a_verificar = int(input("Digite um número inteiro: "))
resultado = maior_fator_primo(numero_a_verificar)

print(f"O maior fator primo de {numero_a_verificar} é: {resultado}")

