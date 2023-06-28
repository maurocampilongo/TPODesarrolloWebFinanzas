# -------------------------------------------------------------------
# Escribimos una serie de funciones para crear una pequeña app que
# maneje un arreglo que contenga datos de operacions.
# Cada operacion tiene un código numérico entero, una descripción
# alfabetica, una tipo en stock y un monto de venta.
# Nuestras funciones haran lo siguiente:
#
# - Agregar un operacion al arreglo
# - Consultar un operacion a partir de su código
# - Modificar los datos de un operacion a partir de su código
# - Obtener un listado de los operacions que existen en el arreglo.
# - Eliminar un operacion del arreglo
# -------------------------------------------------------------------

# Definimos una lista para almacenar los operacions.
# Es una lista de diccionarios.
operaciones = []
# Definir un segundo arreglo para el presupuesto de compras
presupuesto = []

# -------------------------------------------------------------------
# Función para agregar un operacion al arreglo
# -------------------------------------------------------------------
def agregar_operacion(codigo, descripcion, tipo, monto):
    """
    Agrega un operacion al arreglo de operacions.

    Parámetros:
    - codigo: int, código numérico del operacion.
    - tipo: ingreso o egreso
    - descripcion: str, descripción alfabética del operacion.
    - monto: float
    """
    # Creamos un diccionario con los datos del operacion...
    nueva_operacion = {
        'codigo': codigo,
        'descripcion': descripcion,
        'tipo': tipo,
        'monto': monto
    }
    # Y lo agregamos a nuestro arreglo.
    operaciones.append(nueva_operacion)
    return True

# -------------------------------------------------------------------
# Función para consultar un operacion a partir de su código
# -------------------------------------------------------------------
def consultar_operacion(codigo):
    """
    Consulta una operacion a partir de su código y devuelve sus datos.

    Parámetros:
    - codigo: int, código numérico del operacion.

    Retorna:
    - dict: datos del operacion en forma de diccionario, o False si no se encontró la operacion.
    """
    # Recorremos la lista de operacions...
    for operacion in operaciones:
        # Y si el código es el correcto,
        if operacion['codigo'] == codigo:
            # Refresamos el diccionario correspondiente.
            return operacion
    # Si el bucle finaliza sin encontrar el operacion,
    # regresamos "falso."
    return False


# -------------------------------------------------------------------
# Función para modificar los datos de un operacion a partir de su código
# -------------------------------------------------------------------
def modificar_operacion(codigo, nueva_descripcion, nuevo_tipo, nuevo_monto):
    """
    Modifica los datos de un operacion a partir de su código.

    Parámetros:
    - codigo: int, código numérico del operacion.
    - nueva_descripcion: str, nueva descripción alfabética del operacion.
    - nuevo_tipo: str, nueva descripción alfabética del operacion.
    - nuevo_monto: float, nuevo monto de venta del operacion.
    """
    # Recorremos la lista de operacions...
    for operacion in operaciones:
        # Y si el código es el correcto,
        if operacion['codigo'] == codigo:
            # ...actualizamos los valores de cada clave del diccionario
            operacion['descripcion'] = nueva_descripcion
            operacion['tipo'] = nuevo_tipo
            operacion['monto'] = nuevo_monto

            # Como no hay otro operacion con ese código, salimos del bucle.
            return True
    # Si llegamos aqui, el operacion no existe.
    return False

# -------------------------------------------------------------------
# Función para obtener un listado de los operacions en pantalla
# -------------------------------------------------------------------
def listar_operaciones():
    """
    Muestra en pantalla un listado de las operaciones existentes.
    """
    # Recorremos la lista de operacions...
    print("-"*30)
    for operacion in operaciones:
        # Y mostramos los datos de cada uno de ellos.
        print(f"Código: {operacion['codigo']}")
        print(f"Descripción: {operacion['descripcion']}")
        print(f"tipo: {operacion['tipo']}")
        print(f"monto: {operacion['monto']}")
        print("-"*30)


# -------------------------------------------------------------------
# Función para modificar los eliminar un operacion a partir de su código
# -------------------------------------------------------------------
def eliminar_operacion(codigo):
    """
    Elimina una operacion a partir de su código.

    Parámetros:
    - codigo: int, código numérico de la operacion.
    """
    # Recorremos la lista de operacions...
    for operacion in operaciones:
        # Y si el código es el correcto,
        if operacion['codigo'] == codigo:
            # ...lo quitamos de la lista.
            operaciones.remove(operacion)
            # Como no hay otro operacion con ese código, salimos del bucle.
            return True
    # Si llegamos aqui, el operacion no existe.
    return False


# -------------------------------------------------------------------
# Funciones para el manejo del "presupuesto"
#
# Con estas funciones, podrás agregar y quitar operacions al presupuesto
# y mostrar el contenido del presupuesto en pantalla.
# Se realizan las verificaciones necesarias para asegurarse de que
# el operacion exista en el arreglo de operacions y que la tipo en
# stock sea suficiente.
#
# Los diccionarios que representan los elementos en el presupuesto tienen
# las mismas claves que los diccionarios que representan a los
# operacions.
# -------------------------------------------------------------------


# -------------------------------------------------------------------
# Función para agregar un operacion al presupuesto de compras
# -------------------------------------------------------------------
def agregar_al_presupuesto(codigo, monto):
    """
    Agrega una operacion al presupuesto.

    Parámetros:
    - codigo: int, código numérico del operacion a agregar.
    - tipo: int, tipo del operacion a agregar.

    Retorna:
    - bool: True si se pudo agregar el operacion al presupuesto, False si no se encontró el operacion o la tipo en stock es insuficiente.
    """
    # Vemos si existe el operacion...
    operacion = consultar_operacion(codigo)

    # Si se devolvio un falso, el operacion no existe.
    if operacion is False:
        print("La operacion no existe.")
        return False

    
    # Verificar si el operacion ya está en el presupuesto
    for item in presupuesto:
        if item['codigo'] == codigo:
            # Si existe, sumo a la tipo del presupuesto...
           item['monto'] += monto
            # ...y descuento del stock de ese operacion.
     #       operacion['monto'] -= tipo
     #       return True

    # Si el operacion no está en el presupuesto, se agrega como un nuevo item
    nuevo_item = {
        'codigo': codigo,
        'descripcion': operacion['descripcion'],
        'tipo': operacion['tipo'],
        'monto': monto
    }
    presupuesto.append(nuevo_item)

    # ...y descuento del stock de ese operacion.
    operacion['monto'] += monto
    return True


# -------------------------------------------------------------------
# Función para quitar un operacion del presupuesto de compras
# -------------------------------------------------------------------
def quitar_del_presupuesto(codigo, tipo):
    """
    Quita un operacion del presupuesto de compras.

    Parámetros:
    - codigo: int, código numérico del operacion a quitar.
    - tipo: int, tipo del operacion a quitar.

    Retorna:
    - bool: True si se pudo quitar el operacion del presupuesto, False si no se encontró el operacion en el presupuesto o la tipo a quitar es mayor a la tipo en el presupuesto.
    """
    # Recorremos la lista de operacions en el presupuesto...
    for item in presupuesto:
        # Si se ecuentra ese operacion...
        if item['codigo'] == codigo:
            # Si no hay tipo suficiente en el presupuesto...
            if tipo > item['tipo']:
                print("tipo a quitar mayor a la tipo en el presupuesto.")
                return False

            # Si llegue aqui, es que puedo descontarlos del presupuesto...
            item['tipo'] -= tipo

            # ...y reponerlos en el stock de operacions!
            operacion = consultar_operacion(codigo)
            modificar_operacion(codigo, operacion["descripcion"], operacion["tipo"]-tipo, operacion["monto"] )

            # Compruebo si la tipo de ese operacion en el presupuesto es cero:
            if item['tipo'] == 0:
                # Si quedo en cero, lo elimino del presupuesto.
                presupuesto.remove(item)
            return True

    # Si el bucle finaliza sin novedad, es que ese operacion NO ESTA en el presupuesto.
    print("El operacion no se encuentra en el presupuesto.")
    return False


# -------------------------------------------------------------------
# Función para mostrar el contenido del presupuesto de compras
# -------------------------------------------------------------------
def mostrar_presupuesto():
    """
    Muestra en pantalla el contenido del presupuesto de compras.
    """
    # Inicializamos una variable para sumar los importes de cada item
    suma = 0
    print("-"*30)

    # Recorremos la lista de operacions en el presupuesto
    # y mostramos los datos de cada operacion.
    for item in presupuesto:
        print(f'Cod: {item["codigo"]} - {item["descripcion"]}')
        print(f'monto: {item["monto"]}  tipo: {item["tipo"]}')

        # Calculamos el importe a pagar por el operacion...
        importe = item["monto"] * item["tipo"]

        # ...y acumulamos el importe en la variable suma.
        suma += importe
        print(f'Importe: {importe}')
        print("-"*30)
    print(f'Importe TOTAL: {suma}')
    return True




# -------------------------------------------------------------------
# Ejemplo de uso de las funciones
# -------------------------------------------------------------------

# Agregamos operacions a la lista:
agregar_operacion(1, 'Egreso','Alquiler', -150000)
agregar_operacion(2, 'Ingreso','Salario', 450000)
agregar_operacion(3, 'Egreso','Comida', -18000)
agregar_operacion(4, 'Egreso','Entretenimiento', -10000)
agregar_operacion(5, 'Ingreso','Clases', 10000)
# eliminar_operacion(5) # Eliminamos un operacion del stock.

# Consultar un operacion por su código
# operacion = consultar_operacion(1)
# if operacion:
#     print(f"operacion encontrado: {operacion['descripcion']}")
# else:
#     print("operacion no encontrado.")

# Modificar un operacion por su código
# modificar_operacion(1, 'Teclado mecánico 62 teclas', 20, 34000)

# Listamos todos los operacions en pantalla
listar_operaciones()

# Agregamos operaciones al presupuesto
agregar_al_presupuesto(1, -15000)
agregar_al_presupuesto(2, 45000)

# agregar_al_presupuesto(30, 1) # intentamos agregar un operacion inexistente

# Intentar agregar un operacion con tipo insuficiente
# agregar_al_presupuesto(1, 150)

# Quitar un operacion del presupuesto
quitar_del_presupuesto(5, 10000)

# Mostrar el contenido del presupuesto
mostrar_presupuesto()