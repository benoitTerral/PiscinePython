def all_thing_is_obj(object: any) -> int:
    match object:
        case list():
            print('List : %s' % type(object))
        case tuple():
            print('Tuple : %s' % type(object))
        case set():
            print('Set : %s' % type(object))
        case dict():
            print('Dict : %s' % type(object))
        case str():
            print('%s is in the kitchen : %s' % (object, type(object)))
        case _:
            print('Type not found')
    return 42