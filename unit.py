"""
I have to create class to implement operations consistently with the units
"""
# we define a class that takes the unit of measure (e.g. length), the amount (e.g. 5) and the scale (e.g. km)
class Measure(object):
        def __init__(self,amount,unit,scale=1):
         self.amount=amount
         self.unit=unit
         self.scale=scale
		def conversion():
        def add(self, others):
             if self.unit==others.unit:
                 if self.scale==others.scale:
                     return self.amount+others.amount
                 else:
                     return others.amount+self.conversion(others.scale)     
             else:
                 raise ValueError('Incompatibleunits') 				 