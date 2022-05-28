class Dog:
    def __init__(self,name,age,friendliness,):
        self.name=name
        self.age=age
        self.frienliness=friendliness
    def likes_chicken(self):
        return True 

class Bull(Dog):
    def __init__(self,name,age,friendliness):
       super().__init__(name,age,friendliness)
   

class Chiwawa(Dog):
    def __init__(self,name,age,friendliness):
       super().__init__(name,age,friendliness)
    

class Shepherd(Dog):
    def __init__(self,name,age,friendliness):
       super().__init__(name,age,friendliness)
   
class idgets(Dog):
    def __init__(self,name,age,friendliness):
       super().__init__(name,age,friendliness)
   
    