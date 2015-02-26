"""
I have to create class to implement operations consistently with the units
"""

class Term(object):
        def __init__(self, *args):
            lead=args[0]
            if type(lead)==type(self):
                # Copy constructor
                self.data=dict(lead.data)
                self.coefficient=lead.coefficient
            elif type(lead)==int:
                self.from_constant(lead)
            elif type(lead)==str:
                self.from_symbol(*args)
            elif type(lead)==dict:
                self.from_dictionary(*args)
            else:
                self.from_lists(*args)
        def from_constant(self, constant):
            self.coefficient=constant
            self.data={}
        def from_symbol(self, symbol, coefficient=1, power=1):
            self.coefficient=coefficient
            self.data={symbol:power}
        def from_dictionary(self, data, coefficient=1):
            self.data=data
            self.coefficient=coefficient
        def from_lists(self, symbols=[], powers=[], coefficient=1):
            self.coefficient=coefficient
            self.data={symbol: exponent for symbol,exponent
                    in zip(symbols, powers)}
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
			def __add__(self, other):
            return self.add(other)
        def __mul__(self, other):
            return self.multiply(other)
		def __rmul__(self, other):
            return self.__mul__(other)
        def __radd__(self, other):
            return self.__add__(other)