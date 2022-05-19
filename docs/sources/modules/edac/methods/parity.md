#


## Parity
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/methods/parity.py/#L5)
```python 
Parity(
   debug: bool = False
)
```


---
A [Parity](../../../../../tutorials/ErrorDetection/parity) 
EDAC System to deal with data that needs parity code added


**Args**

* **debug** (bool, optional) : Debug Level. Defaults to False.



**Methods:**


### .decode
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/methods/parity.py/#L37)
```python
.decode(
   data: int, check: int
)
```

---
Check the if the data is same as the given 
parity code

**See Also**

- [EDACMethod](../../schema#decode)


**Args**

* **data** (int) : given data
* **check** (int) : parity bit


**Returns**

* **tuple**  : (**error**, **data**, **error bits**)
* **error** (bool) : If any error happens in the data
* **data** (int) : the corrected data (`0` for `CI`)
* **bits** (list) : the index of the error bits
`CI` for `Cannot Identify`

### .encode
[source](https://github.com/N0Ball/EDAC/blob/main/modules/edac/methods/parity.py/#L18)
```python
.encode(
   data: int
)
```

---
encode the given integer (was bytes)


**Args**

* **data** (int) : given integer


**Returns**

* **int**  : integer that is encoded

