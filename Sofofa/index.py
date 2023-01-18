from flask import Flask, request, render_template, request, session, redirect
import numpy as np
import pandas as pd
app = Flask(__name__)
ds = pd.read_csv("leype.csv")
df = pd.read_csv("SUBa.csv")
db = pd.read_csv("bono.csv")
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/buscador', methods =["GET", "POST"])

def BUSCADOR():
 busca = request.form["busca"]
 if busca == "subsidios":
  print ("Bienvenido a la seccion de subsidios")
  print(buscadorsubsidios())
  return render_template('simple.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)
 elif busca == "bono":
    print("Bienvenido a la seccion bonos")
    print(sal())
    return render_template('simple.html',  tables=[db.to_html(classes='data')], titles=df.columns.values)
 elif busca == "Ley presupuesto":
    print("Bienvenido a la ley de presupuesto,")
    print (leypresupuesto())
    
def buscadorsubsidios():
        tipo = request.form["tipo"]
        in_1 = df[df['Región'] == tipo]
        if in_1.empty:
            return 'Region no encontrada, trata con la primera letra en mayuscula'
        else:
            return in_1.to_dict
def sal():
    tipo = request.form["tipo"]
    in_2 = db[db['Glosa.Comuna'] == tipo]
    tipo = tipo.upper
    if in_2.empty:
        return 'Comuna no encontrada'
    else:
        return in_2.to_html
def leypresupuesto():
    tipo = request.form["tipo"]
    in_3 = ds[ds['Mes']== tipo]
    if in_3.empty:
        return 'mes no encontrado, Prueba con la primera letra en mayuscula'
    else:
     return in_3.to_dict()
if __name__ =='__main__':
   app.debug = True
   app.run(host='0.0.0.0')