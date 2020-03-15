from unittest import TestCase
import Kata

class TestArreglos(TestCase):
    def test_get_arreglos(self):
        self.assertEqual(Kata.Arreglos.GetArreglos(""), [None, None, None], "Cadena vacía")

    def test_get_arreglo_con_un_numero(self):
        self.assertEqual(Kata.Arreglos.GetArreglos("1"), [1, 1], "Arreglo con la cantidad de números")

    def test_get_arreglo_con_dos_numeros(self):
        self.assertEqual(Kata.Arreglos.GetArreglos("1,2"), [2, 1], "Arreglo con  2 números")

    def test_get_arreglo_con_muchos_numeros(self):
        self.assertEqual(Kata.Arreglos.GetArreglos("1,2,3,4,5,6,7,8"), [8, 1], "Arreglo con 8 números")
