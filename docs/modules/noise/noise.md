#


## NoiseFactory
[source](https://github.com/N0Ball/EDAC/blob/main/modules/noise/noise.py/#L5)
```python 
NoiseFactory(
   noise_type: NoiseType, debug: bool = False, **kwargs
)
```


---
Creates a noise system to add noise to.


**Args**

* **noise_type** ([NoiseType](../scheme#NoiseType)) : The noise type of the given type
* **debug** (bool, optional) : The debug flag. Defaults to False.


**Example**


```python

>>> noise_system = NoiseFactory(NoiseType.NO_NOISE)
>>> noise_system.add_noise(b"123")
b'123'

```
---
SeeAlso:
    [NoiseType](../scheme#NoiseType)


**Methods:**


### .__get_noise_generator
[source](https://github.com/N0Ball/EDAC/blob/main/modules/noise/noise.py/#L52)
```python
.__get_noise_generator(
   noise_type: NoiseType
)
```

---
Get the noise system of the given noise type


**Args**

* **noise_type** ([NoiseType](../scheme#NoiseType)) : the givin noise type seealso: noise.shceme.NoiseType


**Raises**

* **ValueError**  : No noise type found


**Returns**

* **NoiseMethod**  : the noise system


### .add_noise
[source](https://github.com/N0Ball/EDAC/blob/main/modules/noise/noise.py/#L28)
```python
.add_noise(
   data: bytes
)
```

---
Add noise to the data


**Args**

* **data** (bytes) : data to add noise on


**Raises**

* **ValueError**  : data's type is not `bytes`


**Returns**

* **bytes**  : the data with the noise

