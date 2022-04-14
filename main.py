from modules.edac.factory import EDACFactory
from modules.edac.schema import EDACType
from modules.noise.factory import NoiseFactory
from modules.noise.schema import NoiseType

ORIGINAL_MSG = b'A'

edac_system = EDACFactory(EDACType.HAMMING_CODE)
ENC_MSG = edac_system.encode(ORIGINAL_MSG)

for i in range(0, len(ENC_MSG)):

    print('\t|'.join([str(j) for j in range(8*i, 8*i+8)]))
    print('-'*60)
    # print('\t|'.join(list(bin(ORIGINAL_MSG[i])[2:].rjust(8, '0'))))
    print('\t|'.join(list(bin(ENC_MSG[i])[2:].rjust(8, '0'))))
    print()

print(ENC_MSG)

noise_system = NoiseFactory(NoiseType.BIT_FLIP, flip_list=[3, 7])
NOISE_MSG = noise_system.add_noise(ENC_MSG)

for i in range(0, len(NOISE_MSG)):

    print('\t|'.join([str(j) for j in range(8*i, 8*i+8)]))
    print('-'*60)
    print('\t|'.join(list(bin(ENC_MSG[i])[2:].rjust(8, '0'))))
    print('\t|'.join(list(bin(NOISE_MSG[i])[2:].rjust(8, '0'))))
    print()

# pass_check, DEC_MSG, error_bits = edac_system.decode(NOISE_MSG)
print(edac_system.decode(NOISE_MSG))

# if pass_check:
#     print(DEC_MSG)
# else:
#     print(DEC_MSG)
#     print(error_bits)