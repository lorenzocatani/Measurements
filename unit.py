
# We define a class that takes  the value (e.g. 5), the unit (e.g. km) and the measure(length or time).
class Measure(object):
        def __init__(self,value,unit,measure):
                self.value=value
                self.unit=unit
	        self.measure=measure
		 #if self.unit=='km' or self.unit=='m':
		  #     self.measure='length'
		 #if self.unit=='h' or self.unit=='s':
		  #     self.measure='time'  
	       #        return self.measure  This works wrong
		# this function convert the current unit into the one indicated by unitconvertion.	
	def conversion(self, unitconversion):
         if self.unit=='m' and unitconversion=='km':
             return 0.001*self.value
         elif self.unit=='km' and unitconversion=='m':
             return 1000*self.value
         elif self.unit=='h' and unitconversion=='s':
             return 3600*self.value
         elif self.unit=='s' and unitconversion=='h':
             return 0.000277777777777777777777777777*self.value 
		# this function adds the values of self and others if they are the same measure and if they are the same unit.		 
        def add(self, others):
             if self.measure==others.measure:
                 if self.unit==others.unit:
                     return self.value+others.value
                 else:
                     return self.value+others.conversion(self.unit)     
             else:
                 raise ValueError('Units not summable')
                 return				 
	     def __add__(self, other):
               return self.add(other)
             def __radd__(self, other):
                  return self.__add__(other)			 
		# this function multiplies the values of self and others.				 
        def multiply(self, others):
            if self.unit==others.unit:
                 return self.value*others.value
            else:
                 return self.value*others.conversion(self.unit)     
        def __mul__(self, other):
             return self.multiply(other)	 
	     def __rmul__(self, other):
               return self.__mul__(other)	
		# define the equality function.			   
        def __eq__(self,other):
             if self.measure==other.measure:
                 if self.unit==other.unit:
                     if self.value==other.value:
                          return True
                     else:
                          return False
                 else:
                     if other.value==self.conversion(other.unit):
                          return True
                     else:
                          return False
             else:
                  raise TypeError('Incompatibleunits')	
                  return
        def __req__(self, other):
              return self.__eq__(other)	