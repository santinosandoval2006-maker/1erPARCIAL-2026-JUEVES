def ordenar_eventos_simpson(eventos, expresion=False):
    """Ordena la lista de eventos de los Simpson.

    Si expresion es True, ordena de la Z a la A (descendente).
    Si expresion es False (o no se pasa valor), ordena de la A a la Z
    (ascendente por defecto).
    """
    return sorted(eventos, reverse=bool(expresion))


# Lista con los nuevos eventos
eventos = [
    "Día de Jeremías Springfield",
    "Concurso de comida de donas",
    "Reunión del consejo municipal",
]

# 1. Llamada por defecto (A -> Z)
print("Por defecto (A -> Z):")
print(ordenar_eventos_simpson(eventos))
# Output: ['Concurso de comida de donas', 'Día de Jeremías Springfield', 'Reunión del consejo municipal']

# 2. Expresión evaluada en True (Z -> A)
print("\nExpresión True (Z -> A):")
print(ordenar_eventos_simpson(eventos, 10 > 5))
# Output: ['Reunión del consejo municipal', 'Día de Jeremías Springfield', 'Concurso de comida de donas']

# 3. Expresión evaluada en False (A -> Z)
print("\nExpresión False (A -> Z):")
print(ordenar_eventos_simpson(eventos, "Springfield" == "Shelbyville"))
# Output: ['Concurso de comida de donas', 'Día de Jeremías Springfield', 'Reunión del consejo municipal']