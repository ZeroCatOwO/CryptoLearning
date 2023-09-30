a = 66528
b = 52920

while(b != 0):
    temp = a % b
    a = b
    b = temp

print(a)