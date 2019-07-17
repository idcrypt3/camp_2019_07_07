code = "1001001010100001"
key = "1001110100010101"
cipher = ""
codeBits = [int(i) for i in str(code)]
keyBits = [int(i) for i in str(key)]
cipherBits = []
for i in range(0, len(codeBits)):
    cipherBit = codeBits[i] ^ keyBits[i]
    cipherBits.append(cipherBit)
cipher = cipher.join(str(i) for i in cipherBits)
print("Cipher: " + cipher)
