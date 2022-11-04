#TP1
#la super classe (classe mère) qui représente une arme de manière générale
class weapon:
    def __init__(self,munitions,range):
        self.munitions=munitions
        self.range=range

#Lance-missiles antisurface
class antisurface(weapon(30,40)):
    def fire_at(self,x,y,z):
        if self.munitions == 0:
            print("NoAmmunitionError")
        if z!=0:
            print("OutOfRangeError")
            self.munitions=self.munitions-1


#Lance-missiles antiair
class antiair(weapon(40,50)):
    def fire_at(self,x,y,z):
        if self.munitions == 0:
            print("NoAmmunitionError")
        if z<=0:
            print("OutOfRangeError")
            self.munitions=self.munitions-1
#Lance-torpilles
class torpilles(weapon(20,15)):
    def fire_at(self,x,y,z):
        if self.munitions == 0:
            print("NoAmmunitionError")
        if z>0:
            print("OutOfRangeError")
            self.munitions=self.munitions-1
