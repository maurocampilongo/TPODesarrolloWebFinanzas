# -------------------------------------------------------------------
# Definimos la clase "Registro"
# -------------------------------------------------------------------
class Registro:
    # Definimos el constructor e inicializamos los atributos de instancia
    def __init__(self, codigo, fecha, detalle, categoria, rubro, monto):
        self.codigo = codigo           # Código del registro
        self.fecha = fecha             # Fecha del registro
        self.detalle = detalle         # Detalle del registro
        self.categoria = categoria     # Categoria del registro
        self.rubro = rubro             # Rubro del registro
        self.monto = monto             # Monto del registro

    # Este método permite modificar un registro.
    def modificar(self, new_fecha, new_detalle, new_categoria, new_rubro, new_monto):
        self.fecha = new_fecha               
        self.detalle = new_detalle            
        self.categoria = new_categoria           
        self.rubro = new_rubro
        self.monto = new_monto

# -------------------------------------------------------------------
# Definimos la clase "Transacciones"
# Transacciones gestiona una lista de registros.
# Es nuestro "libro diario"
# -------------------------------------------------------------------

class Transacciones:
    # Definimos el constructor e inicializamos los atributos de instancia
    def __init__(self):
        self.registros = []  # Lista de registros en Transacciones (variable de clase)

    # Este método permite crear objetos de la clase "Registro" y
    # agregarlos a Transacciones.
    def agregar_registro(self, codigo, fecha, detalle, categoria, rubro, monto):
        new_registro = Registro(codigo, fecha, detalle, categoria, rubro, monto)
        self.registros.append(new_registro)  # Agrega un nuevo registro a la lista de transacciones        
        print(f"Se ha creado el registro {codigo}.")

    # Este método permite consultar datos de registros que están en Transacciones
    # Devuelve el registro correspondiente al código proporcionado o False si no existe.
    def consultar_registro(self, codigo):
        for registro in self.registros:
            if registro.codigo == codigo:
                return registro
        return False

    # Este método permite modificar datos de registros que están en Transacciones
    # Utiliza el método consultar_registro de Transacciones y modificar del registro.
    def modificar_registro(self, codigo, new_fecha, new_detalle, new_categoria, new_rubro, new_monto):
        registro = self.consultar_registro(codigo)
        if registro:
            registro.modificar (new_fecha, new_detalle, new_categoria, new_rubro, new_monto)    

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
        print("LISTADO DE REGISTROS")
        print("-"*30)
        for registro in self.registros:
            print(f"Código: {registro.codigo}")
            print(f"Fecha: {registro.fecha}")
            print(f"Detalle: {registro.detalle}")
            print(f"Categoria: {registro.categoria}")
            print(f"Rubro: {registro.rubro}")
            print(f"Monto: {registro.monto}")
            print("-"*30)

# -------------------------------------------------------------------
# Definimos la clase "Saldo" 
# Permite realizar operaciones aritmeticas sobre los registros y transacciones
# -------------------------------------------------------------------
class Saldo:
    # Definimos el constructor e inicializamos los atributos de instancia
    def __init__(self):
         self.operaciones = [] # Lista de operaciones en el saldo (variable de clase)            

    # -------------------------------------------------------------------
    # Función para mostrar el contenido del saldo de compras
    # -------------------------------------------------------------------
    def mostrar_saldo(self, mis_transacciones):
        """
        Muestra en pantalla el contenido del saldo de compras.
        """
        # Creamos "acumuladores" e inicializamos en 0 cada variable
        # para luego sumar allí sumar los montos de cada registros 
        # según la categoría a la que pertenecen
        ingresos_fijos= 0
        ingresos_variables = 0
        egresos_fijos =0
        egresos_variables =0
        ahorros = 0
        saldo = 0
        
        # Recorremos la lista de registros en el saldo
        # y mostramos los datos de cada registro.
        for registro in mis_transacciones.registros:
            categoria = registro.categoria
            monto = registro.monto

            if categoria == 'Ingreso Fijo':
                ingresos_fijos += monto
            elif categoria == 'Ingreso Variable':
                ingresos_variables += monto
            elif categoria == 'Egreso Fijo':
                egresos_fijos += monto
            elif categoria == 'Egreso Variable':
                egresos_variables += monto
            elif categoria == 'Ahorro':
                ahorros += monto               

        saldo = ingresos_fijos + ingresos_variables - egresos_fijos - egresos_variables - ahorros
        print("SALDOS")
        print("-"*30)
        print("Ingresos Fijos Totales:", ingresos_fijos)
        print("Ingresos Variables Totales:", ingresos_variables)
        print("Egresos Fijos Totales:", egresos_fijos)
        print("Egresos Variables Totales:", egresos_variables)
        print("Ahorros:", ahorros)
        print("Saldo:", saldo)
        print("-"*30)

        return True
        
# -------------------------------------------------------------------
# Ejemplo de uso de las clases y objetos definidos antes:
# -------------------------------------------------------------------
print("\033[H\033[J") # Limpiamos la pantalla
# Crear una instancia de la clase Transacciones
mis_transacciones = Transacciones()
# Agregamos registros (codigo, fecha, detalle, categoria, rubro, monto)
mis_transacciones.agregar_registro(1, '01/06/2023', 'Alquiler' , 'Egreso Fijo', 'Vivienda', 100000)
mis_transacciones.agregar_registro(2, '02/06/2023','Empleo' ,'Ingreso Fijo', 'Salario', 200000)
mis_transacciones.agregar_registro(3, '12/06/2023','Proyecto Web' ,'Ingreso Variable', 'Facturación', 50000)
mis_transacciones.agregar_registro(4, '13/06/2023','Carnicería', 'Egreso Variable', 'Alimentos', 10000)
mis_transacciones.agregar_registro(5, '27/06/2023','Plazo Fijo', 'Ahorro', 'Banco', 10000)
mis_transacciones.agregar_registro(6, '27/06/2023','Plazo Fijo', 'Ahorro', 'Banco', 10000)
# Modificar un registro por su código
mis_transacciones.modificar_registro(4, '13/06/2023','Verdulería', 'Egreso Variable', 'Alimentos', 4000)
# Eliminamos un registro 
mis_transacciones.eliminar_registro(6)
# Consultar un registro en las Transacciones
registro = mis_transacciones.consultar_registro(2)
if registro:
 print("REGISTRO ENCONTRADO:")
 print(f"Código: {registro.codigo}")
 print(f"Fecha: {registro.fecha}")
 print(f"Detalle: {registro.detalle}")
 print(f"Categoría: {registro.categoria}")
 print(f"Rubro: {registro.rubro}")
 print(f"Monto: {registro.monto}")
else:
 print("registro no encontrado.")

# Listamos todos los registros en pantalla
mis_transacciones.listar_registros()

# Mostrar el contenido del saldo
# Crear una instancia de la clase Saldo
mi_saldo = Saldo()
# Mostrar el contenido del saldo
mi_saldo.mostrar_saldo(mis_transacciones)