class Store:
    def __init__(self):
        self.state_map = {}

__store: Store = Store()

def Register(key, value):
    if key in __store.state_map:
        raise Exception("Duplicate key exception")
    else:
        __store.state_map[key] = value

def Get(key) -> any:
    return __store.state_map[key]



def fullname(o):
    """Goal of this function is to have a unique identifier for a type.
    https://stackoverflow.com/questions/2020014/get-fully-qualified-class-name-of-an-object-in-python"""
    module = o.__class__.__module__
    if module is None or module == str.__class__.__module__:
        return o.__class__.__name__
    return module + '.' + o.__class__.__name__