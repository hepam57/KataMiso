class Arreglos:
    def GetArreglos(cadena):
        if cadena=="":
            return [None, None]
        elif "," in cadena:
            numeros = cadena.split(",")
            return [len(numeros),int( min(numeros))]
        else:
            return [len(cadena), int(cadena)]
