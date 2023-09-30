list = [14, 6, 11]
#X^2 ≡ d mod p
#p = 29, d = someone_in_list

for X in range(1, 29):
    Quadratic_Residues = pow(X, 2, 29)
    if Quadratic_Residues in list :
        print(f"Quadratic_Residues: {Quadratic_Residues},square root: {X}")