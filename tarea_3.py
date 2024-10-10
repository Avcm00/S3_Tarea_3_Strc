#1. Define una clase Libro con atributos para título, autor, y año de publicación.
# Incluye un método que devuelva una descripción completa del libro
class Libro:
    def __init__(self,titulo, autor, año_publicacion):
        self.titulo = titulo    #O(1)
        self.autor = autor  #O(1)
        self.año_publicacion = año_publicacion  #O(1)
    def __str__(self):
        return f'El libro {self.titulo} es del autor{self.autor} y fue publicado en {self.año_publicacion}' #O(1)
    
libro_1 = Libro('don Quijote de la mancha', 'Miguel de servantes',1604)
print(libro_1)
#Big O:#O(1)

#2. Crea una clase Círculo que tenga un atributo radio y un método para calcular el
#área (usa 3.14 como aproximación de π).

class Circulo:
    def __init__(self,radio):
        self.radio = radio#O(1)
        self.pi = 3.14#O(1)
    
    def calcular_area(self):
        return f'El area del circulo es {self.pi*self.radio**2}'#O(1)

circulo_1 = Circulo(radio=12)#O(1)
print(circulo_1.calcular_area())
#Big O:#O(1)
#3. Desarrolla una clase Persona con atributos nombre y edad, y un método para imprimir un saludo 
# que incluya su nombre

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre    #O(1)
        self.edad = edad    #O(1)

    def saludo(self):
        return f'Hola, me llamo {self.nombre} y tengo {self.edad}'  #O(1)
persona_1 = Persona(nombre='Luis',edad= 20) #O(1)
print(persona_1.saludo())
#Big O:#O(1)

#4. Implementa una clase CuentaBancaria que tenga atributos para el saldo inicial, y métodos para depositar,
#retirar y mostrar el saldo actual.

class CuentaBancaria :
    def __init__(self,saldoinicial):
        self.saldoinicial = saldoinicial    #O(1)

    def depositar(self,deposito):
        if deposito > 0:        #O(1)
            self.saldoinicial += deposito       #O(1)
            return f'saldo actual {self.saldoinicial}'
        else:
            return f'deposito no valido'    #O(1)
    def retirar(self,retiro):
        if self.saldoinicial >= retiro: #O(1)
            self.saldoinicial -= retiro     #O(1)
            return f'saldo actual {self.saldoinicial}'      #O(1)
        else:
            return f'retiro no valido'
    def saldoactual(self):
            return f'saldo actual {self.saldoinicial}'      #O(1)
    
cuenta_1 = CuentaBancaria(saldoinicial=1000)    #O(1)
cuenta_1.depositar(100)     #O(1)
print(cuenta_1.saldoactual())       #O(1)
cuenta_1.retirar(500)       #O(1)
print(cuenta_1.saldoactual())
#Big O #O(1)
#5. Crea una clase Rectángulo con atributos largo y ancho, y métodos para calcula área y perímetro.
class Rectangulo:
    def __init__(self,largo,ancho):
        self.largo = largo      #O(1)
        self.ancho = ancho      #O(1)
    def area(self):
        return f'El area del rectangulo es {self.ancho * self.largo}'       #O(1)
    def perimetro(self):
        return f'El perimetro del rectangulo es {(self.ancho + self.largo)*2}'      #O(1)
    
rectangulo_1 = Rectangulo(largo= 12, ancho= 24)     #O(1)
print(rectangulo_1.area())
print(rectangulo_1.perimetro())
#Big O #O(1)

#6. Desarrolla una clase Coche con atributos marca, modelo y kilómetros recorridos, y un método para mostrar
#la información del coche.

class Coche:
    def __init__(self,marca,modelo,kilometrosre):
        self.marca= marca       #O(1)
        self.modelo = modelo        #O(1)
        self.kilometrosre= kilometrosre     #O(1)
    def informacion(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, kilometros recorridos: {self.kilometrosre}'        #O(1)
    
coche_1 = Coche(marca='Chevrolet', modelo='Camaro', kilometrosre= 12000)        #O(1)
print(coche_1.informacion())
#Big O #O(1)

#7. Implementa una clase Estudiante que herede de Persona y añade un atributo grado.
#Sobrescribe el método de saludo para incluir su grado de estudio.
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)      #O(1)
        self.grado = grado      #O(1)
    def saludo(self):
        return f'Hola , me llamo {self.nombre} tengo {self.edad} grado {self.grado} '       #O(1)

estudiante = Estudiante(nombre= 'Enrique',edad= 21, grado= 2)       #O(1)
print(estudiante.saludo())
#Big O #O(1)
#8. Crea una clase Vector con atributos para coordenadas x e y, y métodos para sumar dos vectores y 
#multiplicar un vector por un escalar.
class Vector:
    def __init__(self, x, y):
        self.x = x          #O(1)
        self.y = y          #O(1)

    def sumar(self, otro_vector):
        suma_x = self.x + otro_vector.x     #O(1)
        suma_y = self.y + otro_vector.y     #O(1)
        return Vector(suma_x, suma_y)       #O(1)

    def multiplicar_por_escalar(self, escalar):
        return Vector(self.x * escalar, self.y * escalar)       #O(1)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"        #O(1)

vector_1 = Vector(2, 3)     #O(1)
vector_2 = Vector(4, 5)     #O(1)
vector_suma = vector_1.sumar(vector_2)      #O(1)
print(f"La suma de los vectores es: {vector_suma}")
escalar = 3     #O(1)
vector_multiplicado = vector_1.multiplicar_por_escalar(escalar)     #O(1)
print(f"El vector {vector_1} multiplicado por el escalar {escalar} es: {vector_multiplicado}")
#Big O #O(1)

#9. Desarrolla una clase Email que tenga atributos para el remitente, destinatario, 
# asunto y cuerpo del mensaje. Incluye un método para "enviar" el email, imprimiendo el contenido.
class Email:
    def __init__(self,remitente,destinatario,asunto,cuerpodemensaje):
        self.remitente= remitente       #O(1)
        self.destinatario = destinatario        #O(1)
        self.asunto = asunto        #O(1)
        self.cuerpodemensaje= cuerpodemensaje       #O(1)
    def enviar(self):
        return f'Remitente: {self.remitente} \n Destinatario: {self.destinatario}\n Asunto {self.asunto} \n {self.cuerpodemensaje}'     #O(1)

email_1 = Email("hola","hol","holo","kasjdkjaskdjajsdlkajsdalksdj")     #O(1)
print(email_1.enviar())
#Big O #O(1)

#10. Implementa una clase AgendaTelefonica que almacene nombres y números de teléfono en un diccionario,
#  con métodos para añadir, eliminar, y buscar contactos

class AgendaTelefonica:
    def __init__(self):
        self.contactos = {}     #O(1)

    def agregar_contacto(self, nombre, telefono):
        if nombre not in self.contactos:    #O(1)
            self.contactos[nombre] = telefono       #O(1)
            return f'Contacto {nombre} añadido con el número {telefono}.'
        else:
            return f'El contacto {nombre} ya existe.'   #O(1)

    def eliminar_contacto(self, nombre):
        if nombre in self.contactos:        #O(1)
            del self.contactos[nombre]      #O(1)
            return f'Contacto {nombre} eliminado.'
        else:
            return f'El contacto {nombre} no existe.'       #O(1)

    def buscar_contacto(self, nombre):
        if nombre in self.contactos:        #O(1)
            return f'El número de {nombre} es {self.contactos[nombre]}.'
        else:
            return f'El contacto {nombre} no se encuentra en la agenda.'        #O(1)

    def mostrar_contactos(self):
        if self.contactos:      #O(1)
            return f'Lista de contactos: {self.contactos}'  #O(n)
        else:
            return 'La agenda está vacía.'      

agenda = AgendaTelefonica()     #O(1)
print(agenda.agregar_contacto('Ana', '123456789'))
print(agenda.agregar_contacto('Pedro', '987654321'))
print(agenda.buscar_contacto('Ana'))
print(agenda.eliminar_contacto('Pedro'))
print(agenda.mostrar_contactos())
#Big O#O(n)
#11. Crea una clase Animal con un método hablar que simplemente imprima "Este animal hace un sonido".
#  Luego, crea clases Perro y Gato que hereden de Animal y sobrescriban el método hablar para que imprima 
# "Guau" y "Miau", respectivamente
class Animal:
    def hablar(self):
        return "Este animal hace un sonido."    #O(1)

class Perro(Animal):
    def hablar(self):
        return "Guau"   #O(1)

class Gato(Animal):
    def hablar(self):
        return "Miau"       #O(1)

perro = Perro()     #O(1)
gato = Gato()       #O(1)
print(perro.hablar())  
print(gato.hablar())   
#Big O:#O(1)
#12. Crea una clase Empleado con atributos nombre y salario, y un método para mostrar estos datos. 
# Luego, crea una clase Gerente que herede de Empleado y añade un atributo para el departamento.

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre    #O(1)
        self.salario = salario      #O(1)

    def mostrar_datos(self):
        return f'Nombre: {self.nombre}, Salario: {self.salario}'    #O(1)

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
       
        super().__init__(nombre, salario)   #O(1)
        self.departamento = departamento  #O(1)

    def mostrar_datos(self):
        return f'Nombre: {self.nombre}, Salario: {self.salario}, Departamento: {self.departamento}'     #O(1)

empleado = Empleado(nombre='Ana', salario=30000)        #O(1)
print(empleado.mostrar_datos())  

gerente = Gerente(nombre='Luis', salario=50000, departamento='Ventas')      #O(1)
print(gerente.mostrar_datos()) 
#Big O:#O(1)
#13. Utiliza la herencia para crear varias clases de animales que tengan un método común moverse, 
# pero que se comporte diferente para cada animal (por ejemplo, los peces nadan, las aves vuelan).

class Animal:
    def moverse(self):
        return "Este animal se mueve de alguna manera."     #O(1)
class Pez(Animal):
    def moverse(self):
        return "El pez nada."       #O(1)
class Ave(Animal):
    def moverse(self):
        return "El ave vuela."      #O(1)

class Perro(Animal):
    def moverse(self):
        return "El perro camina o corre."       #O(1)

class Serpiente(Animal):
    def moverse(self):
        return "La serpiente se arrastra."      #O(1)

pez = Pez()     #O(1)
ave = Ave()     #O(1)
perro = Perro()     #O(1)
serpiente = Serpiente()     #O(1)

print(pez.moverse())       
print(ave.moverse())       
print(perro.moverse())     
print(serpiente.moverse()) 
#Big O:#O(1)
