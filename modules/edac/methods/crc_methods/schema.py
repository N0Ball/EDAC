from enum import Enum, auto

class SCHEMA(Enum):

    CRC_1 = auto()
    CRC_5_CCITT = auto()
    CRC_5_USB= auto()
    CRC_7 = auto()
    CRC_8 = auto()
    CRC_8_ATM = auto()
    CRC_8_CCITT = auto()
    CRC_8_DALLAS = auto()
    CRC_8_MAXIM = auto()
    CRC_12 = auto()
    CRC_16_CCITT = auto()
    CRC_16_IBM = auto()
    CRC_16_BBS = auto()
    CRC_32_IEEE = auto()
    CRC_32_C = auto()
    CRC_64_ISO = auto()
    CRC_64_ECMA_182 = auto()

def GENERATOR(schema: SCHEMA) -> list:

    generator = {
        SCHEMA.CRC_1: [1, 0],
        SCHEMA.CRC_5_CCITT: [5, 3, 1, 0],
        SCHEMA.CRC_5_USB: [5, 2, 0],
        SCHEMA.CRC_7: [7, 3, 0],
        SCHEMA.CRC_8: [8, 7, 6, 4, 2, 0],
        SCHEMA.CRC_8_ATM: [8, 2, 1, 0],
        SCHEMA.CRC_8_CCITT: [8, 7, 3, 2, 0],
        SCHEMA.CRC_8_DALLAS: [8, 5, 4 ,0],
        SCHEMA.CRC_8_MAXIM: [8, 5, 4, 0],
        SCHEMA.CRC_12: [12, 11, 3, 2, 1, 0],
        SCHEMA.CRC_16_CCITT: [16, 12, 5, 0],
        SCHEMA.CRC_16_IBM: [16, 15, 2, 0],
        SCHEMA.CRC_16_BBS: [16, 15, 10, 3],
        SCHEMA.CRC_32_IEEE: [32, 26, 23, 22, 16, 12, 11, 10, 8, 7, 5, 4, 2, 1, 0],
        SCHEMA.CRC_32_C: [32, 28, 27, 26, 25, 23, 22, 20, 19, 18, 14, 13, 11, 10, 9, 8, 6, 0],
        SCHEMA.CRC_64_ISO: [64, 4, 3, 1, 0],
        SCHEMA.CRC_64_ECMA_182: [64, 62, 57, 55, 54, 53, 52, 47, 46, 45, 40, 39, 38, 37, 35, 33, 32, 31, 29, 27, 24, 23, 22, 21, 19, 17, 13, 12, 10, 9, 7, 4, 1, 0],
    }.get(schema, None)

    assert generator != None, f"ERROR: Generator of shema: <{schema}> not found!"

    return generator