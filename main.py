from modules.edac.factory import EDACFactory
from modules.edac.schema import EDACType
from modules.noise.factory import NoiseFactory
from modules.noise.schema import NoiseType
from modules.edac.methods.crc_methods.schema import SCHEMA

ORIGINAL_MSG = b'FLAG'

def detail(msgs: list):

    for i in range(0, len(msgs[0])):

        print('\t|'.join([str(j) for j in range(8*i, 8*i+8)]))
        print('-'*60)

        for msg in msgs:
            print('\t|'.join(list(bin(msg[i])[2:].rjust(8, '0'))))

        print()


edac_system = EDACFactory(EDACType.CRC, True)
ENC_MSG = edac_system.encode(ORIGINAL_MSG)

detail([ENC_MSG])

print(ENC_MSG)

noise_system = NoiseFactory(NoiseType.NO_NOISE)
NOISE_MSG = noise_system.add_noise(ENC_MSG)

detail([ENC_MSG, NOISE_MSG])

pass_check, DEC_MSG, error_bits = edac_system.decode(NOISE_MSG)

if pass_check:
    print(DEC_MSG)
else:
    print(f'{DEC_MSG = }')
    print(f'with erros : {error_bits}')
