from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
ds = pd.read_csv("leype.csv")
df = pd.read_csv("Subsidios.csv")
db = pd.read_csv("bono.csv")
@app.route('/', methods =["GET", "POST"])

def home():
    return render_template('index.html')

def buscadorsubsidios(region: int):
    if region <= 16:
        in_1 = df[df['REG'] == region]
        print(dict(in_1))
        return in_1.to_dict()
    else:
        print("Region no encontrada")
    return False

def sal(comuna: str):
    in_2 = db[db['Glosa.Comuna'] == comuna]
    comuna = comuna.upper
    if in_2.empty:
        return 'Comuna no encontrada'
    else:
        return in_2.to_dict()

def leypresupuesto(mes: str):
    in_3 = ds[ds['Mes']== mes]
    if in_3.empty:
        return 'mes no encontrado, Prueba con la primera letra en mayuscula'
    else:
     return in_3.to_dict()
    

if __name__ =='__main__':
   app.run