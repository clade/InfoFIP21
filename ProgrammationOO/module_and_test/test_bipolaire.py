import unittest

from circuit_bipolaire import *
from circuit_bipolaire.base import Serie
from math import pi

class TestCircuitBipolaire(unittest.TestCase):
    def test_circuit_elementaire(self):
        R1 = Resistance(10)
        C1 = Condensateur(1)
        self.assertEqual(R1.impedance(10), 10)
        self.assertEqual(C1.impedance(10), 1/(2j*pi*10*1))

    def test_somme(self):
        R1 = Resistance(10)
        C1 = Condensateur(1)
        self.assertTrue(isinstance(C1 + R1, Serie))                 
      
    def test_impedance(self):
        R1 = Resistance(10)
        C1 = Condensateur(1)
        circuit = (R1 + C1)|C1
        z = circuit.impedance(10)
        
#assert R1.impedance(10)==10
#assert C1.impedance(10)==1/(2j*pi*10*1)

#assert isinstance(C1 + R1, Serie)

if __name__ == '__main__':
    unittest.main()