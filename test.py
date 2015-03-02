from nose.tools import assert_raises, assert_equal, assert_true, assert_false
from unit import Measure

def test_proposed():

    #metres = Measure(1,"m")
    #kilometres = Measure(1,"km")
    #seconds = Measure(1, "s")
    #hours = Measure(1, "h")

    assert_true(Measure(1,'km') == Measure(1000,'m'))
    assert_true(Measure(3600,"s") == Measure(1,"h"))
    with assert_raises(IncompatibleUnitsError):
        Measure(3,"m").add(Measure(4,"s"))
	 
	 
	 
#assert_true(5*metres == 0.005*kilometres)