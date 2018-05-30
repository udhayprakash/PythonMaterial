class Animal:
    def __init__(self,name):
        self.name = name
 
    def walk(self):
        print(self.name + ' walks.')
 
duck = Animal('Duck')
duck.walk()
 
rhino = Animal('African Rhino')
rhino.walk()