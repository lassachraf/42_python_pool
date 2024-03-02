def is_float(obj: any) -> bool:
    return isinstance(obj, float) and not (obj.is_integer())

def NULL_not_found(obj: any) -> int:
    if obj is None:
        print("Nothing: None", type(obj))
        return 0
    elif is_float(obj):
        print("Cheese: nan", type(obj))
        return 0
    elif obj == False and isinstance(obj, bool):
        print("Fake:", obj, type(obj))
        return 0
    elif obj == 0:
        print("Zero: 0", type(obj))
        return 0
    elif obj == '':
        print("Empty:", type(obj))
        return 0
    else:
        print("Type not Found")
        return 1
