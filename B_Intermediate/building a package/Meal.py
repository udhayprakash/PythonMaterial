"""
Module for making meals in Python.

Import this module and then call
makeBreakfast(), makeDinner() or makeLunch().

"""


__all__ = ['Meal','AngryChefException', 'makeBreakfast', 
    'makeLunch', 'makeDinner', 'Breakfast', 'Lunch', 'Dinner']


# Helper functions.

def makeBreakfast():
    ''' Creates a Breakfast object.'''
    return Breakfast()
    
def makeLunch():
    ''' Creates a Breakfast object.'''
    return Lunch()

def makeDinner():
    ''' Creates a Breakfast object.'''
    return Dinner()
    
# Exception classes.

class SensitiveArtistException(Exception): 
    '''Exception raised by an overly-sensitive artist.
    
    Base class for artistic types.'''
    pass


class AngryChefException(SensitiveArtistException): 
    '''Exception that indicates the chef is unhappy.'''
    pass

    
    
    
class Meal:
    '''Holds the food and drink used in a meal.
    In true object-oriented tradition, this class
    includes setter methods for the food and drink.
    
    Call printIt to pretty-print the values.
    '''

    def __init__(self, food='omelet', drink='coffee'):
        '''Initialize to default values.'''
        self.name = 'generic meal'
        self.food = food
        self.drink = drink
    
    def printIt(self, prefix=''):
        '''Print the data nicely.'''
        print prefix,'A fine',self.name,'with',self.food,'and',self.drink
          
    # Setter for the food.
    def setFood(self, food='omelet'):
        self.food = food
    
    # Setter for the drink.    
    def setDrink(self, drink='coffee'):
        self.drink = drink
        
    # Setter for the name.
    def setName(self, name=''):
        self.name = name
        

class Breakfast(Meal):
    '''Holds the food and drink for breakfast.'''
        
    def __init__(self):
        '''Initialize with an omelet and coffee.'''
        Meal.__init__(self, 'omelet', 'coffee')
        self.setName('breakfast')
        
class Lunch(Meal):
    '''Holds the food and drink for lunch.'''
        
    def __init__(self):
        '''Initialize with a sandwich and a gin and tonic.'''
        Meal.__init__(self, 'sandwich', 'gin and tonic')
        self.setName('midday meal')

    # Override setFood().
    def setFood(self, food='sandwich'):
        if food != 'sandwich' and food != 'omelet':
            raise AngryChefException
        Meal.setFood(self, food)
        
class Dinner(Meal):
    '''Holds the food and drink for dinner.'''
        
    def __init__(self):
        '''Initialize with steak and merlot.'''
        Meal.__init__(self, 'steak', 'merlot')
        self.setName('dinner')

    def printIt(self, prefix=''):
        '''Print even more nicely.'''
        print prefix,'A gourmet',self.name,'with',self.food,'and',self.drink       
 
        
def test():
    '''Test function.'''
    
    print 'Module meal test.'
    
    # Generic no arguments.
    print 'Testing Meal class.'
    m = Meal()
    
    m.printIt("\t")
    
    
    m = Meal('green eggs and ham', 'tea')
    m.printIt("\t")
    
    # Test breakfast
    print 'Testing Breakfast class.'
    b = Breakfast()
    b.printIt("\t")
    
    b.setName('breaking of the fast')
    b.printIt("\t")
    
    
    # Test dinner
    print 'Testing Dinner class.'
    d = Dinner()
    d.printIt("\t")
    
    
    # Test lunch
    print 'Testing Lunch class.'
    l = Lunch()
    l.printIt("\t")
    
    print 'Calling Lunch.setFood().'
    try:
        l.setFood('hotdog')
    except AngryChefException:
        print "\t",'The chef is angry. Pick an omelet.'

# Run test if this module is run as a program.        
if __name__ == '__main__':
    test()
