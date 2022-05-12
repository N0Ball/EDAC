#


## EDACType
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/schema.py/#L4)
```python 
EDACType()
```


---
Enumerate of the EDAC Type system


----


## EDACMethod
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/schema.py/#L14)
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


### .encode
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/schema.py/#L65)
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


### .decode
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/schema.py/#L80)
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

* **tuple**  : format should be `(error, data, error bits)`
* **error** (bool) : Is the data corrupted
* **data** (bytes) : The fixed data (return `0x00` if can't be fixed)
* **bits** (list) : The index of errorbits


### .get_default_block
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/schema.py/#L35)
```python
.get_default_block()
```

---
Generate default block of the EDAC system


**Returns**

* **int**  : default block of the EDAC system


### .get_parity_size
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/schema.py/#L50)
```python
.get_parity_size()
```

---
Generate the parity size of the EDAC system


**Returns**

* **int**  : parity size of the EDAC system

