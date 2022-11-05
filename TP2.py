#TP1
#la super classe (classe mère) qui représente une arme de manière générale
class weapon:
    def __init__(self,munitions:int,range:int):
        self.munitions=munitions
        self.range=range

#Lance-missiles antisurface
class antisurface(weapon(30,40)):
    def fire_at(self,x:int,y:int,z:int):
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
    def fire_at(self,x:int,y:int,z:int):
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
    def fire_at(self,x:int,y:int,z:int):
        try:
            try:
                print(f"fire at {x},{y},{z}")
                self.munitions = self.munitions - 1
            except self.munitions == 0 :
                print("NoAmmunationError")
        except z >0 :
            print("OutOFRangeError")
            self.munitions = self.munitions - 1



#TP2
#la super classe (classe mère) qui représente un vaisseau de manière générale
class vessel:
    def __init__(self,coordinates:tuple,max_hits:int,weapon:weapon):
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

    def fire_at(self,x:int,y:int,z:int):
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

    def fire_at(self,x:int,y:int,z:int):
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

    def fire_at(self,x:int,y:int,z:int):
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

    def fire_at(self,x:int,y:int,z:int):
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

    def fire_at(self,x:int,y:int,z:int):
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
    def __init__(self,X:float,Y:float,Z:int):
        self.X=X
        self.Y=Y
        self.Z=Z
        self.vessel=[]

    def add_vessel(self,v:vessel,x,y,z):
        if len(self.vessel)==0:
            self.vessel.append(v)
        else:
            sommmehits=self.vessel[0].max_hits
            for i in self.vessel:
                if (x, y, z) == i.get_coordinates:
                    print("PositionError")
                else:
                    sommmehits += i.max_hits
                    if sommmehits <= 22:
                        self.vessel.append(v)
                    else:
                        print("HitsError")




    def receive(self,x,y,z):
        for i in self.vessel:
            try :
                if i.get_coordinates()[0] == x and i.get_coordinates()[1] == y and i.get_coordinates()[2] == z:
                    return True
                else:
                    return False
            except i.get_coordinates() is None:
                print("PositionError")






