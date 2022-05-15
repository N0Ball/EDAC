# 

## Hamming Code

---

A [SEC-DED](../definitions/EDAC.md#sec-ded) method.
Capable of detect and correct errors.

### How

The index of the data can be seperate into different *groups* 
by the index of it's binary data. [[1]](#1) 
Therefore, the index of a \(2^{n}\)-bit data can be presented with n *groups* (n-bits).

If we set the significant bit [[2]](#2) as the parity bit of each group, 
we can know which *groups* contain error.

If there are only one error bit, 
the combination of the *groups* that contains error 
is the index of the bit that is error.[[4]](#4)

The \(0^{th}\) bit of the data doesn't belongs to any *group*.
This means that we can't use the above method to identify if it is correct or not. 
However we can set the \(0^{th}\) bit as the [parity bit](../ErrorDetection/parity.md#parity-bit) 
to the whole data string as an identify of 2 errors.

Since *groups* expect that there are only one errors in the data; 
however if there exists over one errors, the *groups* will only **try to fix** one error 
(which is correcting an correct data -> creates another incorrect data).
This means that if only two errors exist, the **fix** will make `3` errors.

### Summary

- For every \(2^{n}\)-bit data, we need (n+1)-bit parity bits (1 the \(0^{th}\) bit).
- The combinations of the error *groups* can identify the error (**SEC**).
- The \(0^{th}\) bit is the parity bit for the whole data (**DED**).

## Examples

take \(2^3\) bits data, which is a (8-3-1, 4) -> (4, 4) hamming code for example.

### Encode

If the data is `1011` -> the message will be `xxx1x011`

**GROUPS**

```shell
0: x, 1, 0, 1 -> x = 0
1: x, 1, 1, 1 -> x = 1
2: x, 0, 1, 1 -> x = 0
```

Therefore the message becomes `x0110011` -> x = 0 ([parity bit](./parity.md#parity-bit)).
We get the final encoded message `00110011`.

### Decode

Simple git rid of the parity bits: `00110011` -> `xxx1x011` -> `1011`

### Error Detection

#### Example 1

`00110011` -> `001100111` (change bit 5 -> the \(5^{th}\) bit have error).

**GROUPS**

```shell
0: 0, 1, 1, 1 -> 1 -> INCORRECT
1: 1, 1, 1, 1 -> 0 -> CORRECT
2: 0, 1, 1, 1 -> 1 -> INCORRECT
```

We have detected the error! (1, 0, 1) = `0b101` = 5 [[4]](#4).
Therefore we can correct it by flipping the \(5^{th}\) bit.
`00110111` -> `00110011`, we get the original data.

#### Example 2

`00110011` -> `00110001` (change bit 6)

**GROUPS**

```shell
0: 0, 1, 0, 1 -> 0 -> CORRECT
1: 1, 1, 0, 1 -> 1 -> INCORRECT
2: 0, 0, 0, 1 -> 1 -> INCORRECT
```

We have detected the error! (1, 1, 0) = `0b110` = 6 [[4]](#4).
Therefore we can correct it by flipping the \(6^{th}\) bit.
`00110001` -> `00110011`, we get the original data.

#### Example 3

`00110011` -> `00110101` (change bit 5 and 6)

**GROUPS**

```shell
0: 0, 1, 1, 1 -> 1 -> INCORRECT
1: 1, 1, 0, 1 -> 1 -> INCORRECT
2: 0, 1, 0, 1 -> 0 -> CORRECT
```

We **think** that we detected the error! (0, 1, 1) = `0b011` = 3.
Therefore we tried to correct it by flipping the \(3^{rd}\) bit, which makes three incorrects.
`00110101` -> `00100101`, we can see that the \(0^{th}\) bit parity didn't pass.
We **find** an error that can't be corrected.

### More

The result of this can be viewed as the [sum](../../definitions/math#summations) of the index of the data that have `1`

Take [Example 1](#example-1) as an example.
`00110011` -> the 2, 3, 6, 7 bit have `1`.

```shell
  010
  011
  110
  111
+ ---
  000 -> This is what we set, every group's sum is 0
```

Therefore if `00110011` -> `00110111` (change bit 5)

```shell
  010
  011
  101
  110
  111
+ ---
  101 = 5 -> This is the same as what we do above but turned 90 degrees
```

That is, we can simple [sum](../definitions/math#summations) all the index that have `1`.
The result of will be the index that have error.

**Do you see the mathematics inside?**

1. We make the sum (which is `xor`) of all the indexs that the data contains `1` to 0 -> the encoding.
2. Since `0 ^ x = x` -> if there are only one error, we can simply detect the error by sum it again. -> error detecting.

## Python Code

Below are simple python codes for encoding and decoding.

### Encoding

```python
>>> from functools import reduce
>>> message = [list(map(int, "1011"))]
>>> encodeMatrix = [
...     [1, 1, 1, 0, 0, 0, 0],
...     [1, 0, 0, 1, 1, 0, 0],
...     [0, 1, 0, 1, 0, 1, 0],
...     [1, 1, 0, 1, 0, 0, 1]
... ] # the encode procedure can be written as a matrix
>>> encode = list(*[[sum(a*b for a,b in zip(X_row,Y_col))%2 for Y_col in zip(*encodeMatrix)] for X_row in message]) # encode the data
>>> encode.insert(reduce(lambda a, b: int(a) ^ int(b), encode), 0) # Create 0th bit parity 
>>> encode
[0, 0, 1, 1, 0, 0, 1, 1]
```

### Error detecting 

```python
>>> encode = [0, 0, 1, 1, 0, 0, 1, 1]
>>> reduce(lambda a, b: a^b, [e[0] for e in filter(lambda x: x[1], enumerate(encode))])
0 # No errors
>>> encode = [0, 0, 1, 0, 0, 0, 1, 1]
>>> reduce(lambda a, b: a^b, [e[0] for e in filter(lambda x: x[1], enumerate(encode))])
3 # Third bit have error
```

### Error Correcting

Correct single error
```python
>>> encode = [0, 0, 1, 0, 0, 0, 1, 1] # Original [0, 0, 1, 1, 0, 0, 1, 1]
>>> encode[reduce(lambda a, b: a^b, [e[0] for e in filter(lambda x: x[1], enumerate(encode))])] ^= 1
>>> reduce(lambda a, b: int(a) ^ int(b), encode) == 0
True
>>> encode
[0, 0, 1, 1, 0, 0, 1, 1] # Successfully fix the error
```

Detects double error
```python
>>> encode = [0, 0, 1, 0, 1, 0, 1, 1] # Original [0, 0, 1, 1, 0, 0, 1, 1]
>>> encode[reduce(lambda a, b: a^b, [e[0] for e in filter(lambda x: x[1], enumerate(encode))])] ^= 1
>>> reduce(lambda a, b: int(a) ^ int(b), encode) == 0
False # Unfixable detected (double error)
```

## Problem

As we know, this is a double error detecting system, therefore, if the [hamming distance](../../definitions/math#hamming-distance) \( H(m) \gt 2\).
Though the results might give you correct; however it is incorrect

```python
>>> encode = [0, 0, 1, 0, 1, 0, 0, 1] # Original [0, 0, 1, 1, 0, 0, 1, 1]
>>> encode[reduce(lambda a, b: a^b, [e[0] for e in filter(lambda x: x[1], enumerate(encode))])] ^= 1
>>> reduce(lambda a, b: int(a) ^ int(b), encode) == 0
True
>>> encode
[0, 1, 1, 0, 1, 0, 0, 1] # Original [0, 0, 1, 1, 0, 0, 1, 1] -> Different from original
```

We can see that although it says that it successfully corrects the message; however it is still different from its original message.

## Reference

### [1]

For example:

```shell
0 -> 0b000
1 -> 0b001
2 -> 0b010
3 -> 0b011
4 -> 0b100
5 -> 0b101
6 -> 0b110
7 -> 0b111
```

The \(0^{th}\) group is `0, 2, 4, 7`, since the \(0^{th}\)
index of thier binaries are 1 (`0b001`, `0b011`, `0b101`, `0b111`). 
The \(1^{st}\) group is `2, 3, 6, 7` (`0b010`, `0b011`, `0b110`, `0b111`).

### [2]

The significant bit of a group is the bit that have only one `1` 
while presented in binary [[3]](#3). 
The reason we choose this is beacuse significsant bits are one and only to thier groups 
since they have only one `1`. 
That is, for *group 0*, `1` is the significant bit, and `1` is only in *group 0*; 
however `3` is not is because *group 0* containes `3`, 
but `3` is in both *group 0* and *gorup 1*.

### [3]

For example:
significant bit of the *group 0* is `1` 
since `1` is `0b00000001`, 
which only one `1` exists in the binary.
The significant bit of *group 5* is `32`, since `32` is `0b00100000`, 
also only one `1` is in it's binary.
<br>
We can also say that the significant bit of *group n* is `2n`, 
since that is how binary is.

### [4]

Take a \(2^3\)-bit data as an example:

1. There are 3 groups
2. `O` is **correct** `X` is **incorrect**
3. There are only one error. (Single Error)

**GROUPS**

```shell
0: 1, 3, 5, 7
1: 2, 3, 6, 7
2: 4, 5, 6, 7
```

**COMBINATIONS**

```shell
| 2 | 1 | 0 | error bit |
|---+---+---+-----------|
| O | O | O |     X     |
|---+---+---+-----------|
| O | O | X |     1     |
|---+---+---+-----------|
| O | X | O |     2     |
|---+---+---+-----------|
| O | X | X |     3     |
|---+---+---+-----------|
| X | O | O |     4     |
|---+---+---+-----------|
| X | O | X |     5     |
|---+---+---+-----------|
| X | X | O |     6     |
|---+---+---+-----------|
| X | X | X |     7     |
|-----------------------|
```

- If only *group 1* is incorrect -> Second bit have error (`2`).
    - *group 0* and *group 2* is correct.
    - since we are finding the incorrect bit
        - the number can't be in *group 0* and *group 2* (since both of the groups are correct).
        - the number must be in *group 1* (since the group is incorrect).
    - you can't find any number except `2` that contains *group 1* but *group 0* and *group 2*.
- If both *group 0* and *group 1* is incorrect -> Third bit have error (`3`).
    - only *group 2* is correct.
    - since we are finding the incorrect bit
        - the number can't be in *group 2* (since *group 2* is correct).
        - the number must be in *group 0* and *group 1* (since both of the groups are incorrect).
    - you can't find any number except `3` that contains *group 0* and *group 1* but *group 2*.
- If both *group 1* and *group 2* is incorrect -> Sixth bit have error (`6`).
    - only *group 0* is correct.
    - since we are finding the incorrect bit
        - the number can't be in *group 0* (since *group 0* is correct).
        - the number must be in *group 1* and *group 2* (since both of the groups are incorrect).
    - you can't find any number except `6` that contains *group 1* and *group 2* but *group 0*.

**Do you see the relation of error groups and indexs?**


If we see the incorrect groups as `1`, 
the correct groups as `0`, 
we can view the combination of groups as one binary number, 
the error is the result of the binary.

That is 
(remember, the index should be inverse, since `0b001` the zeroth index is the right most):

- If only *group 1* is incorrect.
    - (0, 1, 0) -> `0b010` -> 2
    - second bit have error.
- If both *group 0* and *group 1* is incorrect.
    - (0, 1, 1) -> `0b011` -> 3
    - third bit have error.
- If both *group 1* and *group 2* is incorrect.
    - (1, 1, 0) -> `0b110` -> 6
    - sixth bit have error.

We get the same result as above.