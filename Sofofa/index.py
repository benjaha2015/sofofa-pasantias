from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
ds = pd.read_csv("leype.csv")
df = pd.read_csv("SUBa.csv")
db = pd.read_csv("bono.csv")
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/buscador', methods =["GET", "POST"])
def BUSCADOR(busca: str):
 busca = request.form["busca"]
 if busca == "subsidios":
  print ("Bienvenido a la seccion de subsidios")
  tipo = int(input("Ingrese la region: "))
  print(buscadorsubsidios(tipo))
  return render_template('index.html', )

 elif busca == "bono":
    print("Bienvenido a la seccion bonos")
    tipo = (input("Ingrese la comuna: "))
    tipo = tipo.upper()
    print(sal(tipo))
    return busca

 elif busca == "Ley presupuesto":
    print("Bienvenido a la ley de presupuesto,")
    tipo = input("Eliga el mes de la ley: ")
    print(leypresupuesto(tipo))
def buscadorsubsidios(tipo: str):
        in_1 = df[df['REG'] == tipo]
        if in_1.empty:
            return 'Region no encontrada, trata con la primera letra en mayuscula'
        else:
            return in_1.to_dict()
def sal(tipo: str):
    in_2 = db[db['Glosa.Comuna'] == tipo]
    tipo = tipo.upper
    if in_2.empty:
        return 'Comuna no encontrada'
    else:
        return in_2.to_dict()
def leypresupuesto(tipo: str):
    in_3 = ds[ds['Mes']== tipo]
    if in_3.empty:
        return 'mes no encontrado, Prueba con la primera letra en mayuscula'
    else:
     return in_3.to_dict()

if __name__ =='__main__':
   app.debug = True
   app.run()