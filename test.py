from DES import DES
from AES import *
import util


"""print(AES128("414553206573206d757920666163696c", "2b7e151628aed2a6abf7158809cf4f3c",mode="encode", mes_is_hex=True, key_is_hex=True))
print(AES128("e448e574a374d90cc33c22af9b8eab7f", "2b7e151628aed2a6abf7158809cf4f3c",mode="decode", mes_is_hex=True, key_is_hex=True))"""

"""ecb_m = ECB("AES es un algoritmo muy importante en la seguridad de la informacion actual", "0123456789ABCDEF0123456789ABCDEF", mode="encode", mes_is_hex=False, key_is_hex=True)
print(ecb_m)
ecb_m = ECB("0071a070ba171f8880eea34b6f3e7cbae7906e0d39deae0448a4357871852146e9a2cbf66e080be574d59fc6aebb916b378a39a06b321db331efc748c279e2ff8ac78210774b919e1fc939337d28a33d", "0123456789ABCDEF0123456789ABCDEF", mode="decode", mes_is_hex=True, key_is_hex=True)
ecb_m = util.ascii_hex_to_str(ecb_m)
print(ecb_m)"""




print(util.powermod(2, 20, 100))
print(util.discrete_log(2, 76, 100))