def decode (message):
    alphabet =  "abcdefghijklmnopqrstuvwxyz"
    for key in range (len(alphabet)):
        newalphabet = alphabet[key:] + alphabet[:key]
        attempt = ""
        for i in range(len(message)):
            index = alphabet.find(message[i])
            if index<0:
                attempt += message[i]
            else:
                attempt+=newalphabet[index]
        print ("key"+str(key)+"-"+attempt)
if __name__ == "__main__":
    message = "wpau iwt ephhldgs udg iwt uxghi rajt xh tctgvxots"
    decode(message)
