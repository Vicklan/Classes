class Animals:
    def __init__(self, name, weight, height, food):
        self.name = name
        self.weight = weight
        self.height = height
        self.food = food
    def getFood (self):
        return self.__food

    def setFood(self,food):
        self.__food = food

         
     
class Birds(Animals):
    def fly(self, speed):
        print(self.name,"fly at",speed,"KPH max")
 
bird1 = Birds("Eagles", 6, 0.45, "mouse")
bird1.setFood("Hare")
print(bird1.getFood())
 