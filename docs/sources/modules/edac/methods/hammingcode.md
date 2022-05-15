#


## HammingCode
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/methods/hammingcode.py/#L4)
```python 
HammingCode(
   debug: bool = False
)
```


---
EDAC System to deal with data that needs hamming code 


**Args**

* **debug** (bool, optional) : Debug level. Defaults to False.



**Methods:**


### ._create_table
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/methods/hammingcode.py/#L136)
```python
._create_table(
   data: int
)
```

---
Create the hamming table according to the given block size


**Args**

* **data** (int) : data


**Returns**

* **list**  : hamming table


### .encode
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/methods/hammingcode.py/#L19)
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

* **int**  : the encoded data in integer


### .decode
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/methods/hammingcode.py/#L53)
```python
.decode(
   data: int, check: int
)
```

---
Decode the given data


**Args**

* **data** (int) : the given data
* **check** (int) : parity bytes


**Returns**

* **tuple**  : the results of the decode [see more](../../schema#decode)

