class KwikEMart:

    def __init__(self):
        #Atributos internos: Listas de objetos ProductoKwikE por pasillo/sección
        self.bebidas = []
        self.snacks = []
        self.conveniencia = []

    def _obtener_pasillo(self, pasillo_nombre):
        """Método auxiliar interno para validar y retornar la lista del pasillo."""
        pasillos = {
            "bebidas": self.bebidas,
            "snacks": self.snacks,
            "conveniencia": self.conveniencia,
        }
        pasillo_lower = pasillo_nombre.lower().strip()
        if pasillo_lower in pasillos:
            return pasillos[pasillo_lower]
        print("insertar Pasillo '{pasillo_nombre}' no existe. Pasillos válidos: bebidas, snacks, conveniencia."
        )
        return None

# Métodos para añadir y remover productos
  def agregar_producto(self, insertar pasillo_nombre, producto):
        "Añade un objeto ProductoKwikE a un pasillo específic"
        pasillo = self._obtener_pasillo(pasillo_nombre)
        if pasillo is not None:
            if isinstance(producto, ProductoKwikE):
                pasillo.append(producto)
                print'{producto.descripcion}' añadido al pasillo de {pasillo_nombre.capitalize()})"
            else:
                print("El elemento a agregar debe ser un ProductoKwikE.")

    def remover_producto(self, pasillo_nombre, id_producto):
        """Remueve un producto del pasillo especificado por su ID."""
        pasillo = self._obtener_pasillo(pasillo_nombre)
        if pasillo is not None:
            for i, prod in enumerate(pasillo):
                if prod.id_producto == id_producto:
                   eliminado = pasillo.pop(i)               print('{eliminado.descripcion}' fue removido de {pasillo_nombre.capitalize()}."
                    )
                    return eliminado
            print("No se encontró ningún producto con ID {id_producto} en el pasillo {pasillo_nombre}."
            )
        return None
#Métodos para controlar el stock
   def ajustar_stock_producto(self, id_producto, nuevo_stock):
        """Busca un producto en todos los pasillos y actualiza su cantidad de stock."""
        todos_los_pasillos = [self.bebidas, self.snacks, self.conveniencia]
        encontrado = False

        for pasillo in todos_los_pasillos:
            for prod in pasillo:
                if prod.id_producto == id_producto:
                    prod.stock = int(nuevo_stock)
                  print ("Stock de '{prod.descripcion}' (ID: {id_producto}) actualizado a {nuevo_stock} unidades."
                    )
                    encontrado = True
                    break

        if not encontrado:
            print("No se encontró el producto con ID {id_producto} en ningún pasillo."
            )

    def reporte_inventario(self):
        """Muestra el reporte detallado del inventario actual por cada pasillo."""
        print("\n" + "=" * 45)
        print("INVENTARIO GENERAL DEL KWIK-E-MART")
        print("=" * 45)

        pasillos = [
            ("BEBIDAS", self.bebidas),
            ("SNACKS", self.snacks),
            ("CONVENIENCIA", self.conveniencia),
        ]

        for nombre_pasillo, lista_productos in pasillos:
            print(f"\n--- Pasillo: {nombre_pasillo} ---")
            if not lista_productos:
                print("  (Pasillo vacío)")
            else:
                for prod in lista_productos:
                    print(f"  • [ID: {prod.id_producto}] {prod}")
        print("=" * 45 + "\n")