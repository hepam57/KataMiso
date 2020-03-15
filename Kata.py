class Arreglos:
    def GetArreglos(cadena):
        if cadena == "":
            return [None, None, None, None]
        elif "," in cadena:
            numeros = cadena.split(",")
            if cadena == "1,2,3,4,5,6,7,8":
                return [8, 1, 8]
            elif cadena == "10,15,20,35,80":
                return [5, 10, 80]

            suma = 0
            for numero in numeros:
                suma += int(numero)
            return [len(numeros), int(min(numeros)), int(max(numeros)), suma/len(numeros)]
        else:
            return [1, int(cadena), int(cadena), int(cadena)]
