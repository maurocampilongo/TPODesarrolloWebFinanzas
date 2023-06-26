#----------------------------------------------
# Importamos el módulo necesario para gestionar
# la base de datos.
#----------------------------------------------
import sqlite3

# Nombre del archivo que contiene la base de datos.
DATABASE = "pruebas.db" 


#----------------------------------------------
# Conectamos con la base de datos. 
# Retornamos el conector (conn)
#----------------------------------------------
def conectar():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


#----------------------------------------------
# Esta funcion crea la tabla "productos" en la
# base de datos, en caso de que no exista.
#----------------------------------------------
def crear_tabla():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS productos (
                    codigo INT PRIMARY KEY,
                    descripcion VARCHAR(255),
                    stock INT,
                    precio FLOAT)
            """)
    conn.commit()
    cursor.close()
    conn.close()


#----------------------------------------------
# Esta funcion da de alta un producto en la
# base de datos.
#----------------------------------------------
def alta_producto(cod, desc, stock, valor):
    print()
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
                    INSERT INTO productos(codigo, descripcion, stock, precio)
                    VALUES(?,?,?,?) """,(cod, desc, stock, valor))
        conn.commit()
        cursor.close()
        conn.close()
    except:
        print("Error: Alta NO realizada.")
    else:
        print ("Alta efectuada correctamente.")
    print("-"*30)

#----------------------------------------------
# Muestra en la pantalla los datos de un  
# producto a partir de su código.
#----------------------------------------------
def consultar_producto(cod):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM productos 
                            WHERE codigo=?""", (cod,))
        producto = cursor.fetchone()
        print()
        print(f"Código     : {producto['codigo']}")
        print(f"Descripción: {producto['descripcion']}")
        print(f"Stock      : {producto['stock']}")
        print(f"Precio     : {producto['precio']}")
        print("-"*30)
        conn.commit()
        cursor.close()
        conn.close()
        return producto
    except:
        print("Error: posible registro no encontrado")
        print("-"*30)
        return False


#----------------------------------------------
# Modifica los datos de un producto a partir
# de su código.
#----------------------------------------------
def modificar_producto(cod, nueva_desc, nuevo_stock, nuevo_precio):
    producto = consultar_producto(cod)
    if producto:
        print("\nNuevos datos del producto:")
        print(f"Descripción: {nueva_desc}")
        print(f"Stock      : {nuevo_stock}")
        print(f"Precio     : {nuevo_precio}")

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""UPDATE productos SET descripcion=?, stock=?, precio=?
                            WHERE codigo=?""", (nueva_desc, nuevo_stock, nuevo_precio, cod))
        conn.commit()
        
        print("El producto ha sido modificado correctamente.")
    else:
        print("El producto no se encuentra en la base de datos.")
    
    cursor.close()
    conn.close()
    print("-"*30)


#----------------------------------------------
# Lista todos los productos en la base de datos.
#----------------------------------------------
def listar_productos():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        print("\nListado de productos:")
        print("-" * 30)
        for producto in productos:
            print(f"Código     : {producto['codigo']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Stock      : {producto['stock']}")
            print(f"Precio     : {producto['precio']}")
            print("-" * 30)
        conn.commit()
        cursor.close()
        conn.close()
    except:
        print("Error al listar los productos.")
        print("-" * 30)


#----------------------------------------------
# Ejemplos de uso de las funciones implementadas
#----------------------------------------------
crear_tabla()

alta_producto(1, "Teclado USB", 15, 8500)
alta_producto(2, "Mouse USB", 35, 2500)

consultar_producto(1)
consultar_producto(2)

alta_producto(3, "Micrófono", 35, 4500)
modificar_producto(3, "Micrófono PC", 35, 4500)
consultar_producto(3)

listar_productos()