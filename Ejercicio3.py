def contar_interrupciones(a, b):
    # Caso base: si transcurrieron 0 horas, no hay interrupciones
    if b == 0:
        return 0
    # Caso recursivo: suma las interrupciones de una hora más las del tiempo restante
    return a + contar_interrupciones(a, b - 1)

#Si Bart interrumpe 4 veces por hora (a) durante 3 horas (b):
interrupciones_por_hora = 4
horas_tarde = 3

total = contar_interrupciones(interrupciones_por_hora, horas_tarde)
print(f"Total de interrupciones a Marge: {total}")  # Output: 12