#


## EDACType
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/schema.py/#L5)
```python 
EDACType()
```


---
Enumerate of the EDAC Type system


----


## EDACMethod
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/schema.py/#L13)
```python 
EDACMethod(
   edac_type: EDACType = EDACType.NO_EDAC, debug: bool = False
)
```


---
The Base class of the EDAC Method
which means that all EDAC should contains all the methods
it contains and will only be call the method it contains


**Args**

* **TYPE** ([EDACType](./#edactype)) : The type of the EDAC system
* **DEBUG** (bool) : Debug flag



**Methods:**


### .decode
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/schema.py/#L74)
```python
.decode(
   data: int, check: int
)
```

---
The method that the EDAC system need to decode for checking
the correctness


**Args**

* **data** (int) : The data to be checked
* **check** (int) : Parity Code to check


**Returns**

* **tuple**  : format should be `(error, original_data, errorbits)`
* **error** (bool) : Is the data corrupted
* **original_data** (bytes) : The fixed original data (`None` if can't be fixed)
* **errorbits** (list) : The index of errorbits


### .encode
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/schema.py/#L59)
```python
.encode(
   data: int
)
```

---
The method that the EDAC system need to encode for futher
EDAC usage


**Args**

* **data** (int) : the data to be encoded


**Returns**

* **int**  : the data encoded

