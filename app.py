from flask import Flask, request, url_for, session, redirect, render_template, flash
from usuarios import Usuario

app = Flask(__name__)

app.secret_key = "saflñdsfldkiijukiekswdx sfdafsafgrerjtretrt68545375473fefe432tewyp0o7ik7564utr4utj2jhg4"

@app.route("/")
def inicio():
    usuarios = Usuario.get_all

    return render_template("index.html", usuarios=usuarios)

@app.route("/usuario_nuevo")
def form_usuario():
    return render_template("registro.html")

@app.route("/Crear", methods=['POST'])
def Crear_usuario():
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    email = request.form.get('email') 

    try:
        user_id = Usuario.save({
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
        })

        if not user_id:
            flash("No se pudo crear la cuenta.", "error")
            return redirect(url_for("inicio"))

    except ValueError as error:
        flash(str(error), "error")
        return redirect(url_for("inicio"))

    return redirect(url_for("inicio")), flash("Cuenta creada correctamente", "success")

@app.route("/Editar", methods=['POST'])
def editar():
    datos = {
        
    }

