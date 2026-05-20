class Silla:
  def __init__(self, respaldo, asiento, material, patas, altura, peso, capacidad_carga, color, descansabrazos, estilo):
 
        self.respaldo = respaldo
        self.asiento = asiento
        self.material = material
        self.patas = patas
        self.altura = altura
        self.peso = peso
        self.capacidad_carga = capacidad_carga
        self.color = color
        self.descansabrazos = descansabrazos
        self.estilo = estilo
        
        print("La silla tienen respaldo: {self.respaldo}")
        print("La silla es un asiento: {self.asiento}")
        print("Material del que se hizo la silla: {self.material}")
        print("Total de patas: {self.patas}")
        print("Altura de la silla: {self.altura}")
        print("Peso de la silla: {self.peso}")
        print("Capacidad de carga de la silla: {self.capacidad_carga}")
        print("Color de la silla: {self.color}")
        print("¿Usa descansabrazos?: {self.descansabrazos}")
        print("Tipo de estilo de la silla: {self.estilo}")

        def sentarse (self):
            print ("Te puedes sentar en una silla")
        def mover (self):
            print ("Mover la silla")
        def levantar (self):
            print ("Levanta la silla")
        def acomodar (self):
            print ("Acomodar la silla, por favor")
        def prestar (self):
            print ("Prestame la silla, por favor")

silla_giratoria = Silla("De malla", "Alconchonada", "Tapiz en tela", "Base de 5 ruedas", "Ajustable", "12 kilogramos", "150 kilogramos", "Negro", "Fijos", "Gamer")

silla_giratoria.sentarse()
silla_giratoria.mover()
silla_giratoria.levantar()
silla_giratoria.acomodar()
silla_giratoria.prestar()
