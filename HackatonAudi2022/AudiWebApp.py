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
def hello():
    if request.method == "GET":
        print("GETTTTTTTTTTTTTTTTTTTTTTTTTTTT")
        return render_template("login.html")
    else:
        usuario=request.form['username']
        password=request.form['password']

        print("Hola, este es un mensaje en consola")
        print(usuario)
        print(password)
        return render_template("home.html")


        