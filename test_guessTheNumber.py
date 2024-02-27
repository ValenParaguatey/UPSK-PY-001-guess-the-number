import unittest
from main import generateSecretNumber, resolveNumber, validateInput

class TestsJuegoNumeroSecreto(unittest.TestCase):

    def test_generateSecretNumber(self):
        numero = generateSecretNumber()
        self.assertTrue(1 <= numero <= 100)

    def test_mayor(self):
        # Caso cuando la entrada del usuario es mayor que el número correcto
        numero_correcto = 50
        entrada_usuario = 70
        resultado = resolveNumber(numero_correcto, entrada_usuario)
        self.assertEqual(resultado, "mayor")
    
    def test_menor(self):
        # Caso cuando la entrada del usuario es menor que el número correcto
        numero_correcto = 50
        entrada_usuario = 30
        resultado = resolveNumber(numero_correcto, entrada_usuario)
        self.assertEqual(resultado, "menor")
    
    def test_igual(self):
        # Caso cuando la entrada del usuario es igual al número correcto
        numero_correcto = 50
        entrada_usuario = 50
        resultado = resolveNumber(numero_correcto, entrada_usuario)
        self.assertTrue(resultado)

class TestValidateInput(unittest.TestCase):
    def test_cadena_vacia(self):
        # Prueba cuando se pasa una cadena vacía
        guess_number = ''
        resultado = validateInput(guess_number)
        self.assertFalse(resultado)

    def test_cadena_no_numerica(self):
        # Prueba cuando se pasa una cadena que no es numérica
        guess_number = 'abc'
        resultado = validateInput(guess_number)
        self.assertFalse(resultado)

    def test_numero_entero_valido(self):
        # Prueba cuando se pasa un número entero válido
        guess_number = '123'
        resultado = validateInput(guess_number)
        self.assertTrue(resultado)

        


if __name__ == '__main__':
    unittest.main()



