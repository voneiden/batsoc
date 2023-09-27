from batsoc import BatteryType, soc
from batsoc.batsoc import voltage


def test_batsoc():
    assert soc(BatteryType.ALKALINE, 1.6) == 1.0
    assert soc(BatteryType.ALKALINE, 0.0) == 0.0
    assert soc(BatteryType.ALKALINE, 1.6) == 1.0
    assert soc(BatteryType.LI_ION, 4.20) == 1.0
    assert soc(BatteryType.CR2032, 3.0) == 1.0
    assert soc(BatteryType.NICD, 1.46) == 1.0


def test_voltage():
    assert voltage(BatteryType.ALKALINE, 1.0) == 1.6
