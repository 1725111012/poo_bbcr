class Transporte:
  def __init__(self, horario, unidad_transporte, promedio_pasajeros, color, numero_asientos, chofer, numero_unidad, costo, rutas, servicios):
 
  self.horario = horario
  self.unidad_transporte = unidad_transporte
  self.promedio_pasajeros = promedio_pasajeros
  self.color = color
  self.numero_asientos = numero_asientos
  self.chofer = chofer
  self.numero_unidad = numero_unidad
  self.costo = costo
  self.rutas = rutas
  self.servicios = servicios


  print("Horarios: {self.horario}")
  print("Tipo de unidad: {self.unidad_transporte}")
  print("Promedio de pasajeros: {self.promedio_pasajeros}")
  print("Color: {self.color}")
  print("Número de asientos: {self.numero_asientos}")
  print("Nombre del chofer: {self.chofer}")
  print("Número de la unidad: {self.numero_unidad}")
  print("Costo: {self.costo}")
  print("Rutas: {self.rutas}")
  print("Servicios: {self.servicios}")


def viajar (self):
  print ("Viajar en el transporte")
def dormir (self):
  print ("Dormir en el transporte")
def leer (self):
  print ("Leer en el transporte")
def ver (self):
  print ("Viendo en el transporte")
def escuchar (self):
  print ("Escuchar en el transporte")


ado = Transporte("Pachuca: 9:25 AM a 10:00 PM", "Autobus", "3000 pasajeros al día", "Roja con letras blancas", "44 asientos",
"Miguel Angel Soto", "04", "$43", "Ciudad de México, Pachuca, Tampico, Tuxpan", "Aire acondicionado, baño, pantallas, portaequipajes")


ado.viajar()
ado.dormir()
ado.leer()
ado.ver()
ado.escuchar()
