class Expression(object):
        def __init__(self, terms=[]):
            self.terms=list(terms)
        def add(self, *others):
            result=Expression(self.terms)
            for another in others:
                if type(another)==Term:
                    result.terms.append(another)
                else:
                    result.terms+=another.terms
            return result
        def multiply(self, another):
            # Distributive law left as exercise
            pass
        def __add__(self, other):
            return self.add(other)
		def __radd__(self, other):
            return self.__add__(other)