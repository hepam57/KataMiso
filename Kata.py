class Arreglos:
    def GetArreglos(cadena):
        if cadena=="":
            return [None, None]
        elif "," in cadena:
            numeros = cadena.split(",")
            return [len(numeros)]
        else:
            return [len(cadena)]
