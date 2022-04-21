import inspect

# for each in inspect.stack():
#     print(each)

# FrameInfo(

#      filename='D:\\MEGAsync\\Python-related\\PythonMaterial\\python3\\10_Modules\\21_MultiThreading\\old\\new3.py',
#      lineno=3,
#      function='<module>',
#      code_context=['for each in inspect.stack():\n'],
#      index=0)


import inspect

print(__file__)
c = inspect.currentframe()
print(c.f_lineno)
print(c.f_lineno)


def hello():
    print(dir(inspect.stack()[0]))


hello()


def hello():
    previous_frame = inspect.currentframe().f_back
    (filename, line_number,
     function_name, lines, index) = inspect.getframeinfo(previous_frame)
    return (filename, line_number, function_name, lines, index)


print(hello())
