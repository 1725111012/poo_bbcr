class LibroBiblioteca:
  def __init__(self, titulo, autor, tipo_letra, agradecimientos, tipo_portada, empresa_edicion, numero_paginas, introduccion, imagenes, ano_publicacion)
    self.titulo = titulo 
    self.autor = autor 
    self.tipo_letra = tipo_letra 
    self.agradecimientos = agradecimientos
    self.tipo_portada = tipo_portada
    self.empresa_edicion = empresa_edicion
    self.numero_paginas = numero_paginas 
    self.introduccion = introduccion 
    self.imagenes = imagenes 
    self.ano_publicacion = ano_publicacion 
     
    print(":Título del libro {self.titulo}")
    print(":Autor {self.autor}")
    print(":Tipo de letra {self.tipo_letra}")
    print(":Agradecimientos {self.agradecimientos}")
    print(":Tipo de portada {self.tipo_portada}")
    print(":Empresa de edición {self.empresa_edicion}")
    print(":Número de páginas {self.numero_paginas}")
    print(":Introducción {self.introduccion}")
    print(":Imágenes {self.imagenes}")
    print(":Año de publicación {self.ano_publicacion}")
    
def leer (self): 
    print ("Leer libro")
def hojear (self): 
    print ("Hojear libro")
def vender (self): 
    print ("Vender un libro")
def prestar (self): 
    print ("Prestar libro")
def rayar (self): 
    print ("Rayar libro")
    
el_nino_en_la_cima_de_la_montana = LibroBiblioteca("El niño en la cima de la montaña", "John Boyne", "serif", "A mis editores, familia...", 
"Tapa blanda, 22.00 x 13.50 cm", "Salamandra", "256 páginas", None, None, "2016")

el_nino_en_la_cima_de_la_montana.leer()
el_nino_en_la_cima_de_la_montana.hojear()
el_nino_en_la_cima_de_la_montana.vender()
el_nino_en_la_cima_de_la_montana.prestar()
el_nino_en_la_cima_de_la_montana.rayar()
