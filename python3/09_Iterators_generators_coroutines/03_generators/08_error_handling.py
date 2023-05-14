def my_gen():
    try:
        yield "value"
    except ValueError:
        yield "Handling Exception"
    finally:
        print("cleaning up")


x = my_gen()

next(x)

e = ValueError("some error")

print(x.throw(e))  # "Handling Exception"
print(x.close())  # Cleaning Up
