from nose.tools import assert_raises, assert_equal, assert_true, assert_false
from unit import Measure

def test_proposed():

    #meters = Measure(1,"m")
    #kilometers = Unit("length", 1e3)
    #seconds = Unit("time", 1)
    #minutes = Unit("time", 60)

    assert_true(Measure(5,"m") == Measure(0.005,"km"))
    assert_true(Measure(3600,"s")==Measure(1,"h"))
    with assert_raises(IncompatibleUnitsError):
        Measure(3,"m")+Measure(4,"s")