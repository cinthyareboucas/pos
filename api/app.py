#!/usr/bin/env python
import json
import traceback
import base64
import logging
from datetime import date, datetime
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import mysql.connector


app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'senhaFiap'
app.config['MYSQL_DATABASE_DB'] = 'fiapdb'
app.config['MYSQL_DATABASE_HOST'] = 'mysql'

#def json_serial(obj):
 #   """JSON serializer for objects not serializable by default json code"""
  #  if isinstance(obj, (datetime, date)):
   #     return obj.isoformat()
    #raise TypeError ("Type %s not serializable" % type(obj))


@app.route("/")
def hello():
    return "1 2 3 Testando!\n"


@app.route("/getAluno")
def getAluno():
    try:
        name = request.args.get('nome', default='*', type=str)
        conn = mysql.connector.connect(auth_plugin='mysql_native_password', host = "mysql",user = 'root',password = 'senhaFiap',database = 'fiapdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from aluno where name like '%"+name+"%'")
        r = [dict((cursor.description[i][0], value)
            for i, value in enumerate(row)) for row in cursor.fetchall()]
        json_string = json.dumps(r)
        return json_string
    except Exception as e:
        return 'Erro /getDados' + str(e) + traceback.format_exc()

@app.route("/getDados")
def getDados():
    try:
        conn = mysql.connector.connect(auth_plugin='mysql_native_password', host = "mysql",user = 'root',password = 'senhaFiap',database = 'fiapdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from aluno")
        r = [dict((cursor.description[i][0], value)
            for i, value in enumerate(row)) for row in cursor.fetchall()]
        json_string = json.dumps(r)
        return json_string
    except Exception as e:
        return 'Erro /getDados' + str(e) + traceback.format_exc()

@app.route("/insereAluno", methods =['POST'])
def insereAluno():
    try:
        id_aluno=request.form['id']
        nome=request.form['nome']
        idade=request.form['idade']
        conn = mysql.connector.connect(auth_plugin='mysql_native_password', host = "mysql",user = 'root',password = 'senhaFiap',database = 'fiapdb')
        cursor = conn.cursor()
        cursor.execute("insert into aluno values ("+id_aluno+",'"+nome+"', "+idade+");")
        conn.commit()
        cursor.close()
        conn.close()
        return "Inserido com sucesso!\n"
    except Exception as e:
        return 'Erro /getDados' + str(e) + traceback.format_exc()

if __name__ == "__main__":
    #teste()
    app.run(host='0.0.0.0',debug=True)
