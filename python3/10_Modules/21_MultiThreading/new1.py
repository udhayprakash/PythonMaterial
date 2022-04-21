import threading

def display():
    for i in range(10):
        print('child Thread', i)

# creating a thread
t = threading.Thread(target=display)

t.start()

for i in range(10):
    print('Main Thread', i)

