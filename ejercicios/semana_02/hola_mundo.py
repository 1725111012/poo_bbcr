class HolaMundo:

    def __init__(self):
        print("Constructor")

    def metodoUno(self):
        print("Método Uno")

    def metodoDos(self, variable_uno:int, varible_dos:int)->int:
        """
        Este método recibe dos variables enteras, las suma y regresa
        el resultado de la suma

        Args:

        variable_uno:int - Primer número entero
        variable_dos:int - Segundo número entero

        Return:

        suma : int - Suma de los dos números enteros
        """
        suma = variable_uno + varible_dos
        return int(suma)

    def metodoTres(self, varible_tres:str)->None:
        print(f"Número de caracteres: {len(variable_tres)}")

nombre_objeto = HolaMundo()
nombre_objeto.metodoUno()
