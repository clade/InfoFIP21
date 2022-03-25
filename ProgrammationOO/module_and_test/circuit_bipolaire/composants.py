import math

from .base import CircuitElementaire

class Resistance(CircuitElementaire):
    def impedance(self, freq):
        return self.val

class Condensateur(CircuitElementaire):
    def impedance(self, freq):
        return 1/(2*self.val*math.pi*freq*1J)
    
class Inductance(CircuitElementaire):
    def impedance(self, freq):
        return (2*self.val*math.pi*freq*1J)
