#


## CRC
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/methods/crc.py/#L4)
```python 
CRC(
   debug: bool = False, *args, **kwargs
)
```


---
EDAC System to deal with data that needs CRC


**Args**

* **debug** (bool, optional) : Debug level. Defualts to False.
* **kwargs** (optional) : The keyword argument passed from             [EDAC Factory](../../factory#EDACFactory). Defualts to None.            **should contian key `schema`**
* **schema** ([SCHEMA](../crc_methods/schema#SCHEMA)) : The schema of            CRC you chose to use, defaults to `CRC_8_ATM`



**Methods:**


### .decode
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/methods/crc.py/#L69)
```python
.decode(
   data: int, check: int
)
```

---
Decode the given data


**Args**

* **data** (int) : the target data to decode
* **check** (int) : syndrome


**Returns**

* **tuple**  : the results of the decode [see more](../../schema#decode)


### .encode
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/methods/crc.py/#L53)
```python
.encode(
   data: int
)
```

---
Encode the given data


**Args**

* **data** (int) : the data in integer


**Returns**

* **int**  : the syndrome in interger


### ._devide
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/methods/crc.py/#L91)
```python
._devide(
   data: int
)
```

---
Devide in GF(\(2^n\)) of given generator


**Args**

* **data** (int) : the given data


**Returns**

* **int**  : the result

