#


## BitFlipNoise
[source](https://github.com/N0Ball/EDAC/blob/main/modules/noise/noise_method/bitflip.py/#L7)
```python 
BitFlipNoise(
   debug: bool, kwargs: dict = None
)
```


---
Add the Bit Flip Noise System to the data


**Args**

* **debug** (bool) : the debug flag
* **kwargs** (optional) : The key word argument passed from             [Noise Factory](../../noise/). Defaults to None.            should contain key `flip_list`
* **flip_list** (list[int]) : A list of integer index that defines the bit index            that should be flipped


**Note**

the `**kwargs` should be `flip_list (list[int])`, if no such key in            `**kwargs` it will auto flips a random bit


**Example**



```python

>>> from lib.noise.scheme import NoiseType
>>> noise_system = NoiseFactory(NoiseType.BIT_FLIP, flip_list=[6])
>>> noise_system.add_noise(b'OUO')
b'MUO'
>>> noise_system.add_noise(b'OUO')
b'MUO'
>>> noise_system = NoiseFactory(NoiseType.BIT_FLIP)
>>> noise_system.add_noise(b'OUO')
b'OuO'
>>> noise_system.add_noise(b'OUO')
b'OÕO'
```


**Methods:**


### .__add_noise
[source](https://github.com/N0Ball/EDAC/blob/main/modules/noise/noise_method/bitflip.py/#L76)
```python
.__add_noise(
   data: bytes
)
```

---
The method to add noise


**Args**

* **data** (bytes) : The data to add noise at


**Returns**

* **bytes**  : the data with the noise


**Note**

The algorithm of this method is using a xor mask to flip the data               , since `x ^ 0 = x, x ^ 1 = !x`
Given an example

```
| 0 | 1 | 2 | 3 | 4 |

| 1 | 0 | 1 | 1 | 0 |
--------------------- XOR
| 0 | 0 | 1 | 0 | 1 |
--------------------- Results
| 1 | 0 |*0*| 1 |*1*|
```

You can see that except the \(2^{nd}\) and the \(4^{th}\) data, the data remains                the same.

### .add_noise
[source](https://github.com/N0Ball/EDAC/blob/main/modules/noise/noise_method/bitflip.py/#L47)
```python
.add_noise(
   data: bytes
)
```

---
Validate the `flip_list` and add the noise to the data


**Args**

* **data** (bytes) : The data to be noise added


**Raises**

* **IndexError**  : the `flip_list` contains integers that exceeds the length of                the original data


**Returns**

* **bytes**  : the data with the noise

