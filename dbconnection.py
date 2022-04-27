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
        assert isinstance(nombre, str)
        assert isinstance(password, str)
        assert isinstance(tipo_usuario, str)
        query = f'INSERT INTO Usuario (nombre, password, tipo_usuario) VALUES ("{nombre}", "{password}", "{tipo_usuario}")'
        try: 
                print(query)
                cursor =conn.cursor()
                cursor.execute(query)
                conn.commit()
        except Exception as e:
                print(e)
                return False
        return True

def verificar_usuario(nombre: str, password: str, tipo_usuario: str) -> bool:
        assert isinstance(nombre, str)
        assert isinstance(password, str)
        assert isinstance(tipo_usuario, str)
        query = f'SELECT * FROM Usuario WHERE nombre = "{nombre}" AND password = "{password}"'
        try: 
                cursor =conn.cursor()
                result = cursor.execute(query)
                conn.commit()
                if not result:
                        return False
        except Exception as e:
                print(e)
                return False
        return True