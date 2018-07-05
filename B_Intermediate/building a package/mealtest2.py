import Meal

# In the book, "meal" should be capitalized

print 'Making a Breakfast'
breakfast = Meal.makeBreakfast()

breakfast.printIt("\t")

print 'Making a Lunch'
lunch = Meal.makeLunch()

try:
    lunch.setFood('pancakes')
except Meal.AngryChefException:
    print "\t",'Cannot make a lunch of pancakes.'
    print "\t",'The chef is angry. Pick an omelet.'
