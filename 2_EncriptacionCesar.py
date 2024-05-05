""" 
Cifrado de Cesar
Es un tipo de cifrado por sustitución en el que una letra en el texto original es reemplazada
por otra letra que se encuentra un número fijo - clave - de posiciones más adelante en el alfabeto.
"""


def cifradoCesar(texto:str, clave:int):
    textoEncriptado = ""
    abecNormal = "abcdefghijklmnopqrstuvwxyz"
    abecEncrip = abecNormal[clave:] + abecNormal[:clave]
    
    for letra in texto.lower():
        try:
            indiceAbecNormal = abecNormal.index(letra.lower())
            textoEncriptado += abecEncrip[indiceAbecNormal]
        except:
            textoEncriptado += " "

    return textoEncriptado

def descriptarCesar(textoEncriptado:str, clave:int):
    textoNormal = ""
    abecNormal = "abcdefghijklmnopqrstuvwxyz"
    abecEncrip = abecNormal[clave:] + abecNormal[:clave]
    
    for letraEncrip in textoEncriptado:
        try:
            indiceAbecEncriptado = abecEncrip.index(letraEncrip)
            textoNormal += abecNormal[indiceAbecEncriptado]
        except:
            textoNormal += " "
    
    return textoNormal

print("Cifrado de cesar".center(30, "-"))
texto = input("Ingrese un texto para cifrar: ")
clave = int(input("Ingrese la clave de cifrado: "))

print(f"Texto original: {texto}")
print(f"Texto cifrado: {cifradoCesar(texto, clave)}")
