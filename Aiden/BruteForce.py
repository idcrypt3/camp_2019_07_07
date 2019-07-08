alphabet = "abcdefghijklmnopqrstuvwxyz"
myMessage = "wpau iwt ephhldgs udg iwt uxghi rajt xh tctgvxots"
def decode(myMessage):
    for key in range(len(alphabet)):
        newAlphabet = alphabet[key:] + alphabet[:key]
        attempt = ""
        for i in range(len(myMessage)):
            index = alphabet.find(myMessage[i])
            if index < 0:
                attempt += myMessage[i]
            else:
                attempt += newAlphabet[index]
        print("Key: " + str(key) + " - " + attempt)
decode(myMessage)
print("remember this for later: half the password for the first clue is energized")