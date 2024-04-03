from States import StoreModule

class StatefulModel:
    """
    Usage:
        -Inherit this class
        -Define a class level data attribute as so:
            -'store_key = None'
        -Define an '__init__()' for the descendent type
            -Invoke super().__init__()
        -Register the state by using the 'StoreModule.Register(type)' function
            -This function receives the descendent of this type.
        -Get the state by using the 'StoreModule.Get(type)' function
            -This function receives the descent of this type,
                and uses the descendent's 'store_key' class level data attribute
                to retrieve the state from a 'map'
    """
    def __init__(self):
        type_fullname = StoreModule.fullname(self)

        if self.__class__.store_key != None:
            raise Exception(f"'{type_fullname}' has already been created in "
                            f"'{str(StoreModule)}'")
        else:
            self.__class__.store_key = type_fullname