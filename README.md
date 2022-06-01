# EDAC

A Learning Program for Error Decoding and Correction

you can either 

## Learn

How to **decode**, **encode** or **correct** your EDAC message.

## Test

Your EDAC implementation

# Intro

## What is EDAC

**In a nutshell:** 

A method that you can 

- Detect Error
- Correct Error

to your data

[A little more details](../tutorials/definitions/EDAC#edac)

## What EDAC Systems do we have

- [CRC](modules/edac/methods/crc/)
- [Hamming Code](modules/edac/methods/hammingcode/)
- [Parity Bit](modules/edac/methods/parity/)

## If you want to learn EDACs

- [CRC](../tutorials/ErrorDetection/crc/)
- [Hamming Code](../tutorials/ErrorDetection/hammingCode/)
- [Parity Bit](../tutorials/ErrorDetection/parity/)

# Installations

## Before you run

```sh
git clone https://github.com/N0Ball/EDAC.git
python3 -m pip install -r requirements
```

## Web API

```sh
export FLASK_APP=server/web/server:app
flask run
```

## Docs
[Documentations](https://n0ball.github.io/EDAC)

```sh
make view-docs # Open a server to view documentation
make build-docs # Auto create docs from code
make deploy-docs # Create doc on github page
```