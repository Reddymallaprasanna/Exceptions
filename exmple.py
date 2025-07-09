#code is to initiate t process of exception
try:
    raise Exception('prasana','It')
except Exception as errorobj:
    print(type(errorobj))
    print(errorobj.args)
    arg1,arg2=errorobj.args
    print("1st argument",arg1)
    print("2nd argument",arg2)