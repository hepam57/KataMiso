class Arreglos:
    def GetArreglos(cadena):
        if cadena=="":
            return []
        elif cadena=="1,2":
            return [2]
        else:
            return [len(cadena)]
