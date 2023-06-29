import sqlite3

# Configurar la conexión a la base de datos SQLite
DATABASE = 'transacciones.db'

# Obtener la conexión a la base de datos
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Crear la tabla 'registros' si no existe
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
        return True

    def consultar_registro(self, codigo):
        self.cursor.execute("SELECT * FROM registros WHERE codigo = ?", (codigo,))
        row = self.cursor.fetchone()
        if row:
            codigo, fecha, detalle, categoria, rubro, monto = row
            return Registro(codigo, fecha, detalle, categoria, rubro, monto)
        return False

    def modificar_registro(self, codigo,new_fecha, new_detalle, new_categoria, new_rubro, new_monto):
        registro = self.consultar_registro(codigo)
        if registro:
            registro.modificar(new_fecha, new_detalle, new_categoria, new_rubro, new_monto)
            self.cursor.execute("UPDATE registros SET fecha = ?, detalle= ?, categoria = ?, rubro = ?, monto = ? WHERE codigo = ?",
                                (new_fecha, new_detalle, new_categoria, new_rubro, new_monto, codigo))
            self.conexion.commit()

    def listar_registros(self):
        print("-" * 30)
        self.cursor.execute("SELECT * FROM registros")
        rows = self.cursor.fetchall()
        for row in rows:
            codigo, fecha, detalle, categoria, rubro, monto = row
            print(f"Código: {codigo}")
            print(f"Fecha: {fecha}")
            print(f"Detalle: {detalle}")
            print(f"Categoría: {categoria}")
            print(f"Rubro: {rubro}")
            print(f"Monto: {monto}")
            print("-" * 30)

    def eliminar_registro(self, codigo):
        self.cursor.execute("DELETE FROM registros WHERE codigo = ?", (codigo,))
        if self.cursor.rowcount > 0:
            print("Registro eliminado.")
            self.conexion.commit()
        else:
            print("Registro no encontrado.")

# -------------------------------------------------------------------
# Definimos la clase "Saldo"
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

# -------------------------------------------------------------------
# Ejemplo de uso de las clases y objetos definidos antes:
# -------------------------------------------------------------------
# Crear una instancia de la clase Transaccion
x = Transacciones()

# Crear una instancia de la clase Saldo
mi_saldo = Saldo()

# Agregar registros al inventario
x.agregar_registro(1, '01/06/2023', 'Alquiler' , 'Egreso Fijo', 'Vivienda', 100000)
x.agregar_registro(2, '02/06/2023','Empleo' ,'Ingreso Fijo', 'Salario', 200000)
x.agregar_registro(3, '12/06/2023','Proyecto Web' ,'Ingreso Variable', 'Facturación', 50000)
x.agregar_registro(4, '13/06/2023','Carnicería', 'Egreso Variable', 'Alimentos', 10000)
x.agregar_registro(5, '27/06/2023','Plazo Fijo', 'Ahorro', 'Banco', 10000)
x.agregar_registro(6, '27/06/2023','Plazo Fijo', 'Ahorro', 'Banco', 10000)

mi_saldo.mostrar()