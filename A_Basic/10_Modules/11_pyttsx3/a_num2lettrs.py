"""
Purpose: digits to alphabets 

786 -> SEVEN EIGHT SIX

0-9
"""

number_to_alphabets = {
    0: 'ZERO',
    1: 'ONE',
    2: 'TWO',
    3: 'THREE',
    4: 'FOUR',
    5: 'FIVE',
    6: 'SIX',
    7: 'SEVEN',
    8: 'EIGHT',
    9: 'NINE'
}
'''
NOTE: 
abs(-num) = num
abs(+num) = num
'''

# recursive function implementation
def digit_to_number(num1):
    num = int(abs(num1))
    # if type(num) == float:
    #     print 'it is float.'
    #     return
    if num > 9:
        for each_num in divmod(num, 10): # /, %
            digit_to_number(each_num)
        return
    print num, number_to_alphabets.get(num)
    text_to_speech(number_to_alphabets.get(num))

try:
    import pyttsx3
except ImportError:
    import os 
    os.system('pip install pyttsx3')
    import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait() 

digit_to_number(-1.8)
digit_to_number(10)
digit_to_number(23)

digit_to_number(986857578)
