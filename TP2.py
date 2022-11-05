#TP2
#la super classe (classe mère) qui représente un vaisseau de manière générale
class vessel:
    def __init__(self,coordinates,max_hits,weapon):
        self.coordinates=coordinates
        self.max_hits=max_hits
        self.weapon=weapon

    def get_coordinates(self):
        if len(self.coordinates)==3:
            return self.coordinates
        else:
            return None

class Cruiser(vessel({},6,antiair)):
    def go_to(self,x,y,z):
        if self.max_hits ==0:
            print("DestroyedError")
        else:
            try:
                print(f"vessel moved to {x},{y},{z}")
            except z != 0:
                print("MoveError")
    def fire_at(self):
        if self.max_hits ==0:
            print("DestroyedError")
        else:
            if range.antiair() < (x ** 2 + y ** 2 + z ** 2) ** 0.5:
                print("OutOfRangeError")
                self.munitions = self.munitions - 1
            else:
                antiair.fire_at(x,y,z)

class Submarine(vessel({},2,torpilles)):
    def go_to(self,x,y,z):
        if self.max_hits ==0:
            print("DestroyedError")
        else:
            try:
                print(f"vessel moved to {x},{y},{z}")
            except z != 0 and z != -1:
                print("MoveError")
    def fire_at(self):
        if self.max_hits == 0:
            print("DestroyedError")
        else:
            if range.antiair() < (x ** 2 + y ** 2 + z ** 2) ** 0.5:
                print("OutOfRangeError")
                self.munitions = self.munitions - 1
            else:
                torpilles.fire_at(x, y, z)

class Fregate(vessel({},5,antisurface)):
    def go_to(self,x,y,z):
        if self.max_hits == 0:
            print("DestroyedError")
        else:
            try:
                print(f"vessel moved to {x},{y},{z}")
            except z != 0:
                print("MoveError")
    def fire_at(self):
        if self.max_hits == 0:
            print("DestroyedError")
        else:
            if range.antiair() < (x ** 2 + y ** 2 + z ** 2) ** 0.5:
                print("OutOfRangeError")
                self.munitions = self.munitions - 1
            else:
                antisurface.fire_at(x,y,z)

class Destroyer(vessel({},4,torpilles)):
    def go_to(self,x,y,z):
        if self.max_hits == 0:
            print("DestroyedError")
        else:
            try:
                print(f"vessel moved to {x},{y},{z}")
            except z != 0:
                print("MoveError")
    def fire_at(self):
        if self.max_hits == 0:
            print("DestroyedError")
        else:
            if range.antiair() < (x ** 2 + y ** 2 + z ** 2) ** 0.5:
                print("OutOfRangeError")
                self.munitions = self.munitions - 1
            else:
                torpilles.fire_at(x,y,z)

class Aircraft(vessel({},1,antisurface)):
    def go_to(self,x,y,z):
        if self.max_hits == 0:
            print("DestroyedError")
        else:
            try:
                print(f"vessel moved to {x},{y},{z}")
            except z != 1:
                print("MoveError")
    def fire_at(self):
        if self.max_hits == 0:
            print("DestroyedError")
        else:
            if range.antiair() < (x ** 2 + y ** 2 + z ** 2) ** 0.5:
                print("OutOfRangeError")
                self.munitions = self.munitions - 1
            else:
                antisurface.fire_at(x,y,z)


#Le champ de la bataille
class espace:
    def __init__(self,X,Y,Z):
        self.X=X
        self.Y=Y
        self.Z=Z
        self.vessel=[]

    def add_vessel(self,v:vessel):
        try :
            if len(self.vessel)==0:
                self.vessel.append(v)    
            else:
                sommehits=self.vessel[0].max_hits
                for i in self.vessel:
                    if (x, y, z) == i.get_coordinates:
                        print("PositionError")
                    else:
                        sommehits += i.max_hits
                        if sommehits <= 22:
                            self.vessel.append(vessel)
                        else:
                            print("HitsError")                                  
         except type(vessel) not in [Aircraft,Destroyer,Fregate,Submarine,Cruiser]: 
            print("This vessel is not available")
            
        
    def receive(self,x,y,z):
        if (x,y,z)==(self.X,self.Y,self.Z) :
            return True
        else :
            return False
