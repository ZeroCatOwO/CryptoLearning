# get "myXORkey"
from pwn import *

str = bytearray.fromhex(
    "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
)

keyword = b"crypto{"
# secret ^ crypto{ = str[:7]
# str[:7] ^ crypto{ = secret
for i in range(0, len(keyword)):
    print(xor(str[i], keyword[i]).decode(), end="")
# print(xor(str, "myXORkey").decode())
