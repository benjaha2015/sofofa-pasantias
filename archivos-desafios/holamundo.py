cadena = str(input("ingresa una palabra: "))
if cadena ==''.join(reversed(cadena)):
    print("es palindroma")
else:
    print("no es palindroma")