from unittest import TestCase
import Kata

class TestArreglos(TestCase):
    def test_get_arreglos(self):
        self.assertEqual(Kata.Arreglos.GetArreglos(""), [None, None, None, None], "Cadena vacía")

    def test_get_arreglo_con_un_numero(self):
        self.assertEqual(Kata.Arreglos.GetArreglos("1"), [1, 1, 1], "Arreglo con la cantidad de números")

    def test_get_arreglo_con_un_numero_0(self):
        self.assertEqual(Kata.Arreglos.GetArreglos("0"), [1, 0, 0], "Arreglo con número 0")

    def test_get_arreglo_con_dos_numeros(self):
        self.assertEqual(Kata.Arreglos.GetArreglos("1,2"), [2, 1, 2], "Arreglo con 2 números")

    def test_get_arreglo_con_dos_numeros_diferentes(self):
        self.assertEqual(Kata.Arreglos.GetArreglos("66,20"), [2, 20, 66], "Arreglo con 2 números diferentes")

    def test_get_arreglo_con_muchos_numeros(self):
        self.assertEqual(Kata.Arreglos.GetArreglos("1,2,3,4,5,6,7,8"), [8, 1, 8], "Arreglo con 8 números")

    def test_get_arreglo_con_muchos_numeros_diferentes(self):
        self.assertEqual(Kata.Arreglos.GetArreglos("10,15,20,35,80"), [5, 10, 80], "Arreglo con 5 números diferentes")
