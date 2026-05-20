class Coche:
  def __init__(self, tipo_rines, tipo_llantas, tipo_volante, automatico_estandar, asientos, numero_modelo, asistencia, marca, capacidad_tanque, color):
 
        self.tipo_rines = tipo_rines
        self.tipo_llantas = tipo_llantas
        self.tipo_volante = tipo_volante
        self.automatico_estandar = automatico_estandar
        self.asientos = asientos
        self.numero_modelo = numero_modelo
        self.asistencia = asistencia
        self.marca = marca
        self.capacidad_tanque = capacidad_tanque
        self.color = color
        
        print("Tipo de rines: {self.tipo_rines}")
        print("Tipo de llantas: {self.tipo_llantas}")
        print("Tipo de volante: {self.tipo_volante}")
        print("Cantidad de asientos: {self.automatico_estandar}")
        print("Número de modelo: {self.asientos}")
        print("Asistencia: {self.numero_modelo}")
        print("Marca: {self.asistencia}")
        print("Capacidad del tanque: {self.marca}")
        print("Color: {self.capacidad_tanque}")
        print("Automática o estándar: {self.color}")


        def manejar (self):
            print ("Manejar el coche")
        def chocar (self):
            print ("Cuidado al manejar, podría chocar")
        def atropellar (self):
            print ("Cuidado al manejar, no atropelle a nadie")
        def trasladar (self):
            print ("Trasladar usando un coche")
        def viajar (self):
            print ("Viajar en coche")

nissan = Coche("De aluminio 16 pulgadas", "205/60 R16", "Forrado de piel", "Automatico", "5 asientos", "005", "Bolsas de aire, frenos", "Nissan", "47 litros", "Negro")

nissan.manejar()
nissan.chocar()
nissan.atropellar()
nissan.trasladar()
nissan.viajar()
