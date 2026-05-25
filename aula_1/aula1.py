def percorrer(lista):
    alertas = []
    for v in range(len(lista)):
        if lista[v] > 100:
            alertas.append(lista[v])
    if len(alertas) == 0:
        print("Sistema seguro")
    else:
        print(f"Revisar valores: {alertas}")

valores_brutos = [10, 50, 150, 20, 300]
percorrer(valores_brutos)