#Genera la secuencia acumulada de donas consumidas paso a paso
# hasta alcanzar el punto de ruptura (por ejemplo, 1,000,000 de donas)
limite_reventar = 1_000_000

donas_consumidas = [
    round(math.pow(2, n / 2), 2)
    for n in range(1, 100)
    if math.pow(2, n / 2) <= limite_reventar
import math

# Lista por compresión
donas_consumidas = [round(math.pow(2, n / 2), 2) for n in range(1, 21[
    1.41,
    2.0,
    2.83,
    4.0,
    5.66,
    8.0,
    11.31,
    16.0,
    22.63,
    32.0,
    45.25,
    64.0,
    90.51,
    128.0,
    181.02,
    256.0,
    362.04,
    512.0,
    724.08,
    1024.00
print(donas_consumida)