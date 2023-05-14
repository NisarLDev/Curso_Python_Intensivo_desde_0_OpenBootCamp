import hashlib

def hash():
    hashlib.sha256()
    m = hashlib.sha256()
    password = input('Introduzca una contraseña alfanumérica que tenga entre 6 y 12 caracteres: ')
    longitud = len(password)
    if longitud in range(6, 12):
        m = hashlib.sha256(password.encode("UTF-8"))
        print(m.hexdigest())
    else:
        print("Las características de la contraseña no son computables\n La contraseña no tiene la longitud exigida")
      
if __name__ == '__main__':
    hash()
