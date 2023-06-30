import sqlite3
from flask import Flask,  jsonify, request
#from flask_cors import CORS

# Configurar la conexión a la base de datos SQLite 
DATABASE = 'transacciones.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Crear la tabla 'registros' si no existe
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

# -------------------------------------------------------------------
# Definimos la clase "Transacciones"
# -------------------------------------------------------------------
class Transacciones:
    def __init__(self):
        self.conexion = get_db_connection()
        self.cursor = self.conexion.cursor()       

    def agregar_registro(self, codigo, fecha, detalle, categoria, rubro, monto):
        new_registro = Registro (codigo, fecha, detalle, categoria, rubro, monto)
        self.cursor.execute("INSERT INTO registros VALUES (?, ?, ?, ?, ?, ?)", (codigo, fecha, detalle, categoria, rubro, monto))
        self.conexion.commit()
        return jsonify({'message': 'Producto agregado correctamente.'}), 200  

    def consultar_registro(self, codigo):
        self.cursor.execute("SELECT * FROM registros WHERE codigo = ?", (codigo,))
        row = self.cursor.fetchone()
        if row:
            codigo, fecha, detalle, categoria, rubro, monto = row
            return Registro(codigo, fecha, detalle, categoria, rubro, monto)
        return None

    def modificar_registro(self, codigo, new_fecha, new_detalle, new_categoria, new_rubro, new_monto):
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
        self.cursor.execute("SELECT * FROM registros")
        rows = self.cursor.fetchall()
        registros = []
        for row in rows:
            codigo, fecha, detalle, categoria, rubro, monto = row        
            registro = {'codigo': codigo, 'fecha': fecha, 'detalle': detalle, 'categoria': categoria, 'rubro': rubro, 'monto': monto}
            registros.append(registro)
        return jsonify(registros), 200
    
    def eliminar_registro(self, codigo):
        self.cursor.execute("DELETE FROM registros WHERE codigo = ?", (codigo,))
        if self.cursor.rowcount > 0:
            print("Registro eliminado.")
            self.conexion.commit()
            return jsonify({'message': 'Registro eliminado correctamente.'}), 200
        return jsonify({'message': 'Registro no encontrado.'}), 404

# -------------------------------------------------------------------
# Definimos la clase "Saldo"
# -------------------------------------------------------------------       
class Saldo:
    def __init__(self):
        self.conexion = get_db_connection()
        self.cursor = self.conexion.cursor()
        self.operaciones = []
    
    def mostrar(self):
        registros_saldo = []
        for operacion in self.operaciones:
            registro = {'codigo': operacion.codigo, 'fecha': operacion.fecha, 'detalle': operacion.detalle,
                        'categoria': operacion.categoria, 'rubro': operacion.rubro, 'monto': operacion.monto}
            registros_saldo.append(registro)
        return jsonify(registros_saldo), 200    

# -------------------------------------------------------------------
# Configuración y rutas de la API Flask
# -------------------------------------------------------------------

app = Flask(__name__)
#CORS(app)

saldo = Saldo()         # Instanciamos un carrito
transacciones = Transacciones()   # Instanciamos un transacciones

# Ruta para obtener los datos de un producto según su código
@app.route('/registros/<int:codigo>', methods=['GET'])
def obtener_registro(codigo):
    registro = transacciones.consultar_registro(codigo)
    if registro:
        return jsonify({
            'codigo': registro.codigo,
            'fecha': registro.fecha,
            'detalle': registro.detalle,
            'categoria': registro.categoria,
            'rubro': registro.rubro,            
            'monto': registro.monto
        }), 200
    return jsonify({'message': 'Registro no encontrado.'}), 404

# Ruta para obtener la lista de registros de transacciones
@app.route('/registros', methods=['GET'])
def obtener_registros():
    return transacciones.listar_registros()

# Ruta para agregar un registro al transacciones
@app.route('/registros', methods=['POST'])
def agregar_registro():
    codigo = request.json.get('codigo')
    fecha = request.json.get('fecha')
    detalle = request.json.get('detalle')
    categoria = request.json.get('categoria')
    rubro = request.json.get('rubro')
    monto = request.json.get('monto')
    return transacciones.agregar_registro(codigo, fecha, detalle, categoria, rubro, monto)

# Ruta para modificar un registro del transacciones
@app.route('/registros/<int:codigo>', methods=['PUT'])
def modificar_registro(codigo):
    new_fecha = request.json.get('fecha')
    new_detalle = request.json.get('detalle')
    new_categoria = request.json.get('categoria')
    new_rubro = request.json.get('rubro')
    new_monto = request.json.get('monto')
    return transacciones.modificar_registro(codigo, new_fecha, new_detalle, new_categoria, new_rubro, new_monto)

# Ruta para eliminar un registro de las transacciones
@app.route('/registros/<int:codigo>', methods=['DELETE'])
def eliminar_registro(codigo):
    return transacciones.eliminar_registro(codigo)

# Ruta para obtener el saldo
@app.route('/saldo', methods=['GET'])
def obtener_saldo():
    return saldo.mostrar()

# Ruta para obtener la lista de registros de transacciones
@app.route('/')
def index():
    return 'API de transacciones'

# Finalmente, si estamos ejecutando este archivo, lanzamos app.
if __name__ == '__main__':
    app.run()