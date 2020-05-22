class Person:
    def __init__(self):
        self.name = []

    def set_name(self, user_name):
        self.name.append(user_name)
        return len(self.name) - 1

    def get_name(self, user_id):
        if user_id >= len(self.name):
            return 'There is no such user'
        else:
            return self.name[user_id]


if __name__ == '__main__':
    person = Person()
    print('User Udhay has been added with id ' + str(person.set_name('Udhay')))
    print('User associated with id 0 is ' + str(person.get_name(0)))

    basheer_id = person.set_name('Basheer')
    print(f'{basheer_id =}')
    print(person.get_name(basheer_id))

    syed_id = person.set_name('syed')
    print(f'{syed_id =}')
    print(person.get_name(syed_id))

    print(vars(person))