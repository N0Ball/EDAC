# 

## Parity bit

---
**Check Bit**, which is a bit that can detect errors.

## How

---
- Examing the [Least significant bit](../../definitions/computerScience/#least-significant-bit-lsb) of the whole communication string
- Applied in an 8-bit communication system `7 + 1(parity)`

the [sum](../../definitions/math/#summations) of every bit should be 0

## Examples

---
take `25 (0b11001)` as an example

| 0 | 1 | 2 | 3 | 4 | 5 | 6 |<spam style="color: red;">7</spam>|
|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 1 | 0 | 0 | 1 |<spam style="color: red;">1</spam>| 

The parity bit is the 7<sup>th</sup> bit, since the sum of every bit in `25 (0b11001)` is `1`; therefore the value of parity bit is \(0 - 1 = 0 \oplus 1 = 1\)

----

take `30 (0b11110)` as an example

| 0 | 1 | 2 | 3 | 4 | 5 | 6 |<spam style="color: red;">7</spam>|
|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 1 | 1 | 1 | 0 |<spam style="color: red;">0</spam>| 

The parity bit is the 7<sup>th</sup> bit, since the sum of every bit in `30 (0b11110)` is `0`; therefore the value of parity bit is \(0 - 0 = 0 \oplus 0 = 0\)

## Error Detection

---
If **`single bit flip`** occurs, the sum of the bits will not be 0. That is, you can simply sum every bits to check whether an error appears.

a simple python code to check `30 (0b11110)` is listed below 

```python
>>> from functools import reduce
>>> message = "00111100" # e = 0b0
>>> reduce(lambda a, b: int(a) ^ int(b), message) == 0
True
>>> message = "00110100" # e = 0b1000
>>> reduce(lambda a, b: int(a) ^ int(b), message) == 0
False
```

## Problems

---
The bigest problem of parity bit is that you can't identify the error if the [hamming distance](../../definitions/math/#hamming-distance) \(H_d(m) \gt 1\)

Check m = `30 (0b11110)` again but with \(H_d(m) = 2\) with error e `11000000` => m + e = `(0b1111110)`

```python
>>> from functools import reduce
>>> message = "11111100" # Message recieved in Binary
>>> reduce(lambda a, b: int(a) ^ int(b), message) == 0
True
```

*   The result is `True` which means `no errors` however, \(e \ne 0\)

This is called a `collision`, which means two different system have the same parity code

## See also

---

- [Numbers](../../definitions/computerScience/#numbers)
- [Summations](../../definitions/math/#summations)
- [Hamming Distance](../../definitions/math/#hamming-distance)