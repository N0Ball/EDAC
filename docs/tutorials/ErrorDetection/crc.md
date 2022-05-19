# 

## Cyclic Redundancy Check

---

An Error detecting method

### How

You can simply see that CRC check is
transforming \(\Bbb R^2 \rightarrow GF(2^n)\), where \(GF\) is the [Galois Field](../../definitions/math#galois-field), 
where n is the length of CRC [syndrome](../../definitions/EDAC#syndrome).

This is calculating the remainer of two polynomials, 
since different data have **less posibility** of having the **same remainer**, therefore by checking the remainer, 
we can **kind of** know if the data is changed or not.

**NOTE:** The biggest charactoristic of this method is, a little change of the polynomial will cause a large difference of the remainer, 
therefore, if we know that he [hamming distance](../definitions/math#hamming-distance) are feasibly small, 
we can say that we can detect if an error occurs.

### Example

Take `0b11010` as example
the [syndrome](../../definitions/EDAC#syndrome) length is 3 ( \(GF(2^3)\) ),
the [generator](../../definitions/math#generator-of-a-galois-field) is \(x^3 + x^1 + 1\).

#### Encoding

1. Append n `0`s for CRC check `0b11010000`
2. Put it in \(GF(2^n)\), where the generator is \(x^3 + x^1 + 1\) -> It is the remainder of \(\frac{x^7 + x^6 + x^4}{x^3 + x^1 + 1}\)

```shell
        11110
    ---------
1011|11010000
     1011
    -------
      1100
      1011
     -------
       1110
       1011
      -------
        1010
        1011
       ------
           10 -> the answer is 010 since the length should be three
```

Therefore, we have get the encoded message `0b11010010`.

#### Decoding

Simply get rid of the last n (`3`) digit.
`0b11010010` -> `0b11010`

#### Error Detecting

1. Put the message in \(GF(2^n)\), where the generator is \(x^3 + x^1 + 1\) -> It is the remainder of \(\frac{x^7 + x^6 + x^4 + x^1}{x^3 + x^1 + 1}\)

```shell
        11110
    ---------
1011|11010010
     1011
    -------
      1100
      1011
     -------
       1110
       1011
      -------
        1011
        1011
       ------
           00 -> the answer is 0 -> No error occurs
```

## Python code Sample

```python
>>> import binascii
>>> message = "hello"
>>> hex(binascii.crc32(message.encode()))
'0x3610a686'
```