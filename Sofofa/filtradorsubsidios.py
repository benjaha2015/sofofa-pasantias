import pandas as pd

def sal(Var_comuna):
    in_1 = db[db['Glosa.Comuna'] == Var_comuna]
    if in_1.empty:
        return 'Comuna no encontrada'
    else:
        return in_1.head()

# codigo 
db = pd.read_csv('bono.csv')
Var_comuna = (input("Ingrese la comuna: "))
Var_comuna = Var_comuna.upper()
print(sal(Var_comuna))

