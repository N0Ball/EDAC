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


### .get_default_block
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/schema.py/#L34)
```python
.get_default_block()
```

---
Generate default block of the EDAC system


**Returns**

* **int**  : default block of the EDAC system


### .encode
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/schema.py/#L69)
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


### .get_parity_size
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/schema.py/#L52)
```python
.get_parity_size()
```

---
Generate the parity size of the EDAC system


**Returns**

* **int**  : parity size of the EDAC system


### .decode
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/schema.py/#L84)
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

