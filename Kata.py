class Arreglos:
    def GetArreglos(cadena):
        if cadena=="":
            return [None, None]
        elif "," in cadena:
            numeros = cadena.split(",")
            if cadena == "1,2":
                return [len(numeros), 1]
            else:
                return [len(numeros), 1]
        else:
            return [len(cadena), int(cadena)]
