"""
I have to create class to implement operations consistently with the units
"""

class Unit(object):
        def __init__(self,quantity='',unit='',coefficient=0):
         self.quantity=quantity
         self.unit=unit
         self.coefficient=coefficient
        def convert(self,conversionunit):
         if self.unit==conversionunit:
             return self.coefficient
         if self.unit=='meter' and conversionunit=='kilometer':
             return 0.001*self.coefficient
         elif self.unit=='kilometer' and conversionunit=='meter':
             return 1000*self.coefficient
         if self.unit=='second' and conversionunit=='hour':
             return 0.016666666666666666666666666666667*self.coefficient
         if self.unit=='hour' and conversionunit=='second':
             return 60*self.coefficient
         else:
             return self.coefficient
        def add(self, others):
             if self.quantity==others.quantity:
                 if self.unit==others.unit:
                     return self.coefficient+others.coefficient
                 else:
                     return others.coefficient+self.convert(others.unit)     
             else:
                 raise ValueError('Incompatibleunits')
        def add(self, *others):
            return Expression((self,)+others)
        def multiply(self, *others):
            result_data=dict(self.data)
            result_coeff=self.coefficient
        # Convert arguments to Terms first if they are
            # constants or integers
            others=map(Term,others)
            for another in others:
                for symbol, exponent in another.data.iteritems():
                    if symbol in result_data:
                        result_data[symbol]+=another.data[symbol]
                    else:
                        result_data[symbol]=another.data[symbol]
                result_coeff*=another.coefficient
            return Term(result_data,result_coeff)
		# Here we make the addition and multiplication commutative.
		def __add__(self, other):
            return self.add(other)
		def __eq__(self, other):
            return self.eq(other)		
        def __mul__(self, other):
            return self.multiply(other)
		def __rmul__(self, other):
            return self.__mul__(other)
        def __radd__(self, other):
            return self.__add__(other)
		def __req__(self, other):
            return self.__eq__(other)			