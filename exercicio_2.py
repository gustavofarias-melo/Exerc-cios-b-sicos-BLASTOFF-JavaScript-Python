distancia = float(input("Digite a distancia (KM):  "))
combustivel = float(input("Digite quanto combustivel foi gasto (em litros): "))

media = float((combustivel * 1000) / (distancia * 1000))

print(f"Consumo medio: {media}")