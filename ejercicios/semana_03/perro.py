class Perro:
  def __init__(self, nombre, raza, dueño, personalidad, edad, peso, alimentacion, pelaje, color, estatura_longitud):
 
        self.nombre = nombre
        self.raza = raza
        self.dueño = dueño
        self.personalidad = personalidad
        self.edad = edad
        self.peso = peso
        self.alimentacion = alimentacion
        self.pelaje = pelaje
        self.color = color
        self.estatura_longitud = estatura_longitud
        
        print("Nombre del perro: {self.nombre}")
        print("Raza del perro: {self.raza}")
        print("Nombre del dueño: {self.dueño}")
        print("Personalidad del perro: {self.personalidad}")
        print("Edad del perro: {self.edad}")
        print("Peso del perro: {self.peso}")
        print("¿Qué es lo que come su perro?: {self.alimentacion}")
        print("Tipo de pelaje: {self.pelaje}")
        print("Color del pelaje: {self.color}")
        print("¿Cuánto mide su perro?: {self.estatura_longitud}")

        def jugar (self):
            print ("Jugar con el perro")
        def alimentar (self):
            print ("Darle del comer al perro")
        def acariciar (self):
            print ("Acaricia al perro")
        def pasear (self):
            print ("Pasear al perro")
        def dormir (self):
            print ("No dormir con el perro")    

cocker_spaniel = Perro("Toby", "Yhatziri Daniela", "Cocker Spaniel Americano", "Alegre, juguetón y travieso", "1 año", "11 kg", 
                        "Croquetas y pollo", "Rizado y un poco largo", "Café", "37 a 39 cm / 55 a 65 cm")

cocker_spaniel.jugar()
cocker_spaniel.alimentar()
cocker_spaniel.acariciar()
cocker_spaniel.pasear()
cocker_spaniel.dormir()
