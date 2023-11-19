def encontrar_maior_numero(numero1, numero2):
    if numero1 > numero2:
        return numero1
    elif numero2 > numero1:
        return numero2
    else:
        return "Os números são iguais."

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

resultado = encontrar_maior_numero(numero1, numero2)

print(f"O maior número é: {resultado}")
