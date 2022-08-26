from io import open

print()
persona=open("Puestos.txt","r+")
solotextolineas = persona.readlines ()
persona.read()
persona.close()


print("============================================")
print("= Bienvenido a su programa de facturación  =")
print("======================================================")
print("= ¿Eres Administrador, Contador o Auxiliar contable? =")
print("======================================================")


class Usuario():
    
    numerodeUsuarios = 3
    
contraseñas = [0,1,2]
puestos = [0,1,2]

name = input("Ingrese el puesto al que pertenece: ")

def puestos(name):
      if name != "Administrador" and name != "Contador" and name !="Auxiliar Contable":
        print ("Nombre de usuario incorrecto")
      else:
        if name == "Administrador":
            print("Usted es el Administrador, bienvenido")
            print("")
            pass_name = input("Ingrese la contraseña del Administrador: ")
            if pass_name != "Admin123":
              print ("Contraseña incorrecta")
            else:
              print ("Bienvenido a la sesión")
              
        elif name == "Contador":
            print("Usted es el contador, bienvenido")
            print("")
            pass_name = input("Ingrese la contraseña del contador: ")
            if pass_name != "Conta123":
                print ("Contraseña incorrecta")
            else:
                print ("Bienvenido a la sesión")
                
        elif name == "Auxiliar Contable":
            print("Usted es el Auxiliar Contable, bienvenido")
            print("")
            pass_name = input("Ingrese la contraseña del Auxiliar Contable: ")
            if pass_name != "Auxconta123":
                print ("Contraseña incorrecta")
            else:
                print ("Bienvenido a la sesión")
puestos(name)
