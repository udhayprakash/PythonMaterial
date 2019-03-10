class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(self.name + ' walks.')


duck = Animal('Duck')  # Animal.__init__(duck, 'Duck')
duck.walk()  # Animal.walk(duck)
print dir(duck)

rhino = Animal('African Rhino')
rhino.walk()

print vars(rhino)
