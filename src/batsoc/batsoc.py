import csv
from enum import Enum
from pathlib import Path

from scipy.interpolate import interp1d


class BatteryType(Enum):
    ALKALINE = 1
    """ 
    Generic 1.5V non-rechargeable alkaline battery
    """

    LI_ION = 2
    """ 
    Generic lithium ion battery with a nominal 3.7/3.8 voltage 
    and 4.2 charge voltage 
    """

    CR2032 = 3
    """
    Generic 3V lithium coin cell battery. These are a bit tricky
    because they can source very small currents and feature a significant
    voltage sag with even small extended loads. 
    The curve is based on a moderate constant load of 750 µA.
    """

    NICD = 4
    """
    Ni-Cd battery. Values based on ChatGPT's lies. Nominal voltage 1.2 V,
    charge voltage up to 1.45 V
    """


_SRC_PATH = Path(__file__).parent


def _load_curve(battery_type: BatteryType):
    curve_file = _SRC_PATH.joinpath(Path(f"curves/{battery_type}.csv"))
    with open(curve_file, "r") as f:
        reader = csv.reader(f)
        return tuple(tuple((float(line[0]), float(line[1]))) for line in reader)


_CURVE = {
    battery_type: interp1d(*zip(*_load_curve(battery_type)))
    for battery_type in BatteryType
}


def soc(battery_type: BatteryType, cell_voltage) -> float:
    curve_min_voltage = min(_CURVE[battery_type].x)
    curve_max_voltage = max(_CURVE[battery_type].x)

    cell_voltage = max(min(cell_voltage, curve_max_voltage), curve_min_voltage)

    return float(_CURVE[battery_type](cell_voltage))
