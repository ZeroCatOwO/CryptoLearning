from Crypto.Util.number import *

str = "Zer0cat"
str_bytes = str.encode()# str to bytes
print("bytes :", str_bytes)
###
str_int = bytes_to_long(str_bytes)# bytes to int
print("int :", str_int)
print("bytes :", long_to_bytes(str_int))# int to bytes