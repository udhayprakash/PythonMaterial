class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(self.name + ' walks.')

duck = Animal('Duck') 
# Animal.__init__(duck, 'Duck')
print(vars(duck))
print(f'duck.name:{duck.name}')
duck.walk()


rhino = Animal('African Rhino')
rhino.walk()