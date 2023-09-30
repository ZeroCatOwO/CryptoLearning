#use xor()

from pwn import *
a = "label"
b = 13
a_num =[ord(i) for i in a]
xor_ab = [i ^ b for i in a_num]
xor_string = "".join(chr(i) for i in xor_ab)
print("crypto{"+xor_string+"}")
