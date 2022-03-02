#


## NoiseType
[source](https://github.com/N0Ball/EDAC/blob/main/modules/noise/scheme.py/#L3)
```python 
NoiseType()
```


---
The Noise type Enumerate of the Noise system


**Attributes**

* **NO_NOISE** (A system with no Noise) : see also [NO_NOISE](../systems/NO_NOISE/)
* **BIT_FLIP** (A system that flip bits) : see also [BIT_FLIP](../systems/BIT_FLIP/)


----


## NoiseMethod
[source](https://github.com/N0Ball/EDAC/blob/main/modules/noise/scheme.py/#L15)
```python 
NoiseMethod(
   noise_type: NoiseType = NoiseType.NO_NOISE, debug: bool = False
)
```


---
The Base class fo the Noise Method


**Args**

* **TYPE** (NoiseType) : The type of noise system
* **DEBUG** (bool) : Debug Flag


**Note**

This is the abstract base class, `add_noise` method should **never be called**


**Methods:**


### .add_noise
[source](https://github.com/N0Ball/EDAC/blob/main/modules/noise/scheme.py/#L32)
```python
.add_noise(
   data: bytes
)
```

---
Add the noise to the data from the noise system


**Args**

* **data** (bytes) : the data that the noise is going to add on


**Returns**

* **bytes**  : the data with the noise

