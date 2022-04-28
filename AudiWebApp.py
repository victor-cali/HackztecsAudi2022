from curses.ascii import alt
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
        print(usuario, password)
        return render_template("home.html")





@app.route('/registrar_usuario', methods=['GET', 'POST'])
def registrar_usuario():
    if request.method == 'GET':
        return render_template("registrousuarios.html")
    else:
        id=request.form('idUsuario')
        nombre=request.form('nombreUsuario')
        nombreUsuario=request.form('nombreUsuario')
        password=request.form('password')
        confirmPassword=request.form('password')
        
        print("Hola, ese es registro usuarios")
        print(id,nombre,nombreUsuario,password,confirmPassword)
        return render_template("registrousuarios.html")
        
    
    
    
    
        

@app.route('/registro_productos', methods=['GET', 'POST'])
def registro_productos():
    if request.method == 'GET':
        return render_template("registrousuarios.html")
    else:
        usuario=request.form('username')
        password=request.form('password')
        
        print("Hola, este es registroproductos")
        print(usuario, password)
        return render_template('registrousuarios.html')
    
    
    
    
    

@app.route('/registrar_proveedor', methods=['GET', 'POST'])
def registrar_proveedor():
    if request.method == 'GET':
        return render_template("registroproveedores.html")
    else:
        id=request.form('idProveedor')
        nombre=request.form('nombreProveedor')
        cp=request.form('codigopostal')
        area=request.form('area')
        zona=request.form('zona')
        ciudad=request.form('ciudad')
        estado.request.form('estado')
        pais.request.form('pais')
        contraseña=request.form('password')
        confirmarContraseña=request.form('password')
        
        print("Hola, este es registro proveedores")
        print(id,nombre,cp,area,zona,ciudad,estado,pais,contraseña,confirmarContraseña)
        return render_template('registrousuarios.html')
    
    
    
    
    
    

@app.route('/registrar_partes', methods=['GET', 'POST'])
def registrar_partes():
    if request.method == 'GET':
        return render_template("registropiezas.html")  
    else:
        id=request.form('idParte')
        numParte=request.form('numeroParte')
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
        
        print("Hola, este es registro piezas")
        print(id,numParte,idProveedor,
              altoPieza,largoPieza,anchoPieza,
              pesoPieza,ebr,tiempoProveedor,
              empaquesug,piezasporcont)
        return render_template('registropiezas.html')
    
    
    
    
    
@app.route('/registrar_reporte', methods=['GET', 'POST'])
def registrar_reporte():
    if request.method == 'GET':
        return render_template("incidencias.html")    
    
    else:
        fechareporte=request.form('fechareporte')
        reporte=request.form('reporte')
        alto=request.form('alto')
        comentarios=request.form('comentarios')
        
        print("Hola, este es incidencias")
        print(fechareporte,reporte,alto,comentarios)
        return render_template('registrousuarios.html')
    
    



@app.route('/registrar_contenedor', methods=['GET', 'POST'])
def registrar_contenedor():
    if request.method == 'GET':
        return render_template("registrocontenedores.html")      
    else:
       idcontenedor=request.form('idcontenedor')
       codigocontenedor=request.form('codigocontenedor')
       nombrecontenedor=request.form('nombrecontenedor')
       alto=request.form('alto')
       largo=request.form('largo')
       ancho=request.form('ancho')
       capacidad=request.form('capacidad')
       costocontenedor=request.form('costocontenedor')
       tipomaterial=request.form('tipomaterial')
       
    print("hola, este es registro contenedores")    
    print(idcontenedor,codigocontenedor,nombrecontenedor,
              alto,largo,ancho,capacidad,costocontenedor,tipomaterial)
    return render_template('registrocontenedores.html')
    
    
    
