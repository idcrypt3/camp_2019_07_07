characters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ."
def char(number):
    try:
        number=int(number)
    except:
        number=64
    if number<=0 or number>64:
        number=64
    character=characters[number-1]
    return character
def numb(character):
    if character=="":
        character=" "
    number=characters.find(character)+1
    if number==0:
        number=64
    return number
def loop(value,min=1,max=64):
    value=value%max
    while value<min:
        value=max
    return value
def caes(number,shift):
    shifted=number+int(shift)
    looped=loop(shifted)
    return looped
def binr(decimal):
    decimal-=1
    binary=format(decimal,"#08b")
    number=0
    string=""
    for letter in binary:
        number+=1
        if number>2:
            string+=letter
    return string
def decm(binary):
    format='0b'+binary
    decimal=int(format,2)
    return decimal+1
def tlst(text,shift,yn=True):
    list=[]
    for letter in text:
        if yn:
            list.append(binr(caes(numb(letter),shift)))
        else:
            list.append(binr(numb(letter)))
    return list
def flst(list,shift):
    text=""
    for index in list:
        text+=char(caes(decm(index),-shift))
    return text
def keyc(key):
    shift=""
    for fragment in tlst(key,0,False):
        shift+=fragment
    return int(shift)%64
def keys(key,length):
    list=tlst(key,0,False)*(round(length/len(key))+1)
    for index in range(len(list)-length):
        list.pop()
    return list
def strm(one,two):
    for index in range(len(one)):
        onestring=one[index]
        twostring=two[index]
        threestring=""
        onebits=[int(number) for number in onestring]
        twobits=[int(number) for number in twostring]
        for iteration in range(len(onebits)):
            threestring+=str(onebits[iteration]^twobits[iteration])
        one[index]=threestring
    return one
def cphr(message,key):
    return flst(strm(tlst(message,keyc(key)),keys(key,len(tlst(message,keyc(key))))),keyc(key))
def ques(message,options):
    print(message)
    for number in range(len(options)):
        print(" "+str(number+1)+") "+options[number])
    error=True
    while error:
        error=False
        answer = input(">>> ")
        try:
            answer=int(answer)
            error=True
            for number in range(len(options)):
                if number==answer-1:
                    error=False
            if error==True:
                print("Please enter a valid number.")
        except:
            print("Please enter a number.")
            error=True
    return answer
print("\n"*100+"""                       WELCOME  TO\n  _____ _       _             ____________ _____   ____\n / ____(_)     | |           |___  /  ____|  __ \ / __ \\\n| |     _ _ __ | |__   ___ _ __ / /| |__  | |__) | |  | |\n| |    | |  _ \|  _ \ / _ \ '__/ / |  __| |  _  /| |  | |\n| |____| | |_) | | | |  __/ | / /__| |____| | \ \| |__| |\n \_____|_|  __/|_| |_|\___|_|/_____|______|_|  \_\\\\____/\n         | |\n         |_|"""+"\n"*5)
while True:
    answer=ques("\nPlease select an option by typing a number and pressing enter.",["Encrypt or decrypt your own message.","Try to decrypt a preset message.","Learn about CipherZERO."])
    if answer==1:
        message=input("\nPlease enter the message:\n")
        key=input("\nPlease enter the key:\n")
        while len(key) < 2:
            print("The key must be more than one character long.")
            key = input("\nPlease enter the key:\n")
        print("\nCiphered Message:\n"+cphr(message,key))
    if answer==2:
        options=["I ate dinner.","We had a three-course meal.","Brad came to dinner with us.","He loves fish tacos.","In the end, we all felt like we ate too much.","We all agreed; it was a magnificent evening."]
        for option in range(len(options)):
            options[option]=cphr(options[option],"Decrypt")
        sentence=options[ques("\nPlease select a message to decrypt. The key for each option is 'Decrypt'",options)-1]
        key = input("\nPlease enter the key:\n")
        while len(key) < 2:
            print("The key must be more than one character long.")
            key = input("\nPlease enter the key:\n")
        print("\nCiphered Message:\n"+cphr(sentence,key))
    if answer==3:
        print("\nCipherZERO is a cipher that combines Caesar Cipher and Stream Cipher to transform text into unreadable gibberish.\nThe cool thing about CipherZERO is that it is fully reversible.\nSeperate code is not needed for encryption and decryption because CipherZERO uses the exact same methods to do both.\nCipherZERO was created at iD Tech by Akash Shendure during a Cybersecurity and Encryption course.")