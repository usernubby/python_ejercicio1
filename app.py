from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ejercicio1"
    )


@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/par-impar", methods=["POST"])
def par_impar():

    datos = request.get_json()

    numero = int(datos["numero"])

    if numero % 2 == 0:
        resultado = "El número es par mi valecita"
    else:
        resultado = "El número es impar cole que pasa"

    conexion = conectar_db()
    cursor = conexion.cursor()

    sql = "INSERT INTO resultados (numero, resultado) VALUES (%s, %s)"
    valores = (numero, resultado)

    cursor.execute(sql, valores)

    conexion.commit()

    cursor.close()
    conexion.close()

    return jsonify({
        "resultado": resultado
    })


app.run(debug=True)