# class  - blue print of an object
# object is a instance of class which can contain its own attributes and behaviour

class Birds:

    # attribute
    name = ""
    age = 0

    def __init__(self, bird_name, bird_age):
        self.name = bird_name
        self.age = bird_age

    # behaviour / methods
    def fly(self):
        print(self.name,"Hey I can fly!")

bird1 = Birds("parrot",2)

print(bird1.name)
print(bird1.age)
bird1.fly()

bird2 = Birds("eagle","5")

print(bird2.name)
print(bird2.age)
bird2.fly()

#############################################


class Animal:

    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("Hey I can eat")
    
    def sleep(self):
        print("Hey I can sleep")

cat = Animal("cat",5)
cat.eat()
cat.sleep()

##############################

class Vehicle:

    color = "red"
    tyres = ""
    max_speed = ""
    seat_capacity = 0

    def pressBreak(self):
        print("Break is controlled")

    def pressHorn(self):
        print("Horn sounded")

class Vehicle1:

    color = "red"
    tyres = ""
    max_speed = ""
    seat_capacity = 0

    def pressBreak(self):
        print("ABS Break is controlled")

class Car(Vehicle):
    company = ""
    model = ""

    def switchACOn(self):
        print("Switched on AC")

class Car2(Vehicle1, Vehicle):

    company = "testcar"
    model="testmodel"

xuv = Car()
xuv.company = "Mahendra"
xuv.model="xuv700"
xuv.color = "blue"
xuv.tyres = 4
xuv.max_speed = "200kmph"
xuv.seat_capacity = 7    

print(xuv.color, xuv.company, xuv.model, xuv.max_speed, xuv.seat_capacity)
xuv.switchACOn()
xuv.pressBreak()
xuv.pressHorn()

print(dir(xuv))
print(vars(xuv))

dummycar = Car2()
dummycar.pressBreak()


#########

#__init__
#__add__,__sub__, __mul__, __eq__, __le__
#__str__
#__len__
#__call__

class Add2num:

    a=0
    b=0

    def __init__(self, x, y):
        self.a=x
        self.b=y

    def __add__(self, secondObject):
        sumofa=(self.a+secondObject.a)*35
        sumofb=(self.b+secondObject.b)*25
        return [sumofa,sumofb]
        

firstSetofNo = Add2num(5,6)
secondSetofNo = Add2num(1,2)


print(firstSetofNo + secondSetofNo)
