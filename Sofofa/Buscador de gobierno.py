import pandas as pd
df = pd.read_csv('Subsidios.csv')
db = pd.read_csv('bono.csv')
ds = pd.read_csv('leype.csv')
print("Ahora mismo estan disponibles: subsidios, bono")
elige = input("Que quiere buscar: ")

def identi(elige):
 if elige == "subsidios":
  print ("Bienvenido a la seccion de subsidios")
  Var_region = int(input("Ingrese la region: "))
  print(sala(Var_region))
  return (elige)
 elif elige == "bono":
    print("Bienvenido a la seccion bonos")
    Var_comuna = (input("Ingrese la comuna: "))
    Var_comuna = Var_comuna.upper()
    print(sal(Var_comuna))
    return elige
 elif elige == "presupuestoNOV2022":
    print("Estan son la ley de presupuesto de noviembre 2022")
    print(ds)

def sala(Var_region):
    
 if Var_region <= 16:
  in_1 = df[df['REG'] == Var_region]

  return(in_1)
 else:
    print("Region no encontrada")
    return False




def sal(Var_comuna):
    in_2 = db[db['Glosa.Comuna'] == Var_comuna]
    if in_2.empty:
        return 'Comuna no encontrada'
    else:
        return in_2.head()
        

 
print(identi(elige))