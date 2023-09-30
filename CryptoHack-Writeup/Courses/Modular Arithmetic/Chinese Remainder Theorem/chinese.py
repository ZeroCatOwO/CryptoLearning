from Crypto.Util.number import *
#x ≡ a mod m
#x ≡ 2 mod 5
#x ≡ 3 mod 11
#x ≡ 5 mod 17
a1, a2, a3 = 2, 3, 5
m1, m2, m3 = 5, 11, 17
M = 5 * 11 * 17
M1, M2, M3 = M // 5, M // 11, M // 17

t1 = inverse(M1, 5)
t2 = inverse(M2, 11)
t3 = inverse(M3, 17)

X = M1*t1*a1 + M2*t2*a2 + M3*t3*a3
print(f"flag : {X % M}")
