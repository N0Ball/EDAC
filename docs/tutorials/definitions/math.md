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

## Galois Field

---
**NOTE:** This is only a brief introduction to galios field, some of the concepts might be wrong, 
but is more easy for the learnings.

Field is a group of numbers that are well defined their operations.
Galois Field is a group of finite elements, which is also often called finite field, and often use \(GF\) to present it.
We often put \(\Bbb Z\) in Galois Field, since \(\Bbb R\) have infinite numbers.

### \(GF(n)\)

This is exactly the same of 
$$
f(x) \equiv x\ mod(n)
$$
Take \(GF(2)\)for example:

```shell
3 -> f(3) = 3%2 = 1
```

Therefore `3` in \(GF(2)\) is `1`.
We can see that the basic operators ( which is `+-` ) remains the same.

**Note:** the `*/` operator are quite different, 
while \(3 \times 2 \equiv 1\ mod(6)\) however \(1 / 2 = 0.5\) does not equal to anything.

### \(GF(n^m)\)

It is nearly the same as \(GF(n)\), but in a polynomial term.
That is, \(GF(2^m)\) can be written as 
$$
f(X) \equiv X\ mod(\Sigma^{m}_{i = 0} a_ix^i)
$$
where \(a_i\) is the coefficient in \(GF(n)\) with \(a_m \ne 0\) and X is the given polynomial, which also needs to be in \(GF(n)\).
\(\Sigma^{m}_{i = 0} a_ix^i\) can be chosen, and we called this chosen polynomial **generator**.

Take GF(2^3) for example, we chose generator is \(x^3 + x^1 + 1\):

$$
x^4 + x^3 + x^1 \rightarrow f(X) = x^2 + x + 1
$$

[Reference](http://www.ee.unb.ca/cgi-bin/tervo/calc2.pl?num=1+1+0+1+0&den=1+0+1+1&f=d&p=2&d=1&y=1), 
remember that the `+-` is `xor` for every `x` since there is no need for the carries.

Therefore \(x^4 + x^3 + x^1\) in \(GF(2^3)\) is \(x^2 + x + 1\).

## Generator of a Galois Field

A [Galois Field](#galois-field) is equiavlent to a function below
$$
f(X) \equiv X\ mod(\Sigma^{m}_{i = 0} a_ix^i)
$$
where X is a polynomial and \(\Sigma^{m}_{i = 0} a_ix^i\) is chosen.
Therefore we call this chosen polynomial (\(\Sigma^{m}_{i = 0} a_ix^i\)) generator.