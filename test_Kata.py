from unittest import TestCase
import Kata

class TestArreglos(TestCase):
    def test_get_arreglos(self):
        self.assertEqual(Kata.Arreglos.GetArreglos(""), [], "Cadena vacía")

    def test_get_arreglo_con_un_numero(self):
        self.assertEqual(Kata.Arreglos.GetArreglos("1"), [1], "Arreglo con la cantidad de números")

    def test_get_arreglo_con_dos_numeros(self):
        self.assertEqual(Kata.Arreglos.GetArreglos("1,2"), [2], "Arreglo con  2 números")
