from io import open

#ENCABEZADO DEL PROGRAMA

print()
print("============================================")
print("= Bienvenido a su programa de facturación  =")
print("======================================================")
print("= ¿Eres Administrador, Contador o Auxiliar contable? =")
print("======================================================")
print("")

#ARCHIVOS TXT DE DONDE VAMOS A TOMAR LOS DATOS A ASIGNAR

name = input("¿A qué puesto pertenece?: ")

persona = open("Puestos.txt","r+")
for i in persona.readlines():
      if i.find(name) >= 0:
        print ("Puesto encontrado")
      else:
        print ("Puesto no encontrado")
persona.close()       

#NUESTRA FUNCIÓN RESPONSABLE DE REALIZAR LAS ASIGNACIONES  DESPUES DE CONSULTAR LOS DATOS 

def puestos(name):
      if name != "Administrador" and name != "Contador" and name !="Auxiliar Contable":
        print ("Nombre de usuario incorrecto")
      else:
        if name == "Administrador":
            print("Usted es el Administrador, Bienvenido")
            print("")
            pass_name = input("Ingrese la contraseña del Administrador: ")
            if pass_name != "Admin123":
              print ("Contraseña incorrecta")
            else:
              print ("Bienvenido a la sesión")
              
        elif name == "Contador":
            print("Usted es el contador, Bienvenido")
            print("")
            pass_name = input("Ingrese la contraseña del contador: ")
            if pass_name != "Conta123":
                print ("Contraseña incorrecta")
            else:
                print ("Bienvenido a la sesión")
                
        elif name == "Auxiliar Contable":
            print("Usted es el Auxiliar Contable, Bienvenido")
            print("")
            pass_name = input("Ingrese la contraseña del Auxiliar Contable: ")
            if pass_name != "Auxconta123":
                print ("Contraseña incorrecta")
            else:
                print ("Bienvenido a la sesión")
puestos(name)