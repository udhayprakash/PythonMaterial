def producer(sentence, next_coroutine):
    ''' 
    Producer which just split strings and 
    feed it to pattern_filter coroutine 
    '''
    tokens = sentence.split(" ")
    for token in tokens:
        next_coroutine.send(token)
    next_coroutine.close()

def pattern_filter(pattern="ing", next_coroutine=None):
    ''' 
    Search for pattern in received token  
    and if pattern got matched, send it to 
    print_token() coroutine for printing 
    '''
    print("Searching for {}".format(pattern))
    try:
        while True:
            token = (yield)
            if pattern in token:
                next_coroutine.send(token)
    except GeneratorExit:
        print('Done with filtering!!!')


def print_token():
    ''' 
    Act as a sink, simply print the 
    received tokens 
    '''
    print("I'm sink, i'll print tokens")
    try:
        while True:
            token = (yield)
            print(token)
    except GeneratorExit:
        print('Done with printing!')


if __name__ == '__main__':
    pt = print_token()
    next(pt)

    pf = pattern_filter(next_coroutine=pt)
    next(pf)

    sentence = 'Bob is running behind a fast moving car'
    producer(sentence, pf)
