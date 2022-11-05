class Weapon:
    def __init__(self,ammunitions:int,range:int) -> None:
        self.ammunitions=ammunitions
        self.range=range
    def fire_at(self,x:int,y:int,z:int):
        self.x=x
        self.y=y
        self.z=z
class OutOfRangeError(Exception):

    def __init__(self,z, message="la condition en z n'est pas verifié"):
        self.z = z
        self.message = message
        super().__init__(self.message)

class NoAmmunitionError(Exception):

    def __init__(self,ammunitions, message="la munitions est egale à 0"):
        self.ammunitions= ammunitions
        self.message = message
        super().__init__(self.message)



class Lance_missiles_antisurface(Weapon):
    def __init__(self):
        super().__init__(40,30)
        
    def fire_at(self,x:int,y:int,z:int):
        self.x=x
        self.y=y
        self.z=z
        if self.ammunitions==0:
            raise NoAmmunitionError(self.ammunitions)
        if  self.z!=0:
        
            raise OutOfRangeError(z)
            self.ammunitions=self.ammunitions-1
            
            
class Lance_missiles_antiair(Weapon):
    def __init__(self):
        super().__init__(40,30)


        
    def fire_at(self,x:int,y:int,z:int):
        self.x=x
        self.y=y
        self.z=z
        if self.ammunitions==0:
            raise NoAmmunitionError(self.ammunitions)
        
        if self.z<=0:
            raise OutOfRangeError(z) 
            self.ammunitions=self.ammunitions-1
            
class Lance_torpilles(Weapon):
    def __init__(self):
        super().__init__(15,20)
        
    def fire_at(self,x:int,y:int,z:int):
        self.x=x
        self.y=y
        self.z=z
        if self.ammunitions==0:
            raise NoAmmunitionError(self.ammunitions)
        if self.z>0:
            raise OutOfRangeError(z) 
            self.ammunitions=self.ammunitions-1
        
            