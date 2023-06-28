# -------------------------------------------------------------------
# Escribimos una serie de funciones para crear una pequeña app que
# maneje un arreglo que contenga datos de registros de entradas y salidas de dinero.
# Cada registro tiene un código numérico entero (id), una fecha, un detalle,
# una categoría, un rubro y un monto.
#
# Nuestras funciones haran lo siguiente:
#
# - Agregar un registro al arreglo
# - Consultar un registro a partir de su código
# - Modificar los datos de un registro a partir de su código
# - Obtener un listado de los registros que existen en el arreglo.
# - Eliminar un registro del arreglo
# -------------------------------------------------------------------

# Definimos una lista para almacenar los registros.
# Es una lista de diccionarios.
registros = []
# Definir un segundo arreglo para el saldo
saldo = []
# Definimos una lista acotada de opciones de categorías
categoria = ['Ingreso Fijo', 'Ingreso Variable', 'Egreso Fijo', 'Egreso Variable', 'Ahorro']

# -------------------------------------------------------------------
# Función para agregar un registro al arreglo
# -------------------------------------------------------------------
def agregar_registro(codigo, fecha, detalle, categoria, rubro, monto):
    """
    Agrega un registro al arreglo de registros.

    Parámetros:
    - codigo: int, código numérico del registro.
    - fecha: date, fecha del registro 
    - detalle: string, acá se carga de que se trata el registro
    - categoria: lista (entrada o salida)
    - rubro: str, descripción alfabética del registro
    - monto: float
    """
    # Creamos un diccionario con los datos del registro...
    nuevo_registro = {
        'codigo': codigo,
        'fecha': fecha,
        'detalle': detalle,
        'categoria': categoria,
        'rubro': rubro,
        'monto': monto
    }
    # Y lo agregamos a nuestro arreglo.
    registros.append(nuevo_registro)
    print(f"Se ha creado el registro {codigo}.")
    return True

# -------------------------------------------------------------------
# Función para consultar un registro a partir de su código
# -------------------------------------------------------------------
def consultar_registro(codigo):
    """
    Consulta una registro a partir de su código y devuelve sus datos.

    Parámetros:
    - codigo: int, código numérico del registro.

    Retorna:
    - dict: datos del registro en forma de diccionario, o False si no se encontró la registro.
    """
    # Recorremos la lista de registros...
    for registro in registros:
        # Y si el código es el correcto,
        if registro['codigo'] == codigo:
            # Refresamos el diccionario correspondiente.
            return registro
    # Si el bucle finaliza sin encontrar el registro,
    # regresamos "falso."
    return False


# -------------------------------------------------------------------
# Función para modificar los datos de un registro a partir de su código
# -------------------------------------------------------------------
def modificar_registro(codigo, new_fecha, new_detalle, new_categoria, new_rubro, new_monto):
    """
    Modifica los datos de un registro a partir de su código.

    Parámetros:
    - codigo: int, código numérico del registro.
    - fecha: date, fecha del registro 
    - detalle: string, acá se carga de que se trata el registro
    - categoria: lista (entrada o salida)
    - rubro: str, descripción alfabética del registro
    - monto: float
    """
    # Recorremos la lista de registros...
    for registro in registros:
        # Y si el código es el correcto,
        if registro['codigo'] == codigo:
            # ...actualizamos los valores de cada clave del diccionario
            registro['fecha'] = new_fecha
            registro['detalle'] = new_detalle
            registro['categoria'] = new_categoria
            registro['rubro'] = new_rubro
            registro['monto'] = new_monto
            
            print(f"Se ha modificado el registro {codigo}.")
            # Como no hay otro registro con ese código, salimos del bucle.
            return True
    # Si llegamos aqui, el registro no existe.
    return False

# -------------------------------------------------------------------
# Función para obtener un listado de los registros en pantalla
# -------------------------------------------------------------------
def listar_registros():
    """
    Muestra en pantalla un listado de las registros existentes.
    """
    # Recorremos la lista de registros...
    print("-"*30)
    print("Listado de Registros")
    print("-"*30)
    for registro in registros:
        # Y mostramos los datos de cada uno de ellos.
        print(f"Código: {registro['codigo']}")
        print(f"Fecha: {registro['fecha']}")
        print(f"Detalle: {registro['detalle']}")
        print(f"Categoría: {registro['categoria']}")
        print(f"Rubro: {registro['rubro']}")
        print(f"Monto: {registro['monto']}")
        print("-" * 30)


# -------------------------------------------------------------------
# Función para modificar los eliminar un registro a partir de su código
# -------------------------------------------------------------------
def eliminar_registro(codigo):
    """
    Elimina una registro a partir de su código.

    Parámetros:
    - codigo: int, código numérico de la registro.
    """
    # Recorremos la lista de registros...
    for registro in registros:
        # Y si el código es el correcto,
        if registro['codigo'] == codigo:
            # ...lo quitamos de la lista.
            registros.remove(registro)
            print(f"Se ha eliminado el registro {codigo}.")
            # Como no hay otro registro con ese código, salimos del bucle.
            return True
    # Si llegamos aqui, el registro no existe.
    print(f"No se encontró un registro con el código {codigo}.")
    return False

# -------------------------------------------------------------------
# Funciones para el manejo del "saldo"
#
# Con estas funciones, se podrán hacer diferentes consultas de saldo
# para mostrar el contenido del saldo en pantalla de diferentes formas.
# -------------------------------------------------------------------

# -------------------------------------------------------------------
# Función para mostrar el contenido del saldo de compras
# -------------------------------------------------------------------
def mostrar_saldo():
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
    for registro in registros:
        categoria = registro['categoria']
        monto = registro['monto']
        
        categoria = registro['categoria']
        monto = registro['monto']

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
# Ejemplo de uso de las funciones
# -------------------------------------------------------------------

# Agregamos registros (codigo, fecha, detalle, categoria, rubro, monto)
agregar_registro(1, '01/06/2023', 'Alquiler' , 'Egreso Fijo', 'Vivienda', 100000)
agregar_registro(2, '02/06/2023','Empleo' ,'Ingreso Fijo', 'Salario', 200000)
agregar_registro(3, '12/06/2023','Proyecto Web' ,'Ingreso Variable', 'Facturación', 50000)
agregar_registro(4, '13/06/2023','Carnicería', 'Egreso Variable', 'Alimentos', 10000)
agregar_registro(5, '27/06/2023','Plazo Fijo', 'Ahorro', 'Banco', 10000)
agregar_registro(6, '13/06/2023','Verdulería', 'Egreso Variable', 'Alimentos', 4000)

# Eliminamos un registro 
eliminar_registro(6)

# Consultar un registro por su código
registro = consultar_registro(1)
if registro:
    print(f"Registro encontrado: {registro['detalle']}")
else:
    print("Registro no encontrado.")

# Modificar un registro por su código
modificar_registro(3, '12/06/2023','Proyecto Web' ,'Ingreso Variable', 'Facturación', 75000)
# Listamos todos los registros en pantalla
listar_registros()
# Mostrar el contenido del saldo
mostrar_saldo()