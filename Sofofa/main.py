import pandas as pd 
from typing import Union
from fastapi import FastAPI, HTTPException

app = FastAPI()
df = pd.read_csv('Subsidios.csv')
db = pd.read_csv('bono.csv')
ds = pd.read_csv('leype.csv')

@app.get("subsidios{region}")
def buscadorsubsidios(region: int):
    if region <= 16:
        in_1 = df[df['REG'] == region]
        print(dict(in_1))
        return in_1.to_dict()
    else:
        print("Region no encontrada")
    raise HTTPException(status_code=404, detail='Esa region no existe')

@app.get("bono {comuna}")
def sal(comuna: str):
    in_2 = db[db['Glosa.Comuna'] == comuna]
    comuna = comuna.upper
    if in_2.empty:
        return 'Comuna no encontrada'
    else:
        return in_2.to_dict()

@app.get("leypresupuestoNOV2022")
def leypresupuesto(mes: str):
    in_3 = ds[ds['Mes']== mes]
    if in_3.empty:
        return 'mes no encontrado, Prueba con la primera letra en mayuscula'
    else:
     return in_3.to_dict()
    


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}