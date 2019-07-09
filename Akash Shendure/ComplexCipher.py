alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,."
newAlphabet="."
for letter in alphabet:
    newAlphabet+=letter
    newAlphabet+=".,."
print(newAlphabet)