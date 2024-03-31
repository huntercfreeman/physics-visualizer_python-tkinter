class EventModel():
    """Goal of this class: allow tkinter widgets to subscribe to state changes in
    a service. On state change, the tkinter widget could then choose to re-render or etc...
    https://stackoverflow.com/questions/70982565/how-do-i-make-an-event-listener-with-decorators-in-python"""
    def __init__(self):
        # Initialise a list of listeners
        self.__listeners = []

    # Add and remove functions from the list of listeners.
    def addListener(self,func):
        if func in self.__listeners: return
        self.__listeners.append(func)
    
    def removeListener(self,func):
        if func not in self.__listeners: return
        self.__listeners.remove(func)
    
    # Trigger events.
    def trigger(self, args = None):
        # Run all the functions that are saved.
        if args is None:
            args = []
        for func in self.__listeners: func() #func(*args)

