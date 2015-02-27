"""
I have to create class to implement operations consistently with the units
"""
# we define a class that takes  the value (e.g. 5) and the unit (e.g. km). It then creates the measure (length or time).
class Measure(object):
        def __init__(self,value,unit):
         self.value=value
         self.unit=unit
		 if unit=='km' or unit=='m':
		    return self.measure='length'
		 if unit=='h' or unit=='s':
		    return self.measure='time'
		# this function convert the current unit into the one indicated by unitconvertion.	
		def conversion(self, unitconversion):
         if self.unit=='m' and unitconversion=='km':
             return 0.001*self.value
         elif self.unit=='km' and unitconversion=='m':
             return 1000*self.value
         elif self.unit=='h' and unitconversion=='s':
             return 60*self.value
         elif self.unit=='s' and unitconversion=='h':
             return 0.016666666666666666666666666666667*self.value
		# this function add the values of self and others if they are the same unit or if they are the same measure.		 
        def add(self, others):
             if self.measure==others.measure:
                 if self.unit==others.unit:
                     return self.value+others.value
                 else:
                     return others.value+self.conversion(others.unit)     
             else:
                 raise ValueError('Units not summable') 				 