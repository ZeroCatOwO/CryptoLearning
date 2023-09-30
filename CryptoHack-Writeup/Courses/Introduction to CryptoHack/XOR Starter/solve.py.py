a = "label"
b = 13
a_num = []
xor_num = []

for i in a : # chr to num
    a_num.append(ord(i)) 


for i in a_num : # get xor_num
    xor_num.append(chr(i ^ b))

#flag = crypto{xor_num}
print("crypto{",end="")
for i in xor_num:
    print(i,end="")
print("}")
