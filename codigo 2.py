def data_por_extenso(dia, mes, ano):

    meses = {
        1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro"
    }

    print(f"Data: {dia:02d}/{mes:02d}/{ano}, Imprimir: {dia} de {meses[mes]} de {ano}")

data_por_extenso(1, 1, 2000)
