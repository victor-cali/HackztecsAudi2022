import pymysql
import aws_credentials as rds
conn = pymysql.connect(
        host= rds.host, #endpoint link
        port = rds.port, # 3306
        user = rds.user, # admin
        password = rds.password, #adminadmin
        db = rds.db, #test
        )

# To use the connection, import conn from this module
# from dbconnection import conn
def registrar_usuario(nombre: str, password: str, tipo_usuario: str) -> bool:
        resultado = False
        assert isinstance(nombre, str)
        assert isinstance(password, str)
        assert isinstance(tipo_usuario, str)
        if not verificar_usuario(nombre, password):
                query = f'INSERT INTO Usuario (nombre, password, tipo_usuario) VALUES ("{nombre}", "{password}", "{tipo_usuario}")'
                try:
                        cursor =conn.cursor()
                        cursor.execute(query)
                        conn.commit()
                        resultado = True
                except Exception as e:
                        print(e)
        return resultado

def verificar_usuario(nombre: str, password: str) -> bool:
        resultado = False
        assert isinstance(nombre, str)
        assert isinstance(password, str)
        query = f'SELECT * FROM Usuario WHERE nombre = "{nombre}" AND password = "{password}"'
        try: 
                cursor =conn.cursor()
                found = cursor.execute(query)
                conn.commit()
                if found:
                        resultado = True
        except Exception as e:
                print(e)
        return resultado

def registrar_proveedor(duns: str, nombre: str, pais: str, postal: str, ciudad: str, zona: str, subzona: str) -> bool:
        resultado = False
        assert isinstance(duns, str)
        assert isinstance(nombre, str)
        assert isinstance(pais, str)
        assert isinstance(postal, str)
        assert isinstance(ciudad, str)
        assert isinstance(zona, str)
        assert isinstance(subzona, str)

        if not verificar_proveedor(duns):
                query = f""" INSERT INTO Proceedor (duns, nombre, pais, postal, ciudad, zona, subzona) VALUES 
                        ("{duns}", "{nombre}", "{pais}", "{postal}", "{ciudad}", "{zona}", "{pais}", "{subzona}") """
                try:
                        cursor =conn.cursor()
                        cursor.execute(query)
                        conn.commit()
                        resultado = True
                except Exception as e:
                        print(e)
        return resultado

def verificar_proveedor(duns: str) -> bool:
        resultado = False
        assert isinstance(duns, str)
        query = f""" SELECT * FROM Proveedor WHERE duns = "{duns}" """
        try: 
                cursor =conn.cursor()
                found = cursor.execute(query)
                conn.commit()
                if found:
                        resultado = True
        except Exception as e:
                print(e)
        return resultado

def registrar_parte(num_parte: str, num_parte_index: str, descripcion: str, duns: str, alto: str = None, largo: str = None, ancho: str = None, peso: str = None) -> bool:
        resultado = False
        assert isinstance(num_parte, str)
        assert isinstance(num_parte_index, str)
        assert isinstance(descripcion, str)
        assert isinstance(duns, str)

        if verificar_proveedor(duns) and not verificar_parte(num_parte, num_parte_index) :
                if largo is not None and ancho is not None and alto is not None and peso is not None:
                        assert isinstance(alto, str)
                        assert isinstance(largo, str)
                        assert isinstance(ancho, str)
                        assert isinstance(peso, str)
                        query = f""" INSERT INTO Parte (num_parte, num_parte_index, descripcion, alto, largo, ancho, peso, duns) 
                                     VALUES ("{num_parte}", "{num_parte_index}", "{descripcion}", "{alto}", "{largo}", "{ancho}", "{peso}", "{duns}") """
                else:
                        query = f""" INSERT INTO Parte (num_parte, num_parte_index, descripcion, alto, largo, ancho, peso, duns) 
                                     VALUES ("{num_parte}", "{num_parte_index}", "{descripcion}", "{duns}") """
                try:
                        cursor =conn.cursor()
                        cursor.execute(query)
                        conn.commit()
                        resultado = True
                except Exception as e:
                        print(e)
        return resultado

def verificar_parte(num_parte: str, num_parte_index: str) -> bool:
        resultado = False
        assert isinstance(num_parte, str)
        assert isinstance(num_parte_index, str)
        query = f""" SELECT * FROM Parte WHERE num_parte = "{num_parte}" AND num_parte_index = "{num_parte_index}" """
        try: 
                cursor =conn.cursor()
                found = cursor.execute(query)
                conn.commit()
                if found:
                        resultado = True
        except Exception as e:
                print(e)
        return resultado