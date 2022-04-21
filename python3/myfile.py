# def f():
#     for i in range(3):
#         yield i


# # print(f())
# print(list(f()))
# # print([n for n in iter(f)])
# # print(list(f))

# res = []
# g = f()
# while True:
#     try:
#         res.append(next(g))
#     except StopIteration:
#         break
# print(res)


# A semaphore manages an internal counter which is decremented by each acquire() call and incremented by each release() call.

# text = """
# hello      hello
# goodbye
# bye    bye bye
# hello goodbye
# """
# pat = re.compile(r'$.*\s*\0*^', re.MULTILINE)
# result = pat.sub('', text)
# print(result)


class A:
    __slots__ = ["x", "y", "z"]
    w = 1


class B(A):
    __slots__ = ["w", "z"]
    pass


a = A()
b = B()
