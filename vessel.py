from weapon import *
class DestroyedError(Exception):

    def __init__(self,max_hits, message="lle vaiseaux est detruit "):
        self.max_hits= max_hits
        self.message = message
        super().__init__(self.message)
class OutOfRangeErrorr(Exception):

    def __init__(self,z, message="le vaiseaux ne pas atteint l'ennemi "):
        self.z = z
        self.message = message
        super().__init__(self.message)   


import numpy as np             
class Vessel():
    def __init__(self,coordinates:tuple, max_hits:int, weapon:Weapon):
        
        
        self.coordinates=coordinates
        self.max_hits=max_hits
        self.weapon = weapon
        
        
    def go_to(self,a,b,c):
        self.coordinates=(a,b,c)
        
    def get_coordinates(self):
        return self.coordinates
    def fire_at(self,e,f,g):
        self.fire_at=self.weapon().fire_at(e,f,g)
        if (np.sqrt((e- self.coordinates[0])**2+(f-self.coordinates[1])**2+(g-self.coordinates[2])**2)>self.fire_at.range):
            raise OutOfRangeErrorr(self.coordinates[2])
        if self.max_hits==0:
            raise DestroyedError(self.max_hits)    
    