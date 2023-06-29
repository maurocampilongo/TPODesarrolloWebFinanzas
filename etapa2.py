# -------------------------------------------------------------------
# Definimos la clase "Producto"
# -------------------------------------------------------------------
class Registro:
    # Definimos el constructor e inicializamos los atributos de instancia
    def __init__(self, codigo, fecha, detalle, categoria, rubro, monto):
        self.codigo = codigo           # Código del registro
        self.fecha = fecha             # Código del producto
        self.detalle = detalle         # Descripción del producto
        self.categoria = categoria    # Cantidad disponible del producto
        self.rubro = rubro         # Precio del producto
        self.monto = monto

    # Este método permite modificar un registro.
    def modificar(self, new_fecha, new_detalle, new_categoria, new_rubro, new__monto):
        self.fecha = new_fecha                # Modifica la descripción del producto
        self.detalle = new_detalle            # Modifica la cantidad del producto
        self.categoria = new_categoria           # Modifica el precio del producto
        self.rubro = new_rubro
        self.monto = new__monto

# -------------------------------------------------------------------
# Definimos la clase "Transacciones"
# Transacciones gestiona una lista de registros.
# -------------------------------------------------------------------

class Transacciones:
    # Definimos el constructor e inicializamos los atributos de instancia
    def __init__(self):
        self.registros = []  # Lista de registros en Transacciones (variable de clase)


    # Este método permite crear objetos de la clase "Registro" y
    # agregarlos a Transacciones.
    def agregar_registro(self, codigo, fecha, detalle, categoria, rubro, monto):
        nuevo_registro = Registro(self, codigo, fecha, detalle, categoria, rubro, monto)
        self.registros.append(nuevo_registro)  # Agrega un nuevo registro a la lista de transacciones

    # Este método permite consultar datos de registros que están en Transacciones
    # Devuelve el registro correspondiente al código proporcionado o False si no existe.
    def consultar_registro(self, codigo):
        for registro in self.registros:
            if registro.codigo == codigo:
                return registro
        return False

    # Este método permite modificar datos de registros que están en Transacciones
    # Utiliza el método consultar_registro de Transacciones y modificar del registro.
    def modificar_registro(self, codigo, new_fecha, new_detalle, new_categoria, new_rubro, new__monto):
        registro = self.consultar_registro(codigo)
        if registro:
            registro.modificar (new_fecha, new_detalle, new_categoria, new_rubro, new__monto)

    # Este método elimina el registro indicado por codigo de la lista
    # mantenida en Transacciones
    def eliminar_registro(self, codigo):
        for registro in self.registros:
            if registro.codigo == codigo:
                self.registros.remove(registro)
                print("Registro eliminado.")
                break
        else:
            print("Registro no encontrado.")


    # Este método imprime en la terminal una lista con los datos de los
    # registros que figuran en Transacciones
    def listar_registros(self):
        print("-"*30)
        for registro in self.registros:
            print(f"Código: {registro.codigo}")
            print(f"Fecha: {registro.fecha}")
            print(f"Detalle: {registro.detalle}")
            print(f"Categoria: {registro.cantidad}")
            print(f"Rubro: {registro.rubro}")
            print(f"Monto: {registro.monto}")
            print("-"*30)
