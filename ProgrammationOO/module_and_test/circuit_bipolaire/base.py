import sympy

class CircuitBipolaire(object):
    def admittance(self, freq):
        return 1/self.impedance(freq)
    
    def __add__(self, other):
        return Serie(self, other)

    def __or__(self, other):
        return Parallel(self, other)
        
    def impdance(self, freq):
        """ Calcule l'impédance du circuit
        
        Argument : 
            freq : fréquence n Hz
            
        """
        pass
    
class CircuitElementaire(CircuitBipolaire):
    def __init__(self, val):
        self.val = val
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.val})' 
    
    def __str__(self):
        initiale = self.__class__.__name__[0]
        return f'{initiale}({self.val})' 
    
class CircuitCompose(CircuitBipolaire):
    def __init__(self, circ1, circ2):
        self.circ1 = circ1
        self.circ2 = circ2
        
    def __repr__(self):
        return f'{self.__class__.__name__}({self.circ1!r}, {self.circ2!r})' 

class Parallel(CircuitCompose):
    def impedance(self, freq):
        Z1, Z2 = self.circ1.impedance(freq), self.circ2.impedance(freq)
        return Z1*Z2/(Z1+Z2)
        
    def __str__(self):
        return f'({self.circ1!s} | {self.circ2!s})'

class Serie(CircuitCompose):
    def impedance(self, freq):
        return self.circ1.impedance(freq) + self.circ2.impedance(freq)

    def __str__(self):
        return f'({self.circ1!s} + {self.circ2!s})'
 

#R1 = Resistance(10)
#C1 = Condensateur(10E-6)
#print(R1) # R(10)
#Parallel(R1, C1).impedance(1000)
#R1|C1
