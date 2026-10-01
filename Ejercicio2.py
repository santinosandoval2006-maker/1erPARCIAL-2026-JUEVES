def calcular_total_donas(a, b):
    total = 0
    for _ in range(b):
        total += a
    return total
# Si cada persona come 3 donas y asisten 5 personas:
donas_por_persona = 3
cantidad_personas = 5

resultado = calcular_total_donas(donas_por_persona, cantidad_personas)
print(f"Total de donas consumidas: {resultado}")  # Output: 15