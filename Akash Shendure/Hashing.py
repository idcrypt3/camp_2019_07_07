def hash(message):
    digest=0
    for letter in message:
        digest+=ord(letter)
    digest=digest%256
    return digest
print(hash("Hello!"))