import re
from flask import Flask


app = Flask(__name__)

from flask import abort, redirect, render_template, request, url_for
"""import mysql.connector
import sys
import boto3
import os

ENDPOINT="database-1.cvlek1uj9drj.us-west-1.rds.amazonaws.com"
PORT="3306"
USER="Administrator"
REGION="us-west-1c"
DBNAME="database-1"
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

#gets the credentials from .aws/credentials
#session = boto3.Session(profile_name='admin')
#client = session.client('rds')

#token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION)

try:
    conn =  mysql.connector.connect(host=ENDPOINT, user=USER, passwd='Hackztecs.Audi2022', port=PORT, db=DBNAME)
    cur = conn.cursor()
    cur.execute("SELECT now()")
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))"""


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        print("GETTTTTTTTTTTTTTTTTTTTTTTTTTTT")
        return render_template("login.html")
    else:
        usuario=request.form['username']
        password=request.form['password']

        print("Hola, este es un mensaje en consola")
        print(usuario)
        print(password)
        return render_template("pruebaVue.html")


@app.route('/registrar_usuario', methods=['GET', 'POST'])
def registrar_usuario():
    if request.method == 'GET':
        return render_template("registrousuarios.html")
        

@app.route('/registro_productos', methods=['GET', 'POST'])
def registro_productos():
    if request.method == 'GET':
        return render_template("pruebaVue.html")
    else:
        print("Hola, este es un mensaje en post productos")
        
        usuario=request.form['username']
        password=request.form['password']

        
        print(usuario)
        print(password)
        return render_template("pruebaVue.html")

@app.route('/registrar_proveedor', methods=['GET', 'POST'])
def registrar_proveedor():
    if request.method == 'GET':
        return render_template("registroproveedores1.html")
    else:
        print("Hola, este nuevo POST registrar proveedor")

    idproveedor=request.form('idproveedor')
    nombreproveedor=request.form('nombreproveedor')
    codigopostal=request.form('codigopostal')
    area=request.form('area')
    zona=request.form('zona')
    ciudad=request.form('ciudad')
    estado=request.form('estado')
    pais=request.form('pais')
    password=request.form('password')
    confirmpassword=request.form('password')
    
    print(idproveedor,nombreproveedor,codigopostal,
          area,zona,ciudad,estado,pais,
          password,confirmpassword)
    return render_template('registroproveedores1.html')




@app.route('/registrar_partes', methods=['GET', 'POST'])
def registrar_partes():
    if request.method == 'GET':
        return render_template("registropiezas1.html")  
    else:
        print("Nuevo psot registrar partes")
        
        idParte=request.form('idParte')
        numeroParte=request.form('numeroParte')
        nombreParte=request.form('nombreParte')
        idProveedor=request.form('idProveedor')
        altoPieza=request.form('altoPieza')
        largoPieza=request.form('largoPieza')
        anchoPieza=request.form('anchoPieza')
        pesoPieza=request.form('pesoPieza')
        ebr=request.form('ebr')
        tiempoProveedor=request.form('tiempoProveedor')
        empaquesug=request.form('empaquesug')
        piezasporcont=request.form('piezasporcont')
        
        print(idParte,numeroParte,nombreParte,
            idProveedor,altoPieza,
            largoPieza,anchoPieza,pesoPieza,
            ebr,tiempoProveedor,empaquesug,
            piezasporcont)
        return render_template("registropiezas1.html")
    
@app.route('/registrar_reporte', methods=['GET', 'POST'])
def registrar_reporte():
    if request.method == 'GET':
        return render_template("incidencias1.html")    
    
    else:
        print("Hola, este es nuevo POST, registrar Reporte")
    
    fechareporte=request.form('fechareporte')
    reporte=request.form('reporte')
    alto=request.form('alto')
    comentarios=request.form('comentarios')
    
    print(fechareporte,reporte,alto,comentarios)
    
    return render_template("incidencias1.html")




@app.route('/registrar_contenedor', methods=['GET', 'POST'])
def registrar_contenedor():
    if request.method == 'GET':
        return render_template("registrocontenedores1.html")   
    else:
        print("Hola, este es nuevo post registro contenedores")  
         
        idcontenedor=request.form('idcontenedor')
        codigocontenedor=request.form('codigocontenedor')
        nombrecontenedor=request.form('nombrecontenedor')
        alto=request.form('alto')
        largo=request.form('largo')
        ancho=request.form('ancho')
        capacidad=request.form('capacidad')
        idcostocontenedor=request.form('costocontenedor')
        idtipomaterial=request.form('tipomaterial')

        print(idcontenedor,codigocontenedor,nombrecontenedor,alto,largo,
            ancho,capacidad,idcostocontenedor,idtipomaterial)
        return render_template("registrocontenedores1.html")