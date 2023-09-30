from pwn import *
a = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")


for i in range(256):
    result = xor(a,i).decode()
    keyword = "crypto"
    if keyword in result:
        print(result)
        break

    