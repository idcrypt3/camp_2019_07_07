A = 0x5f
B = 0b1000_0010_0100_0000_1010_0111_1001_1100
C = 0x82_40_a7_9c

print(A)
print(hex(A))
print(bin(A))

if B == C:
    print("they are the same")
    print(B)
    print(C)
else:
    print("they are different")
