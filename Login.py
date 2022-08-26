from io import open

<<<<<<< HEAD
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
=======
print("Bienvenido a su programa de facturación")

class Usuario():
    
    administrativos=open("Puestos.txt","w")
    puestos=["Administrador","Contador","Auxiliar contable"]
    contraseñas=["Admin123","Conta123","Auxcont123"]


    puestos={}
    contraseñas={}
    
    administrativos
    
    numerodeUsuarios = 3

    def __init__(self, puestos, contraseñas):
        
        self.puestos = puestos
        self.contraseñas = contraseñas
        
        self.enlinea = False
        self.intentos = 3
        
        Usuario.numerodeUsuarios+=1
        
    def Iniciar_Sesion(self, puestos, contraseñas):
        print()
        MiPuesto = input("Escriba su puesto de trabajo: ")
        print()
        Micontraseña = input("Escriba su contraseña: ")
        
        if Micontraseña==contraseñas[0]:
            print()
            print(" >>> Ha iniciado sesión exitosamente <<< ")
            self.enlinea = True
            
        else:
            self.intentos-=1
            if self.intentos > 0:
                print()
                print (" * UPS, Contraseña Incorrecta, ingrese su contraseña de nuevo")
                print()
                print ("Te quedan: ", self.intentos, "intentos" )
                self.Iniciar_Sesion()
                
            else:
                print("No se pudo Iniciar Sesión")
                print(" * Failed * ")    
 
    print()  
          
    def Cerrar_Sesion(self):
        
        if self.enlinea:
            print(" >>> La sesión cerro correctamente <<<")        
            self.enlinea = False
            
        else:
            print(" >>> No ha iniciado sesión <<< ")
            
    def __str__(self):
        
        if self.enlinea:
            conect = "En línea"
            
        else:
            conect = "Fuera de línea"
        print()
        return f"Mi nombre de usuario es {self.puestos} y me encuentro {conect}"
        print()
print()  
usuario1 = Usuario(input("Ingrese su puesto: "), input("Ingrese su contraseña: "))
print(usuario1)    
usuario1.Iniciar_Sesion()
>>>>>>> 330c86df9f3291c000ea85fe1b719978dbaf3658
