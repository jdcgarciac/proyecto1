from random import * 
import os

clave = input("Ingrese su clave:  ")
pwd = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o",
"p","q","r","s","t","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0",]
print(len(pwd))
pw = ""
    
while(pw != clave):
    pw = ""
    for letra in range(len(clave)):
        obtener_clave = pwd[randint(0,35)]
        pw = str(obtener_clave) + str(pw)
        print(pw)
        print("Obteniendo su clave....... Por favor espere!!!")
        os.system("cls")
print(f"Su clave es: {pw}")
