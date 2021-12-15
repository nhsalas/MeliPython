from flask import Flask, jsonify, request, render_template
import mysql.connector

app = Flask(__name__)

#Conexion BD
mydb = mysql.connector.connect(
    host='localhost',
    user="root",
    password="", 
    database='challengedb',
    port="3306"
)
miCursor = mydb.cursor()

@app.route('/bitacora')
def SaveLog(data):
    query = f"INSERT INTO challengedb.registro (data) VALUES ('{data}')"
    miCursor.execute(query)
    mydb.commit()
    return "Registro agregado correctamente"


from informacion import sistema, usuario, procesos

#GET
@app.route('/sistema', methods=['GET'])
def getInfo():
    return jsonify({"mensaje": "Informacion del Sistema", "Sistema":sistema})

@app.route('/usuarios', methods=['GET'])
def getUsers():
    return jsonify({"mensaje":"Usuarios activos", "Usuarios":usuario})

@app.route('/procesos', methods=['GET'])
def getProcess():
    return jsonify({"mensaje":"Listado de procesos activos", "Procesos":procesos})

#POST - Insercion de datos
@app.route('/sistema', methods=['POST'])
def addLog_Info():
    nuevo_registro = {
        "SO": request.json['sistemaOperativo'], 
        "Version": request.json['versionSO'], 
        "Procesador": request.json['procesador']
    }
    sistema.append(nuevo_registro)
    cadena = nuevo_registro["SO"] + " - " + nuevo_registro["Version"] + " - " + nuevo_registro["Procesador"]
    SaveLog(cadena)
    return jsonify({"mensaje":"Se agregó el registro correctamente"})

@app.route('/usuarios', methods=['POST'])
def addLog_Users():
    nuevo_registro = {
        "Username": request.json['Username'], 
    }
    usuario.append(nuevo_registro)
    SaveLog(nuevo_registro["Username"])
    return jsonify({"mensaje":"Se agregó el registro correctamente"})


if __name__ == '__main__':
    app.run(debug=True, port=4000)