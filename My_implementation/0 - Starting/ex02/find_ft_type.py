def all_thing_is_obj(obj: any) -> int:
    if isinstance(obj, list) or isinstance(obj, tuple) or isinstance(obj, set) or isinstance(obj, dict):
        print(type(obj).__name__.title(), ": " + str(type(obj)))
    elif isinstance(obj, str):
        print(obj + "is in the kitchen : " + str(type(obj)))
    else:
        print("Type not found")
    return 42
