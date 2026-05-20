class PersonajeJuego:
  def __init__(self, nombre, personalidad, rol, juego, genero, raza, vida_hp, poderes, voz, debilidad):
 
        self.nombre = nombre
        self.personalidad = personalidad 
        self.rol = rol 
        self.juego = juego
        self.genero = genero
        self.raza = raza
        self.vida_hp = vida_hp 
        self.poderes = poderes
        self.voz = voz
        self.debilidad = debilidad
        
        print("Nombre de los personaje: {self.nombre}")
        print("Personalidad del personaje: {self.personalidad}")
        print("Rol que cumple en el juego: {self.rol}")
        print("Juego donde esta el personaje: {self.juego}")
        print("Genéro del personaje: {self.genero}")
        print("Raza del personaje: {self.raza}")
        print("Vida del personaje: {self.vida_hp}")
        print("Poderes que tiene el personaje: {self.poderes}")
        print("¿Tiene voz el personaje?: {self.voz}")
        print("Debilidad del personaje: {self.debilidad}")

        def caminar (self):
            print ("El personaje puede caminar")
        def teletransportarse (self):
            print ("El personaje puede teletransportarse")
        def curarse (self):
            print ("El personaje puede curarse")
        def interactuar (self):
            print ("Se puede interactuar con el personaje")
        def morir (self):
            print ("Cuidado, el personaje puede morir")

sans = PersonajeJuego("Sans el esqueleto", "Flojo, sarcastico y bromista", "NPC/Jefe final", "Undertale", "Maculino", "Monstruo, esqueleto", "1 HP", 
                        "Teletransportación, control de gravedad de las almas, huesos, gaster blasters", None, "Solo tiene 1 HP, muere de un golpe")

sans.caminar()
sans.teletransportarse()
sans.curarse()
sans.interactuar()
sans.morir()

