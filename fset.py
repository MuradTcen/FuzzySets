
class FSet:
    
    def __init__(self,x=[],mu_x=[]):
        self.mu_x=mu_x[:]
        self.x=x[]:
        
    
    def __add__(self,other):
        x=self.x+other.x
        mu_x=self.mu_x+other.mu_x
        return FSet{x,mu_x}
        
        
    def __mul__(self)
