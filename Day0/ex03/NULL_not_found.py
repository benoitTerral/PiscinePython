def NULL_not_found(object: any) -> int:
    if (type(object) == float and object != object):
        print("Cheese: nan <class 'float'>$")
        return 0
    elif (object is None):
        print("Nothing: None <class 'NoneType'>$")
    elif(type(object) == str and object == ''):
        print("Empty: <class 'bool'>")
    elif (type(object) == int and object == 0):
        print("Zero: 0 <class 'int'>$")
    elif(type(object) == bool and object == 0):
        print("Fake: False <class 'bool'>")
    else:
        print("Type not found")
        return 1
    return 0