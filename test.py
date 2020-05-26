from DES import DES
from AES import *
import util


"""print(AES128("414553206573206d757920666163696c", "2b7e151628aed2a6abf7158809cf4f3c",mode="encode", mes_is_hex=True, key_is_hex=True))
print(AES128("e448e574a374d90cc33c22af9b8eab7f", "2b7e151628aed2a6abf7158809cf4f3c",mode="decode", mes_is_hex=True, key_is_hex=True))"""

ecb_m = CFB("414553206573206d757920666163696c", "2b7e151628aed2a6abf7158809cf4f3c", "4d857d2408b00c3dd17f0c4ffcf15b97", mode="encode", mes_is_hex=True, key_is_hex=True)
print(ecb_m)
ecb_m = CBC("AES es un algoritmo muy importante en la seguridad de la informacion actual", "0123456789ABCDEF0123456789ABCDEF", "4d857d2408b00c3dd17f0c4ffcf15b97", mode="encode", mes_is_hex=False, key_is_hex=True)
print(ecb_m)
ecb_m = CFB("AES es un algoritmo muy importante en la seguridad de la informacion actual", "0123456789ABCDEF0123456789ABCDEF", "4d857d2408b00c3dd17f0c4ffcf15b97", mode="encode", mes_is_hex=False, key_is_hex=True)
print(ecb_m)


#print(util.powermod(2, 20, 100))
#print(util.discrete_log(2, 76, 100))