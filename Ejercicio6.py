def __repr__(self):
        return (f"ProductoKwikE(id={self.id_producto}, desc='{self.descripcion}', "
            f"precio=${self.precio}, stock={self.stock}, vence={self.fecha_vencimiento})"
        )
# 1. Crear un producto
squishee = ProductoKwikE(descripcion="Squishee de Menta")
    id_producto=101,
    fecha_vencimiento="2026-10-10",
    precio=3.50,
    stock=20,


# 1. Crear un producto
squishee = ProductoKwikE(
    descripcion="Squishee de Menta",
    id_producto=101,
    fecha_vencimiento="2026-10-10",
    precio=3.50,
    stock=20,
)

print("Producto inicial:")
print(squishee)

# 2. Modificar varios datos de forma fácil
squishee.actualizar_datos(precio=4.00, stock=15)
print("\nDespués de actualizar precio y stock:")
print(squishee)

# 3. Calcular días para expirar (ejemplo con fecha futura)
dias = squishee.dias_para_expirar(fecha_referencia="2026-10-05")
print(f"\nDías faltantes para expirar: {dias}")

# 4. Verificar cuando ya está vencido (activa alerta y pone el stock en 0)
print("\nComprobando expiración al llegar la fecha:")
squishee.dias_para_expirar(fecha_referencia="2026-10-11")
print(squishee) inicial:")
print(squishee)

# 2. Modificar varios datos de forma fácil
squishee.actualizar_datos(precio=4.00, stock=15)
print("\nDespués de actualizar precio y stock:")
print(squishee)

# 3. Calcular días para expirar (ejemplo con fecha futura)
dias = squishee.dias_para_expirar(fecha_referencia="2026-10-05")
print(f"\nDías faltantes para expirar: {dias}")

# 4. Verificar cuando ya está vencido (activa alerta y pone el stock en 0)
print("\nComprobando expiración al llegar la fecha:")
squishee.dias_para_expirar(fecha_referencia="2026-10-11")
print(squishee)