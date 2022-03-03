# 

## Intro
---
    This is definitions of Computer Science related page

## Numbers

---

The numbers in CS can be

1. Binary \(\rightarrow\) 0, 1
2. Octal \(\rightarrow\) 0, 1, 2, 3, 4, 5, 6, 7
3. Decimal \(\rightarrow\) 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
4. Hexadecimal \(\rightarrow\) 0, 1, 2, 3, 4, 5, 6, 7, 8, a, b, c, d, e, f

### Example

take 25 as example
```python
>>> number = 25 
>>> number #Decimal
25
>>> bin(number) #Binary
'0b11001'
>>> oct(number) #Octal
'0o31'
>>> hex(number) #Hexadecimal
'0x19'
```

**The notation of this tutorial will always be:**

- Binary -> `0b`
- Octal  -> `0o`
- Decimal -> NA (No Notation)
- Hexadecimal -> `0x`

That is 
`0b11001` = `0o31` = `0x19` = `25`

## Least Significant Bit (LSB)

---
the \(1^{st}\) bit of the data, which is also the `low-order` bit or `right-most` bit

### Example

```python
>>> def LSB(n):
...     return n&1
>>> number = 15
>>> bin(number)
'0b1111'
>>> LSB(number)
1
>>> number = 14
>>> bin(number)
'0b1110'
>>> LSB(number)
0
```

## Most Significant Bit (MSB)

---
The `high-order` bit or `left-most` bit

### Example

Given a `8 bit` system

```python
>>> def MSB(n):
...     return n >> 7
... 
>>> number = 215
>>> bin(number)
'0b11010111'
>>> MSB(number)
1
>>> number = 127
>>> bin(number)
'0b1111111' #It's actuall 0b01111111 since it's a 8-bit system
>>> MSB(number)
0
```