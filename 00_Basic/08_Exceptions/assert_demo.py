
def first_assert_demo():
    # Demonstrate the use of assert()
    large = 1000
    string = "This is a string"
    float = 1.0
    broken_int = "This should have been an int"
    
    assert large > 500
    assert type(string) == type("")
    assert type(float) != type(1)
    assert type(broken_int) == type(4)

def second_assert_demo():
    # Demonstrate the use of assert()
    large = 1000
    string = "This is a string"
    float = 1.0
    broken_int = "This should have been an int"
    
    assert large > 500
    assert type(string) == type("")
    assert type(float) != type(1)

    try: 
        assert type(broken_int) == type(4), "broken_int is broken"
    except AssertionError, message:
        print "Handle the error here.  The message is: %s" % message

print 'From the interpreter call first_assert_demo() and second_assert_demo()'
