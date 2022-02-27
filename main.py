from lib.noise.noise import NoiseFactory
from lib.noise.scheme import NoiseType

ORIGINAL_MSG = b"N0FLAG{I_4m_7h3_0R191N4L_M5G_4ND_1M_S000O0O00oo0o00O00oo0O00o0_G0OD}"

noise_generator = NoiseFactory(NoiseType.BIT_FLIP, debug=True, flip_list=[2, 4])
noise_msg = noise_generator.add_noise(ORIGINAL_MSG)

print('|'.join(list('01234567')))
print('---------------')
print('|'.join(list(bin(ORIGINAL_MSG[0])[2:].rjust(8, '0'))))
print('|'.join(list(bin(noise_msg[0])[2:].rjust(8, '0'))))

print(noise_msg)