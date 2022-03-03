#

## Intro 

---

    This is definitions of mathematic related page

## Summations

---
In Communication systems, the summation of `bits` or `strings` is in a [Galios Field (GF)](https://zh.wikipedia.org/zh-tw/%E6%9C%89%E9%99%90%E5%9F%9F) <!-- #TODO create definition for GF -->

### Example

take GF(2) for example

| A | B | Operation | Result |
|---|---|-----------|--------|
| 0 | 0 |    +/-    |    0   |
| 0 | 1 |    +/-    |    1   |
| 1 | 0 |    +/-    |    1   |
| 1 | 1 |    +/-    |    0   |
| 0 | 0 |     x     |    0   |
| 0 | 1 |     x     |    0   |
| 1 | 0 |     x     |    0   |
| 1 | 1 |     x     |    1   |

As you can see, the `+/-` in GF(2) is also `xor` operation and `x` is `and` operation.
That is 
$$
a \pm b = a \oplus b \\[1em]
a \times b = a \& b
$$

## Hamming Distance

---
Hamming distance is the **number of errors** in a communication system.

### Example

$$
H_d(\text{12345}, \text{22345}) = 1 \\[1em]
H_d(\text{12345}, \text{12545}) = 1 \\[1em]
H_d(\text{12345}, \text{22355}) = 2 \\[1em]
H_d(\text{12345}, \text{54321}) = 4 \\[1em]
$$