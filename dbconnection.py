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
        query = f'INSERT INTO Usuario (nombre, password, tipo_usuario) VALUES ({nombre}, {password}, {tipo_usuario})'
        try: 
                cursor =conn.cursor()
                cursor.execute(query)
                conn.commit()
        except:
                return False
        return True

def verificar_usuario(nombre: str, password: str, tipo_usuario: str) -> bool:
        assert isinstance(nombre, str)
        assert isinstance(password, str)
        assert isinstance(tipo_usuario, str)
        query = f'SELECT * FROM Usuario WHERE nombre == {nombre}, password == {password}'
        try: 
                cursor =conn.cursor()
                cursor.execute(query)
                conn.commit()
        except:
                return False
        return True