import pandas as pd 

df = pd.read_csv('Subsidios.csv')
db = pd.read_csv('bono.csv')
ds = pd.read_csv('leype.csv')

busca = input("Que quiere buscar: ")
 
def buscador(busca):
    if busca == "subsidios":
        region = input(int("eliga su region"))
        return buscadorsubsidios
    elif busca == "bono":
     return sal
    elif busca == "leypresupuesto":
        return leypresupuesto
    else:
        return "no se ha encontrado nada con eso, prueba otra vez"

def buscadorsubsidios(region: int):
    if region <= 16:
        in_1 = df[df['REG'] == region]
        print(dict(in_1))
        return in_1
    else:
        print("Region no encontrada")
    return False

def sal(comuna: str):
    in_2 = db[db['Glosa.Comuna'] == comuna]
    comuna = comuna.upper
    if in_2.empty:
        return 'Comuna no encontrada'
    else:
        return in_2

def leypresupuesto(mes: str):
    in_3 = ds[ds['Mes']== mes]
    if in_3.empty:
        return 'mes no encontrado, Prueba con la primera letra en mayuscula'
    else:
     return in_3