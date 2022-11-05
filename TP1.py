#TP1
#la super classe (classe mère) qui représente une arme de manière générale
class weapon:
    def __init__(self,munitions,range):
        self.munitions=munitions
        self.range=range

#Lance-missiles antisurface
class antisurface(weapon(30,40)):
    def fire_at(self,x,y,z):
        try:
            try:
                print(f"fire at {x},{y},{z}")
                self.munitions = self.munitions - 1
            except self.munitions == 0 :
                print("NoAmmunationError")
        except z != 0:
            print("OutOFRangeError")
            self.munitions = self.munitions - 1


#Lance-missiles antiair
class antiair(weapon(40,50)):
    def fire_at(self,x,y,z):
        try:
            try:
                print(f"fire at {x},{y},{z}")
                self.munitions = self.munitions - 1
            except self.munitions == 0 :
                print("NoAmmunationError")
        except z <=0 :
            print("OutOFRangeError")
            self.munitions = self.munitions - 1
#Lance-torpilles
class torpilles(weapon(20,15)):
    def fire_at(self,x,y,z):
        try:
            try:
                print(f"fire at {x},{y},{z}")
                self.munitions = self.munitions - 1
            except self.munitions == 0 :
                print("NoAmmunationError")
        except z >0 :
            print("OutOFRangeError")
            self.munitions = self.munitions - 1
