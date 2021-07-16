from unittest import TestCase

from oo.motor import Motor

class CarroTestCase(TestCase):

    def test_velocidade_inicial(self):         #unitest TEM que comecar com o prefixo TEST, ou TESTE
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def teste_acelerar(self):                  #unitest TEM que comecar com o prefixo TEST, ou TESTE
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)


