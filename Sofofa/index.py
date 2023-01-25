from flask import Flask, request, render_template, request, session, redirect
import numpy as np
import pandas as pd
import os
app = Flask(__name__)
ds = pd.read_csv("leype.csv")
df = pd.read_csv("SUBa.csv")
db = pd.read_csv("bono.csv")
IMG_FOLDER = os.path.join('static', 'IMG')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER
@app.route('/')
def Display_IMG():
    Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'Logo_gobierno.png')
    return render_template("index.html", user_image=Flask_Logo)
def home():
    return render_template('index.html')

@app.route('/', methods =["GET", "POST"])
def BUSCADOR():
 busca = request.form["busca"]
 tipo = request.form["tipo"]
 if busca == "subsidios":
  
  in_1 = df[df['Región'] == tipo]
  if in_1.empty:
     return 'Region no encontrada, trata de ser mas preciso'
  else:
     return render_template('index.html',  tables=[in_1.to_html(classes='data')], titles=in_1.columns.values)
 elif busca == "bono":
    print("Bienvenido a la seccion bonos")
    in_2 = db[db['Glosa.Comuna'] == tipo]
    tipo = tipo.upper
    if in_2.empty:
        return 'Comuna no encontrada, prueba con todo en mayuscula'
    else:
        return render_template('index.html',  tables=[in_2.to_html(classes='data')], titles=in_2.columns.values)
 elif busca == "Ley presupuesto":
    print("Bienvenido a la ley de presupuesto,")
    in_3 = ds[ds['Mes']== tipo]
    if in_3.empty:
        return 'mes no encontrado, Prueba con la primera letra en mayuscula'
    else:
        print("Esto es lo que se encontro con el mes elegido")
        return render_template('index.html',  tables=[in_3.to_html(classes='data')], titles=in_3.columns.values)

if __name__ =='__main__':
   app.debug = True
   app.run(host='0.0.0.0')