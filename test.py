class Expression(object):
        def __init__(self, terms=[]):
            self.terms=list(terms)
        def add(self, *others):
            result=Expression(self.terms)
            for another in others:
                if type(another)==Metre and type(self)== Metre:
                    result = another.coefficient + self.coefficient
                elif type(another)==Kilometre and type(self)== Kilometre:
                    result = another.coefficient + self.coefficient
                elif type(another)==Kilometre and type(self)== Metre:
                    result = 0.001*another.coefficient + self.coefficient
                elif type(another)==Metre and type(self)== Kilometre:
                    result = another.coefficient + 0.001*self.coefficient					
                else: # raise error? Sopra pero non lo conosce il coefficient. metre.coefficient?
                    #result = another.coefficient + 0.001*self.coefficient
            return result
        def multiply(self, another):
            # Distributive law left as exercise
            pass
			# Definisco anche eq qua? come?
        def __add__(self, other):
            return self.add(other)
		def __radd__(self, other):
            return self.__add__(other)