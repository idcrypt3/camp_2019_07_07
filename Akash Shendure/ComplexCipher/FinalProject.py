characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ."


def char(number):
    try:
        number = int(number)
    except ValueError:
        number = 64
    if number <= 0 or number > 64:
        number = 64
    character = characters[number - 1]
    return character


def numb(character):
    if character == "":
        character = " "
    number = characters.find(character) + 1
    if number == 0:
        number = 64
    return number


def loop(value, minimum=1, maximum=64):
    value = value % maximum
    while value < minimum:
        value = maximum
    return value


def caes(number, shift):
    shifted = number + int(shift)
    looped = loop(shifted)
    return looped


def binr(decimal):
    decimal -= 1
    binary = format(decimal, "#08b")
    number = 0
    string = ""
    for letter in binary:
        number += 1
        if number > 2:
            string += letter
    return string


def decm(binary):
    formated = '0b' + binary
    decimal = int(formated, 2)
    return decimal + 1


def tlst(text, shift, yn=True):
    listed = []
    for letter in text:
        if yn:
            listed.append(binr(caes(numb(letter), shift)))
        else:
            listed.append(binr(numb(letter)))
    return listed


def flst(listed, shift):
    text = ""
    for index in listed:
        text += char(caes(decm(index), -shift))
    return text


def keyc(ikey):
    shift = ""
    for fragment in tlst(ikey, 0, False):
        shift += fragment
    return int(shift) % 64


def keys(ikey, length):
    listed = tlst(ikey, 0, False) * (round(length / len(ikey)) + 1)
    for index in range(len(listed) - length):
        listed.pop()
    return listed


def strm(one, two):
    for index in range(len(one)):
        onestring = one[index]
        twostring = two[index]
        threestring = ""
        onebits = [int(number) for number in onestring]
        twobits = [int(number) for number in twostring]
        for iteration in range(len(onebits)):
            threestring += str(onebits[iteration] ^ twobits[iteration])
        one[index] = threestring
    return one


def cphr(imessage, ikey):
    return flst(strm(tlst(imessage, keyc(ikey)), keys(ikey, len(tlst(imessage, keyc(ikey))))), keyc(ikey))


def ques(imessage, ioptions):
    print(imessage)
    for number in range(len(ioptions)):
        print(" " + str(number + 1) + ") " + ioptions[number])
    error = True
    ianswer = ""
    while error:
        error = False
        if not error:
            ianswer = input(">>> ")
        try:
            ianswer = int(ianswer)
            error = True
            for number in range(len(ioptions)):
                if number == ianswer - 1:
                    error = False
            if error:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a number.")
            error = True
    return ianswer


print(
    "\n" * 100 + """                       WELCOME  TO
  _____ _       _             ____________ _____   ____
 / ____(_)     | |           |___  /  ____|  __ \ / __ \\
| |     _ _ __ | |__   ___ _ __ / /| |__  | |__) | |  | |
| |    | |  _ \|  _ \ / _ \ '__/ / |  __| |  _  /| |  | |
| |____| | |_) | | | |  __/ | / /__| |____| | \ \| |__| |
 \_____|_|  __/|_| |_|\___|_|/_____|______|_|  \_\\\\____/
                | |
                |_|""" + "\n" * 5)
while True:
    answer = ques("\nPlease select an option by typing a number and pressing enter.",
                  ["Encrypt or decrypt your own message.", "Decrypt a preset message.",
                   "Learn about CipherZERO."])
    if answer == 1:
        message = input("\nPlease enter the message:\n")
        key = input("\nPlease enter the key:\n")
        while len(key) < 2:
            print("The key must be more than one character long.")
            key = input("\nPlease enter the key:\n")
        print("\nCiphered Message:\n" + cphr(message, key))
    if answer == 2:
        options = ["I ate dinner.", "We had a three-course meal.", "Brad came to dinner with us.",
                   "He loves fish tacos.", "In the end, we all felt like we ate too much.",
                   "We all agreed; it was a magnificent evening."]
        for option in range(len(options)):
            options[option] = cphr(options[option], "Decrypt")
        sentence = options[
            ques("\nPlease select a message to decrypt. The key for each option is 'Decrypt'", options) - 1]
        key = input("\nPlease enter the key:\n")
        while len(key) < 2:
            print("The key must be more than one character long.")
            key = input("\nPlease enter the key:\n")
        print("\nCiphered Message:\n" + cphr(sentence, key))
    if answer == 3:
        print("\nCipherZERO is a cipher that uses Caesar Cipher and Stream Cipher to make text completely unreadable.")
        print("The cool thing about CipherZERO is that it is fully reversible.")
        print("Seperate code is not used for encryption and decryption because the same methods are used for both.")
        print("CipherZERO was created at iD Tech by Akash Shendure during a Cybersecurity and Encryption course.")
