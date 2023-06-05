import inspect

# print(dir(inspect))

for each in inspect.stack():
    print(each)


"""
FrameInfo(
    frame=<frame at 0x0000019EDDAB0CA0,
    file 'C:\\Users\\Amma\\Downloads\\PythonForDataEngineeringApril2023\\14_Code_Quality\\01_Code_Analyses\\inspecting_code.py',
    line 6,
    code <module>>,
    filename='C:\\Users\\Amma\\Downloads\\PythonForDataEngineeringApril2023\\14_Code_Quality\\01_Code_Analyses\\inspecting_code.py', lineno=5, function='<module>', code_context=['for each in inspect.stack():\n'], index=0, positions=Positions(lineno=5, end_lineno=5, col_offset=12, end_col_offset=27))


"""
print(__file__)


c = inspect.currentframe()
print(c.f_lineno)
print(c.f_lineno)


# ---------------
def hello():
    print(dir(inspect.stack()[0]))


hello()


# ----------------------
def hello():
    previous_frame = inspect.currentframe().f_back
    (filename, line_number, function_name, lines, index) = inspect.getframeinfo(
        previous_frame
    )
    return (filename, line_number, function_name, lines, index)


print(hello())
