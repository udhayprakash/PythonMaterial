import pyttsx3


def myfunc():
    engine = pyttsx3.init()
    engine.say('Sally sells seashells by the seashore.')
    engine.say('The quick brown fox jumped over the lazy dog.')
    engine.runAndWait()


if __name__ == '__main__':
    myfunc()
