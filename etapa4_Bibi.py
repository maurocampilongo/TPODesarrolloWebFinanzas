import sqlite3
from flask import Flask,  jsonify, request
from flask_cors import CORS

# Configurar la conexión a la base de datos SQLite (Para borrar)
DATABASE = 'inventario.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Configurar la conexión a la base de datos SQLite 
DATABASE = 'transacciones.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Crear la tabla 'productos' si no existe (Para borrar)
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            codigo INTEGER PRIMARY KEY,
            descripcion TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

    # Crear la tabla 'registross' si no existe
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registros (
            codigo INTEGER PRIMARY KEY,
            fecha DATE NOT NULL,
            detalle text NOT NULL,
            categoria list NOT NULL,
            rubro text NOT NULL,
            monto real NOT NULL
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

# Verificar si la base de datos existe, si no, crearla y crear la tabla
def create_database():
    conn = sqlite3.connect(DATABASE)
    conn.close()
    create_table()

# Crear la base de datos y la tabla si no existen
create_database()

# ------------------------------------------------------------------- (Para borrar)
# Definimos la clase "Producto"
# -------------------------------------------------------------------
class Producto:
    def __init__(self, codigo, descripcion, cantidad, precio):
        self.codigo = codigo
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio

    def modificar(self, nueva_descripcion, nueva_cantidad, nuevo_precio):
        self.descripcion = nueva_descripcion
        self.cantidad = nueva_cantidad
        self.precio = nuevo_precio

# -------------------------------------------------------------------
# Definimos la clase "Registro"
# -------------------------------------------------------------------
class Registro:
    def __init__(self, codigo, fecha, detalle, categoria, rubro, monto):
        self.codigo = codigo           
        self.fecha = fecha             
        self.detalle = detalle         
        self.categoria = categoria     
        self.rubro = rubro             
        self.monto = monto      

    def modificar(self, new_fecha, new_detalle, new_categoria, new_rubro, new_monto):
        self.fecha = new_fecha               
        self.detalle = new_detalle            
        self.categoria = new_categoria           
        self.rubro = new_rubro
        self.monto = new_monto        

# -------------------------------------------------------------------(Para borrar)
# Definimos la clase "Inventario"
# -------------------------------------------------------------------
class Inventario:
    def __init__(self):
        self.conexion = get_db_connection()
        self.cursor = self.conexion.cursor()

 # -------------------------------------------------------------------
# Definimos la clase "Transacciones"
# -------------------------------------------------------------------
class Transacciones:
    def __init__(self):
        self.conexion = get_db_connection()
        self.cursor = self.conexion.cursor()       

# Para borrar
    def agregar_producto(self, codigo, descripcion, cantidad, precio):
        producto_existente = self.consultar_producto(codigo)
        if producto_existente:
            return jsonify({'message': 'Ya existe un producto con ese código.'}), 400

        nuevo_producto = Producto(codigo, descripcion, cantidad, precio)
        self.cursor.execute("INSERT INTO productos VALUES (?, ?, ?, ?)", (codigo, descripcion, cantidad, precio))
        self.conexion.commit()
        return jsonify({'message': 'Producto agregado correctamente.'}), 200
    # -------------------------------------------------------------------

    def agregar_registro(self, codigo, fecha, detalle, categoria, rubro, monto):
        new_registro = Registro (codigo, fecha, detalle, categoria, rubro, monto)
        self.cursor.execute("INSERT INTO registros VALUES (?, ?, ?, ?, ?, ?)", (codigo, fecha, detalle, categoria, rubro, monto))
        self.conexion.commit()
        return jsonify({'message': 'Producto agregado correctamente.'}), 200  


# Para borrar
    def consultar_producto(self, codigo):
        self.cursor.execute("SELECT * FROM productos WHERE codigo = ?", (codigo,))
        row = self.cursor.fetchone()
        if row:
            codigo, descripcion, cantidad, precio = row
            return Producto(codigo, descripcion, cantidad, precio)
        return None
    # -------------------------------------------------------------------

    def consultar_registro(self, codigo):
        self.cursor.execute("SELECT * FROM registros WHERE codigo = ?", (codigo,))
        row = self.cursor.fetchone()
        if row:
            codigo, fecha, detalle, categoria, rubro, monto = row
            return Registro(codigo, fecha, detalle, categoria, rubro, monto)
        return None


# Para borrar
    def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio):
        producto = self.consultar_producto(codigo)
        if producto:
            producto.modificar(nueva_descripcion, nueva_cantidad, nuevo_precio)
            self.cursor.execute("UPDATE productos SET descripcion = ?, cantidad = ?, precio = ? WHERE codigo = ?",
                                (nueva_descripcion, nueva_cantidad, nuevo_precio, codigo))
            self.conexion.commit()
            return jsonify({'message': 'Producto modificado correctamente.'}), 200
        return jsonify({'message': 'Producto no encontrado.'}), 404
    # -------------------------------------------------------------------

    def modificar_registro(self, codigo,new_fecha, new_detalle, new_categoria, new_rubro, new_monto):
        registro = self.consultar_registro(codigo)
        if registro:
            registro.modificar(new_fecha, new_detalle, new_categoria, new_rubro, new_monto)
            self.cursor.execute("UPDATE registros SET fecha = ?, detalle= ?, categoria = ?, rubro = ?, monto = ? WHERE codigo = ?",
                                (new_fecha, new_detalle, new_categoria, new_rubro, new_monto, codigo))
            self.conexion.commit()
            return jsonify({'message': 'Registro modificado correctamente.'}), 200
        return jsonify({'message': 'Registro no encontrado.'}), 404

# Para borrar
    def listar_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        rows = self.cursor.fetchall()
        productos = []
        for row in rows:
            codigo, descripcion, cantidad, precio = row
            producto = {'codigo': codigo, 'descripcion': descripcion, 'cantidad': cantidad, 'precio': precio}
            productos.append(producto)
        return jsonify(productos), 200
        # -------------------------------------------------------------------

    def listar_registros(self):
        print("-" * 30)
        self.cursor.execute("SELECT * FROM registros")
        rows = self.cursor.fetchall()
        for row in rows:
            codigo, fecha, detalle, categoria, rubro, monto = row
        # -Elegir vs proximo parrafo------------------------------------------------------------------   
            print(f"Código: {codigo}")
            print(f"Fecha: {fecha}")
            print(f"Detalle: {detalle}")
            print(f"Categoría: {categoria}")
            print(f"Rubro: {rubro}")
            print(f"Monto: {monto}")
            print("-" * 30)   
 # -Elegir vs anterior parrafo------------------------------------------------------------------ 
            registro = {'codigo': codigo, 'fecha': fecha, 'detalle': detalle, 'categoria': categoria, 'rubro': rubro, 'monto': monto}
            registros.append(registro)
        return jsonify(registros), 200   
    
# Para borrar
    def eliminar_producto(self, codigo):
        self.cursor.execute("DELETE FROM productos WHERE codigo = ?", (codigo,))
        if self.cursor.rowcount > 0:
            self.conexion.commit()
            return jsonify({'message': 'Producto eliminado correctamente.'}), 200
        return jsonify({'message': 'Producto no encontrado.'}), 404
    
    def eliminar_registro(self, codigo):
        self.cursor.execute("DELETE FROM registros WHERE codigo = ?", (codigo,))
        if self.cursor.rowcount > 0:
            print("Registro eliminado.")
            self.conexion.commit()
            return jsonify({'message': 'Registro eliminado correctamente.'}), 200
        return jsonify({'message': 'Registro no encontrado.'}), 404


# -------------------------------------------------------------------# Para borrar
# Definimos la clase "Carrito"
# -------------------------------------------------------------------
class Carrito:
    def __init__(self):
        self.conexion = get_db_connection()
        self.cursor = self.conexion.cursor()
        self.items = []

    def agregar(self, codigo, cantidad, inventario):
        producto = inventario.consultar_producto(codigo)
        if producto is None:
            return jsonify({'message': 'El producto no existe.'}), 404
        if producto.cantidad < cantidad:
            return jsonify({'message': 'Cantidad en stock insuficiente.'}), 400
            for item in self.items:
            if item.codigo == codigo:
                item.cantidad += cantidad
                self.cursor.execute("UPDATE productos SET cantidad = cantidad - ? WHERE codigo = ?",
                                    (cantidad, codigo))
                self.conexion.commit()
                return jsonify({'message': 'Producto agregado al carrito correctamente.'}), 200

        nuevo_item = Producto(codigo, producto.descripcion, cantidad, producto.precio)
        self.items.append(nuevo_item)
        self.cursor.execute("UPDATE productos SET cantidad = cantidad - ? WHERE codigo = ?",
                            (cantidad, codigo))
        self.conexion.commit()
        return jsonify({'message': 'Producto agregado al carrito correctamente.'}), 200
 # -------------------------------------------------------------------   
        
class Saldo:
    def __init__(self):
        self.conexion = sqlite3.connect('transacciones.db')  # Conexión a la base de datos
        self.cursor = self.conexion.cursor()
        self.operaciones = []

    def mostrar(self):
        print("-" * 30)
        for operacion in self.operaciones:
            print(f"Código: {operacion['codigo']}")
            print(f"Fecha: {operacion['fecha']}")
            print(f"Detalle: {operacion['detalle']}")
            print(f"Categoria: {operacion['categoria']}")
            print(f"Rubro: {operacion['rubro']}")
            print(f"Monto: {operacion['monto']}")
            print("-" * 30)











    def quitar(self, codigo, cantidad, inventario):
        for item in self.items:
            if item.codigo == codigo:
                if cantidad > item.cantidad:
                    return jsonify({'message': 'Cantidad a quitar mayor a la cantidad en el carrito.'}), 400
                item.cantidad -= cantidad
                if item.cantidad == 0:
                    self.items.remove(item)
                self.cursor.execute("UPDATE productos SET cantidad = cantidad + ? WHERE codigo = ?",
                                    (cantidad, codigo))
                self.conexion.commit()
                return jsonify({'message': 'Producto quitado del carrito correctamente.'}), 200

        return jsonify({'message': 'El producto no se encuentra en el carrito.'}), 404

    def mostrar(self):
        productos_carrito = []
        for item in self.items:
            producto = {'codigo': item.codigo, 'descripcion': item.descripcion, 'cantidad': item.cantidad,
                        'precio': item.precio}
            productos_carrito.append(producto)
        return jsonify(productos_carrito), 200


# -------------------------------------------------------------------
# Configuración y rutas de la API Flask
# -------------------------------------------------------------------

app = Flask(__name__)
CORS(app)

carrito = Carrito()         # Instanciamos un carrito
inventario = Inventario()   # Instanciamos un inventario

# Ruta para obtener los datos de un producto según su código
@app.route('/productos/<int:codigo>', methods=['GET'])
def obtener_producto(codigo):
    producto = inventario.consultar_producto(codigo)
    if producto:
        return jsonify({
            'codigo': producto.codigo,
            'descripcion': producto.descripcion,
            'cantidad': producto.cantidad,
            'precio': producto.precio
        }), 200
    return jsonify({'message': 'Producto no encontrado.'}), 404

# Ruta para obtener la lista de productos del inventario
@app.route('/productos', methods=['GET'])
def obtener_productos():
    return inventario.listar_productos()

# Ruta para agregar un producto al inventario
@app.route('/productos', methods=['POST'])
def agregar_producto():
    codigo = request.json.get('codigo')
    descripcion = request.json.get('descripcion')
    cantidad = request.json.get('cantidad')
    precio = request.json.get('precio')
    return inventario.agregar_producto(codigo, descripcion, cantidad, precio)

# Ruta para modificar un producto del inventario
@app.route('/productos/<int:codigo>', methods=['PUT'])
def modificar_producto(codigo):
    nueva_descripcion = request.json.get('descripcion')
    nueva_cantidad = request.json.get('cantidad')
    nuevo_precio = request.json.get('precio')
    return inventario.modificar_producto(codigo, nueva_descripcion, nueva_cantidad, nuevo_precio)

# Ruta para eliminar un producto del inventario
@app.route('/productos/<int:codigo>', methods=['DELETE'])
def eliminar_producto(codigo):
    return inventario.eliminar_producto(codigo)

# Ruta para agregar un producto al carrito
@app.route('/carrito', methods=['POST'])
def agregar_carrito():
    codigo = request.json.get('codigo')
    cantidad = request.json.get('cantidad')
    inventario = Inventario()
    return carrito.agregar(codigo, cantidad, inventario)

# Ruta para quitar un producto del carrito
@app.route('/carrito', methods=['DELETE'])
def quitar_carrito():
    codigo = request.json.get('codigo')
    cantidad = request.json.get('cantidad')
    inventario = Inventario()
    return carrito.quitar(codigo, cantidad, inventario)

# Ruta para obtener el contenido del carrito
@app.route('/carrito', methods=['GET'])
def obtener_carrito():
    return carrito.mostrar()

# Ruta para obtener la lista de productos del inventario
@app.route('/')
def index():
    return 'API de Inventario'

# Finalmente, si estamos ejecutando este archivo, lanzamos app.
if __name__ == '__main__':
    app.run()