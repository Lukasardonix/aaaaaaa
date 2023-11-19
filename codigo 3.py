def verificar_positivo_negativo(numero):
    if numero > 0:
        return 1  
    elif numero < 0:
        return -1  
    else:
        return 0  
numero_verificar = float(input("Digite um número: "))
resultado = verificar_positivo_negativo(numero_verificar)

if resultado == 1:
    print("O número é positivo.")
elif resultado == -1:
    print("O número é negativo.")
else:
    print("O número é igual a zero.")
