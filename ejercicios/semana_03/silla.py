class Mesa:
  def __init__(self, soporte, superficie_plana, color, forma_base, material, detalles, peso, ensamble, ancho, dureza):
 
        self.soporte = soporte
        self.superficie_plana = superficie_plana
        self.color = color
        self.forma_base = forma_base
        self.material = material
        self.detalles = detalles
        self.peso = peso
        self.ensamble = ensamble
        self.ancho = ancho
        self.dureza = dureza
        
        print("Soporte de la mesa: {self.soporte}")
        print("Tipo de superficie de la mesa y tamaño: {self.superficie_plana}")
        print("Color de la mesa: {self.color}")
        print("Forma de la base de la mesa: {self.forma_base}")
        print("Material utilizado para la mesa: {self.material}")
        print("Detalles de la mesa: {self.detalles}")
        print("Peso de la mesa: {self.peso}")
        print("Tipo de ensamblaje: {self.ensamble}")
        print("Tamaño del ancho de la mesa: {self.ancho}")
        print("Cantidad que soporta la mesa: {self.dureza}")

        def limpiar (self):
            print ("Limpiar la mesa")
        def prestar (self):
            print ("Prestar la mesa")
        def cargar (self):
            print ("Cargar la mesa")
        def usar (self):
            print ("Usar/usando la mesa")
        def inclinar (self):
            print ("Se puede inclinar la mesa")

mesa_oficina = Mesa("4 patas metálicas", "Tablero rectangular de 120 x 160 cm", "Gris", "Forma de H", "Estrucutra de acero", 
                    "Portavasos y ganchos para bolsas", "25 y 45 kg", "Con tornillos", "De 60 a 80 cm", "Soporta de 30 a 50 kg")

mesa_oficina.limpiar()
mesa_oficina.prestar()
mesa_oficina.cargar()
mesa_oficina.usar()
mesa_oficina.inclinar()