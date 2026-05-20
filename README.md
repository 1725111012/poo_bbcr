# Repositorio de Programación Orientada a Objetos

Repositorio con ejercicios de Programación Orientada a Objetos

## 1.Crear .gitignore

Crear el archivo .gitignore para configurar los archivos y carpetas que no deseamos que se guarden en el repositorio.

````shell
*pyc
_pycache/
````

## 2. Indexar archivos y carpetas

Indexa todos los directorios y carpetas en busca de archivos de documentos nuevos.

````shell
git add .
````

## 3. Crear un COMMIT

Crea un commit o punto de control de los cambios realizados en el proyecto.

````shell
git commit -m "CREATE .gitignore"
````

* CREATE - Se crearon nuevas carpetas o archivos.
* UPDATE - Se actualizaron o agregaron nuevas funciones.
* FIXED - Se corrigeron errores.


## 4. Realizar el COMMIT

Sincroniza los cambios realizados y los repositorios.

````shell
git push -u origin main
````

## 5. Agregar Documentación a los métodos

Agregar un **Docstring** a los métodos generados

````shell
1. En la documentación, se pone primeramente una descripción de lo que hace el código o ese pedazo de código. 
2. Después de ello, se pone los tipos de variables que se usaron y para que se usaron.
3. La tercera parte, dice si va a regresar algo el código hasta el final.
        """
        Este método recibe dos variables enteras, las suma y regresa
        el resultado de la suma

        Args:

        variable_uno:int - Primer número entero
        variable_dos:int - Segundo número entero

        Return:

        suma : int - Suma de los dos números enteros
        """
*Argos: Abreviación de “Argumentos”
````
