#


## HammingCode
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/methods/hammingcode.py/#L6)
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


### .decode
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/methods/hammingcode.py/#L55)
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


### .encode
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/methods/hammingcode.py/#L21)
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


### ._create_table
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/methods/hammingcode.py/#L123)
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

