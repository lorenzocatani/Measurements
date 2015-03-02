from nose.tools import assert_raises, assert_equal, assert_true
from unit import Measure

def test_equalities():
    assert_true(Measure(5,'km','length')==Measure(5000,'m','length'))
    assert_true(Measure(3600,"s",'time') == Measure(1,"h",'time'))
	 
def test_bad_addition():
    with assert_raises(TypeError):
        Measure(3,"m",'length').add(Measure(4,"s",'time'))	 
		
def test_multiplication():
    with assert_raises(TypeError):
        Measure(3,"m",'length').multiply(Measure(4,"s",'time'))

