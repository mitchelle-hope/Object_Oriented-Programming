class Student:
    school="AkiraChix"
    def __init__(self,name,age,country):
        self.name=name
        self.age=age
        self.coutry=country
    def greet(self):
        return f"hello{