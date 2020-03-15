class Arreglos:
    def GetArreglos(cadena):
        if cadena == "":
            return [None, None, None, None]
        elif "," in cadena:
            numeros = cadena.split(",")
            return [len(numeros), int(min(numeros)), int(max(numeros))]
        else:
            return [1, int(cadena), int(cadena), int(cadena)]
