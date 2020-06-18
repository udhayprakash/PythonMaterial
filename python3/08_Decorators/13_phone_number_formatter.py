
"""
            7895462130      10
            9195969878      10
            9100256236      10
            07895462130     11
            09191919191     11
            919875641230    12
            +919875641230   13
            +919593621456   13
"""
def phone_number_formatter(func):
    def wrapper(*args, **kwargs):
        pass 

    return wrapper 

def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    # l = [input() for _ in range(int(input()))]
    l = ['9195969878',
         '07895462130',
         '919875641230',
         '+919875641230',
         '09191919191',
         '9100256236',
         '+919593621456']
    sort_phone(l)

# Assignment is to complete this decorator