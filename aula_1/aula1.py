valores_brutos: int = [10, 50, 150, 20, 300]
alertas: int = []
for v in valores_brutos:
    print(v)
    if v > 100: 
        alertas.append(v)

if len(alertas) == 0:
    print("Sistema seguro")
else:
    print(f"Revisar valores: {alertas}")