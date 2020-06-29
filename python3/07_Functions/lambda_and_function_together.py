def wish(message):
    return lambda name: message.upper() + name

greet = wish('Happy Birthday')

print(greet('Joe'))