import pandas as pd
print("Hola, bienvenido a mi buscador. Antes que empieces a usarlo tendras que entrar a esta pagina para poder entender lo de los subsidios")
print ("https://ide.minvu.cl/datasets/fl-subsidios-de-arriendo-ds52/explore?location=-33.626280%2C-70.323292%2C8.77")
print("Solo si no sabe del numero de provincia, por como funciona aca ")
print("Como le gustaria buscar su zona? por region(es de las primeras zonas de su region) o provincia?")
def sal(Var_region):
 if Var_region <= 16:
  in_1 = db[db['REG'] == Var_region]

  return(in_1)
 else:
    print("Region no encontrada")
    return False

# codigo 
db = pd.read_csv('Subsidios.csv')
Var_region = int(input("Ingrese la region: "))
df_region = sal(Var_region)
print(df_region.head())

