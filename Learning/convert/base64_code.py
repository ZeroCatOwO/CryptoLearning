import base64 
str = "Hello"
bytes_str = str.encode()# str to bytes
print("bytes :", bytes_str)
###
base64_str = base64.b64encode(bytes_str)# bytes use base64encode
print("base64 :", base64_str)
print("bytes :", base64.b64decode(base64_str))# base64decode
