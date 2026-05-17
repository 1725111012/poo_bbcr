class Universidad:
  def__init__(self, logo, oferta_educativa, localidad, sistema_informativo, modalidad, servicios, ubicacion, talleres, cantidad_salones, rector):
  
  self.logo = logo
  self.oferta_educativa = oferta_educativa
  self.localidad = localidad
  self.sistema_informativo = sistema_informativo
  self.modalidad = modalidad
  self.servicios = servicios
  self.ubicacion = ubicacion
  self.talleres = talleres
  self.cantidad_salones = cantidad_salones
  self.rector = rector
  
  print("Logotipo de la Universidad: {self.logo}")
  print("Oferta educativa: {self.oferta_educativa}")
  print("Localidad: {self.localidad}")
  print("Sitema informativo: {self.sistema_informativo}")
  print("Modalidad: {self.modalidad}")
  print("Servicios: {self.servicios}")
  print("Ubicación: {self.ubicacion}")
  print("Talleres: {self.talleres}")
  print("Cantidad de salones: {self.cantidad_salones}")
  print("Rector: {self.rector}")

unideh = Universidad("logo.jpg", "Ing. Software, Turismo, Gestión Empresarial", "San Miguel", "CADU", "Virtual", "Biblioteca Virtual", "Santa Catarina", None, None, "Octavio Castillo")
                     
