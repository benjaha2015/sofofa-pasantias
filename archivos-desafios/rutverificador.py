import math
rut = input("ingresar rut: ")
rut_lista = []

def enlistar (rut_listado):
    for i in reversed(rut_listado):
        rut_lista.append(i)
def parsearlista(): 
    enlistar(rut)
    for e in range (8):
        rut_lista[e] = int (rut_lista[e])
def calculo():
    parsearlista()
    suma = rut_lista[0]*2 + rut_lista[1]*3 + rut_lista[2]*4 + rut_lista[3]*5 + rut_lista[4]*6 + rut_lista[5]*7 + rut_lista[6]*2 + rut_lista[7]*3
    sumaR = suma / 11
    sumaR = math.trunc(sumaR) * 11
    sumaRes = suma - sumaR
    res = 11 - sumaRes
    if res == 10:
        num_ver = "k"
    elif res == 11:
        num_ver = 0
    else:
        num_ver = res
        
    return num_ver

def crearTXT():
        num_verificador = calculo()
        archivo = open("Rut.txt","w")
        archivo.write(str(rut) + "-" + str(num_verificador))
        archivo.close()
        

crearTXT()
            