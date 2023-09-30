str = "Hello"
bytes_str = str.encode()# str to bytes
print("bytes :", bytes_str)
###
print("hex :", bytes_str.hex())# bytes to hex
hex_str = bytes_str.hex()
print("bytes :", bytes.fromhex(hex_str))# hex to bytes