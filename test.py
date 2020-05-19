from DES import DES
from AES import AES128


print(AES128("414553206573206d757920666163696c", "2b7e151628aed2a6abf7158809cf4f3c",mode="encode", mes_is_hex=True, key_is_hex=True))
print(AES128("e448e574a374d90cc33c22af9b8eab7f", "2b7e151628aed2a6abf7158809cf4f3c",mode="decode", mes_is_hex=True, key_is_hex=True))