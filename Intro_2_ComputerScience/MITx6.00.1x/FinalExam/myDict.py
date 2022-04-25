class myDict(object):
    """ Implements a dictionary without using a dictionary """
    def __init__(self):
        """ initialization of your representation """
        self._extra = {}
    
    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        self.__dict__[k] = v
        
    def getval(self, k):
        """ k, immutable object  """
        return self.__dict__[k]
        
    def delete(self, k):
        """ k, immutable object """   
        del self.__dict__[k]
