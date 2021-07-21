class Animals:
    def __init__(self,weight,height,age,food):
        self.weight = weight
        self.height = height
        self.age  = age
        self.food = food
    def grow (self ):
        print(self.weight," Kgs and ",self.height," metres")
    def reproduce(self,age):
        pass
    def eat(self,food):
        pass
class Birds(Animals):
    def fly(self,speed,altitude):
        pass
class Fish(Animals):
    def swim(self,depth):
        pass

lion = Animals(120,1.2,4,"meat")

lion.grow()