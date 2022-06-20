class Viechle:
    color = "white"
    def __init__(self,name,maxspeed,mileage) :
        self.name=name
        self.maxspeed=maxspeed
        self.mileage=mileage
    def congratulate(self) :
        return f"Congratulations Mitchelle for buying a {self.color} , {self.name} that has a {self.maxspeed} of {self.mileage }" 
    def carcap(self,capacity):
        return f"your {self.color} , {self.name} has {capacity}"

