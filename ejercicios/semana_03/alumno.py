class Alumno:
  def __init__(self, matricula, nombre, carrera_cursa, institucion_cursa, grado, edad, material, materias, horario, becas):
 
        self.matricula = matricula
        self.nombre = nombre
        self.carrera_cursa = carrera_cursa
        self.institucion_cursa = institucion_cursa
        self.grado = grado
        self.edad = edad
        self.material = material
        self.materias = materias
        self.horario = horario
        self.becas = becas
        
        print("Matricula del estudiante: {self.matricula}")
        print("Nombre del estudiante: {self.nombre}")
        print("Carrera que esta cursando: {self.carrera_cursa}")
        print("Institución donde cursa su carrera: {self.institucion_cursa}")
        print("Grado o nivel del estudiante: {self.grado}")
        print("Edad del alumno: {self.edad}")
        print("Material que el alumno usa: {self.material}")
        print("Materias que cursa el alumno: {self.materias}")
        print("Horario de asistencia del alumno: {self.horario}")
        print("¿El alumno cuenta con beca?: {self.becas}")

        def estudiar (self):
            print ("El alumno va a estudiar para un examen")
        def aprender (self):
            print ("El alumno va a aprender")
        def cursar (self):
            print ("El alumno cursa un grado")
        def escribir (self):
            print ("El alumno escribe")
        def asistir (self):
            print ("El alumno asiste a clases")

alumna_utec = Alumno("1725111012", "Betzaida Belén", "TIC'S", "Unversidad Tecnológica de Tulancingo", "3er cuatrimestre", 
                    "19 años", "Libreta, labtops, lapiceros", "Calculo Integral, Programacón Orientada a Objetos", "De 7:00 a 3:00 PM", None)

alumna_utec.estudiar()
alumna_utec.aprender()
alumna_utec.cursar()
alumna_utec.escribir()
alumna_utec.asistir()
