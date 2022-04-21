# We subclass from object to get a class.
class Human(object):
    # A class attribute. It is shared by all instances of this class
    species = 'H. sapiens'

    # Basic initializer, this is called when this class is instantiated.
    # Note that the double leading and trailing underscores denote objects
    # or attributes that are used by python but that live in user-controlled
    # namespaces. You should not invent such names on your own.
    def __init__(self, name):
        # Assign the argument to the instance's name attribute
        self.name = name

        # Initialize property
        self.age = 0

    # An instance method. All methods take "self" as the first argument
    def say(self, msg):
        return '{0}: {1}'.format(self.name, msg)

    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    @classmethod
    def get_species(cls):
        return cls.species

    # A static method is called without a class or instance reference
    @staticmethod
    def grunt():
        return '*grunt*'

    # A property is just like a getter.
    # It turns the method age() into an read-only attribute
    # of the same name.
    @property
    def age(self):
        return self._age

    # This allows the property to be set
    @age.setter
    def age(self, age):
        self._age = age

    # This allows the property to be deleted
    @age.deleter
    def age(self):
        del self._age


# Instantiate a class
i = Human(name='Ian')
print i.say('hi')  # prints out "Ian: hi"

j = Human('Joel')
print j.say('hello')  # prints out "Joel: hello"

# Call our class method
i.get_species()  # => "H. sapiens"

# Change the shared attribute
Human.species = 'H. neanderthalensis'
i.get_species()  # => "H. neanderthalensis"
j.get_species()  # => "H. neanderthalensis"

# Call the static method
Human.grunt()  # => "*grunt*"

# Update the property
i.age = 42

# Get the property
i.age  # => 42

# Delete the property
del i.age
# i.age  # => raises an AttributeError
