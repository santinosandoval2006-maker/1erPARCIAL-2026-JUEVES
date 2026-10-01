
class ProductoKwikE:

    def __init__(self, descripcion, id_producto, fecha_vencimiento, precio, stock):
        self.descripcion = str(descripcion)
        self.id_producto = int(id_producto)

        # Acepta instancias de date/datetime o cadenas 'YYYY-MM-DD'
        if isinstance(fecha_vencimiento, str):
            self.fecha_vencimiento = datetime.strptime(
                fecha_vencimiento, "%Y-%m-%d"
            ).date()
        elif isinstance(fecha_vencimiento, datetime):
            self.fecha_vencimiento = fecha_vencimiento.date()
        else:
            self.fecha_vencimiento = fecha_vencimiento

        self.precio = float(precio)
        self.stock = int(stock)

    def actualizar_datos(self, **kwargs):
        """Permite modificar uno o varios atributos del producto pasándolos como argumentos de palabra clave (ej.

        precio=12.50, stock=10).
        """
        for clave, valor in kwargs.items():
            if hasattr(self, clave):
                if clave == "fecha_vencimiento" and isinstance(valor, str):
                    valor = datetime.strptime(valor, "%Y-%m-%d").date()
                setattr(self, clave, valor)
            else:
                print(" El atributo '{clave}' no existe en el producto.")

    def dias_para_expirar(self, fecha_referencia=None):
        """Calcula cuántos días faltan para que el producto expire.

        Si ya expiró (o expira hoy), alerta al usuario y coloca el stock en 0.
        """
        if fecha_referencia is None:
            fecha_referencia = date.today()
        elif isinstance(fecha_referencia, str):
            fecha_referencia = datetime.strptime(
                fecha_referencia, "%Y-%m-%d"
            ).date()

        dias_restantes = (self.fecha_vencimiento - fecha_referencia).days

        if dias_restantes <= 0:
            print("¡ALERTA Apu! El producto '{self.descripcion}' (ID: {self.id_producto}) ha EXPIRADO."
            )
            self.stock = 0

        return dias_restantes

    