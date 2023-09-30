from Crypto.Util.number import *

a = "78763"
b = b'\x013\xab'
print(int(a)) # str to int
print(type(int(a)))
print(bytes_to_long(b)) # bytes to int
print(type(bytes_to_long(b)))
