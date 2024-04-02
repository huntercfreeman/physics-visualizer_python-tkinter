class Store:
    def __init__(self):
        self.state_map = {}

__store: Store = Store()

def Register(obj):

    key = fullname(obj)

    if key in __store.state_map:
        raise Exception("Duplicate key exception")
    else:
        __store.state_map[key] = obj

def Get(obj) -> any:
    key = fullname(obj)
    return __store.state_map[key]

def fullname(o):
    """Goal of this function is to have a unique identifier for a type.
    https://stackoverflow.com/questions/2020014/get-fully-qualified-class-name-of-an-object-in-python"""

    # I sometimes find usage of a module such as 'DialogServiceModule' will
    # have a different __module__ depending on how I access it(?)
    return o.__class__.__name__

    # module = o.__class__.__module__
    # if module is None or module == str.__class__.__module__:
    #     return o.__class__.__name__
    # return module + '.' + o.__class__.__name__