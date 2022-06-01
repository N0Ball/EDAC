#

## Intro 

---

    This is definitions of Error Detection And Correction related page.

## EDAC

Error <br>
Detection <br>
And <br>
Correction

----

EDAC is something that you can imply to your message, 
which often append bits (which are called parity bits) to the end of the message.
We called these bits [syndrome](#syndrome). By examing syndromes, 
it is able to either **detect** or **correct** errors arised during the transmission of the message.

## Syndrome
---

A syndrome is the a group of parity bits.
For example, take [parity](../../ErrorDetection/parity) as example, a `0b101` have parity bit `0b1`; 
therefore, the syndrome of `0b101` is `1`.

Since, EDAC is often described in an Galios Field; 
therefore, the syndrome can also be written as a polynomial form.
That is, if the syndrome is `0b1011` -> it is equivalent to `x^3 + x + 1`.

## SEC-DED
---

Single Error Correction Double Error Detection (SEC-DED)

### Description

EDAC schemes that are capable of detecting up to 
two simultaneous bit errors and correcting single-bit errors.

### Examples

[Hamming Code](../ErrorDetection/hammingCode) <br>
[Huffman Coding](https://en.wikipedia.org/wiki/Huffman_coding) <br>
[Hsia SEC-DED](http://www.ysu.am/files/11-1549527438-.pdf)