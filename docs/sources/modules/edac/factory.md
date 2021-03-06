#


## EDACFactory
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/factory.py/#L7)
```python 
EDACFactory(
   edac_type: EDACType, debug: bool = False, **kwargs
)
```


---
Creates the EDAC System specify by given [EDAC Type](../schema/#edactype)


**Args**

* **edac_type** ([EDACType](../schema/#edactype)) : The EDAC type needed
* **debug** (bool) : Debug Level



**Methods:**


### .encode
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/factory.py/#L39)
```python
.encode(
   data: bytes, n: int = None
)
```

---
Encodes the data with edac system


**Args**

* **data** (bytes) : The data to be encoded
* **n** (int) : The block size given (`None` as default)


**Returns**

* **bytes**  : The data encoded


### .decode
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/factory.py/#L75)
```python
.decode(
   data: bytes, n: int = None
)
```

---
Decodes the data to verify the integrity


**Args**

* **data** (bytes) : The data to be decode


**Returns**

* **tuple** (bool, bytes, list) : should be formated `(error, original data, error bits)`


### ._create_block
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/factory.py/#L124)
```python
._create_block(
   data: bytes, n: int
)
```

---
Parse data into blocks so that
every block have n bits of data


**Raises**

* **ValueError**  : If the data's type isn't `bytes`


**Returns**

* **list**  : the list of blocks needed


### .__get_edac_generator
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/factory.py/#L161)
```python
.__get_edac_generator(
   edac_type: EDACType
)
```

---
Get the edac system specified by [EDACType](../schema/#edactype)


**Raises**

* **ValueError**  : If no EDAC Type was found


**Returns**

* EDAC system 

