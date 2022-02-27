from lib.noise.noise import NoiseFactory
from lib.noise.scheme import NoiseType

ORIGINAL_MSG = b"N0FLAG{I_4m_7h3_0R191N4L_M5G_4ND_1M_S000O0O00oo0o00O00oo0O00o0_G0OD}"
DEBUG = True

noise_generator = NoiseFactory(NoiseType.NO_NOISE)
msg_with_noise = noise_generator.add_noise(ORIGINAL_MSG)

print(msg_with_noise)