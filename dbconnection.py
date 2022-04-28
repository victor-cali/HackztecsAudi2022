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