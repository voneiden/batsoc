# socbat - State of Charge (Battery)

Got a cell voltage and would like to know how much charge is left? 
Socbat to the rescue!

## Installation

```bash
pip install socbat
```

## Accuracy
Measuring state of charge based on voltage alone is not terribly
accurate. The measured voltage depends on multiple factors besides
the state of charge: temperature and load affect matters as well. 


## Usage

```python
from socbat import soc, BatteryType
soc(BatteryType.ALKALINE, 1.3)
```

will output 0.633 indicating 63.3% state of charge.

## Supported batteries
### ALKALINE
Any generic 1.5V alkaline battery under low load. 
The curve is defined for 0.8 - 1.6 volts.

### LI_ION
Any generic lithium-ion battery with a nominal voltage of 3.7 or 3.8. 
The curve is defined for 3.0 - 4.2 volts.

### CR2032
A 3V lithium coin cell battery under very low load.
The curve is defined for 2.0 - 3.0 volts. 

