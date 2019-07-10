alphabet = "abcdefghijklmnopqrstuvwxyz"
partialOne = ""
partialTwo = ""
newAlphabet = ""
message = input("Please enter a secret message: ")
key = int(input("Please enter a number to shift by: "))

if key == 0:
    newAlphabet = alphabet
elif key > 0:
    partialOne = alphabet[:key]
    partialTwo = alphabet[key:]
    newAlphabet = partialTwo + partialOne
else:
    partialOne = alphabet[:(26 + key)]
    partialTwo = alphabet[(26 + key):]
    newAlphabet = partialTwo + partialOne

new_message =""
for i in range(0,len(message)):
    index=alphabet.find(message[i])

    if index<0:
        new_message += message[i]
    else:
        new_message += newAlphabet[index]

print(new_message)