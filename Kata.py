class Arreglos:
    def GetArreglos(cadena):
        if cadena == "":
            return [None, None, None, None]
        elif "," in cadena:
            numeros = cadena.split(",")
            suma = 0
            for numero in numeros:
                suma += int(numero)
            return [len(numeros), int(min(numeros)), int(max(numeros)), suma/len(numeros)]
        else:
            return [1, int(cadena), int(cadena), int(cadena)]
