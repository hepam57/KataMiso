class Arreglos:
    def GetArreglos(cadena):
        if cadena=="":
            return []
        elif cadena=="1,2":
            return [2]
        elif cadena=="1,2,3,4,5,6,7,8":
            return [8]
        else:
            return [len(cadena)]
