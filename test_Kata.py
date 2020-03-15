from unittest import TestCase
import Kata

class TestArreglos(TestCase):
    def test_get_arreglos(self):
        self.assertEqual(Kata.Arreglos.GetArreglos(""), [], "Cadena vacía")
