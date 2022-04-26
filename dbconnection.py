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