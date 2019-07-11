import os, io

from CeaserCipher import shift_cipher as shift_cypher
from BlockCipher import pad_message as block_pad, rebuild_message as block_rebuild
from BlockCipher import apply_rotate as block_shift, undo_rotate as block_unshift
from DiffieHellman import find_shared_key as dh_shared_key, apply_shift as dh_shift, remove_shift as dh_unshift
from Bruteforce import decode as brute_force

dh_base = 8
dh_mod = 29
dh_private_key = 49
dh_public_key = dh_base ** dh_private_key % dh_mod


def main():
    print("Hello parents!")
    print("Welcome to my Cryptography Package, cryptoIO!!")
    print("Here you can encrypt messages and save them for others to read.")
    print("But they will only be able to decrypt them if you (remember and) share the secret keys!")
    print("I hope you will enjoy!")

    while True:
        print()
        choice = int(input("Type 1 to encrypt, 2 to decrypt, 3 to see colors, 4 for ascii art, or 0 to quit: "))

        if choice == 1:
            encrypt()
        elif choice == 2:
            decrypt()
        elif choice == 3:
            numbers = [0x69, 0x44, 0x54, 0x65, 0x63, 0x68]
            text = ""
            for i in numbers:
                text += chr(i)
            for c in text:
                N = ord(c)

            csi = "\x1b["
            color = "34m"
            colored_text = csi + color + text
            print(colored_text)

            escape = "\x1b["
            color = "31m"
            colored_text = escape + color + text
            print(colored_text)

            cool = "\x1b["
            color = "41m"
            colored_text = cool + color + text
            print(colored_text)
        elif choice == 4:
            print("""MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0kdl:;,,'''...........'',,;:clxOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMWXOdc;''',;:coddxxxkkkkkkkxxxddolc:;'''';cdOXWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWXOo:'..  .':oxkOOOOOOOOOOkkkkkkkkkkkkkkkxdl:'...;oOXWMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWKxc,',:oxxdol:;,',;cdkOOOOOOOOOkkkkkkkkkkkkkkkkxo:.   .:xKWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMXkc'.;lxOOOOOOOOOOOxo:,',:oxOOOOOOOOkkkkkkkkkkkkkkkkkdc'. ...:xXWMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMW0o,.,lxO000000000OOOO0OOOxl;'';lxOOOOOOkOkkkkkkkkkkkkkkkxxl'.';'.'l0WMMMMMMMMMMMMMMM
MMMMMMMMMMMMMW0c.':xO00000000000000000000OOOko;'';cokOOOOOOkkkkkkkkkkkkkkxxd:..cl;..:OWMMMMMMMMMMMMM
MMMMMMMMMMMW0c.'lk00000000000000000000000000OOOxl;'.'cdkOOOOkkkkkkkkkkkkkkxkxl'.:dd:..:OWMMMMMMMMMMM
MMMMMMMMMMKl..ckO00000000000000000000000000000OOOOkxc'.;lxOOOOkkkkkkkkkkkkkkxxo,.;dxd:..cKWMMMMMMMMM
MMMMMMMMNx'.:xOOO000000000000000000000000000000OO0OOOko;'':dkOOkkkkkkkkkkkkkkkkd,.;dxxo;.'xNMMMMMMMM
MMMMMMMKc.'oOOO000000000000000000000000000000000O00OOOOOxc,.,cxkkkkkkkkkkkkkkxxxo'.:xxxdl'.:KMMMMMMM
MMMMMW0,.:xOOOO00000000000000000KKK000000000000000OOOOOOOOko:'';oxkkkkkkkkkkkkkxxl..lxxxxo;.,OWMMMMM
MMMMWk'.ckOOOOOO000000000000000KKKKKK000000000000000OOOOOOOOOxl;.':oxkkkkkkkkkkkxx:.,dxxxxd:..xWMMMM
MMMWk'.lkOOOOOOOO00000000000000KKKKKKK00000000000000OOOOOOOOOOOkdc,'';cdxkkkkkkkxxo'.lxxxxxdc..xWMMM
MMWk'.lkOOOOOOOOOO0000000000000000KKK00000000000000000OOOOOOOOOOOOkxl;''';codxkkkxx:.;dxxdlc;. .xWMM
MM0,.ckOOOOOOOOOOOO00000000000000000000000000000000000OOOOOOOOOOOOOOOkxdc;,''',;;;:' .,,'''',:;.'OMM
MX:.;kOOOOOOOOOOOOOOO00000000000000000000000000000000OOOOOOOOOOOOOOOkkkkkkkxolc:;;,,. ':clodxxd;.;KM
Wd.'dkkkOOOOOkkkxxdddoooooooooodddxxkkkOOO00000000000OOOOOOOOOOOOOOOkkkkkkkkkkkkkkxd,.:xxxxxxxxo'.oN
0,.ckkkdoc:;,,,,,,,,,,,,,,,,,,,,,,,,,,,,,;;;;::clloodxxkOOOOOOOOOOOOkkkkkkkkkkkkkkxx;.;xxxxxxxxxc.'O
d.'ol;,'',;:clodxxkkkOOOOOOOOOOOOOOkkkxxddollc::;;,,,,,,,,;::clodxkkkkkkkkkkkkkkkkkx;.;xxxxxxxxxd,.l
; ...;cdxkkkOOOOOOOOOOOOOOOOOOOO0000000000000000OOOOkkxdolc:;;,,,',,;:clodxkkkkkkkkx;.;xxxxxxxxxxc.,
. .cdkkkkkkkkkkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOkkxdol:;,,''',;:cldxxx;.:xxxxxxxxxxl..
 .oxkkkkkkkkkkkkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOkkkkxdoc:;,''',,..;dxxxxxxxxxo' 
 ,xxkkkkkkkkkkkkkkkkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOkkkkkkkkkkkkkxxdlc,. .',;codxxxxd, 
 ,xxkkkkkkkkkkkkkkkkkkkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOkkkkkkkkkkkkkkkkkkkl..ll:,'.',:ldd; 
 ,xxxxxkkkkkkkkkkkkkkkkkkkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOkkkkkkkkkkkkkkkkkkkkxx;.;xxxxdoc;'.';' 
 ,dxxxxxxkkkkkkkkkkkkkkkkkkkkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOkkkkkkkkkkkkkkkkkkkkkkko'.cxxxxxxxxdl;.  
..oxxxxxxxxxxkkkkkkkkkkkkkkkkkkkkkkkOOOOOOOOOOOOOOOOOOOOOkkkkkkkkkkkkkkkkkkkkkkkkxc.'dxxxxxxxxxxdl. 
'.cxxxxxxxxxxxkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxxxdddddxxxd'.cxxxxxxxxxxxxc..
c.;dxxxxxxxxxxxxxkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxolc:;,,'''''''',,'.'dxxxxxxxxxxxd;.:
k..lxxxxxxxxxxxxxxxxkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxol:;,''',;:cloooddoolc'  .;oxxxxxxxxxdl..x
Nc.,dxxxxxxxxxxxxxxxxxxkkkkkkkkkkkkkkkkkkkkkkkkkkkkxdoc;,''',:codxkkkkkkkxxxxxxd,.,;..:dxxxxxddd;.:X
MO'.cdxxxxxxxxxxxxxxxxxxxxxxxkkkkkkkkkkkkkkkkxdoc;,,''';cldxkkkkkkkkkkkkxxxxxxx:.,oxo,.,oxxxxddc..kM
MWd..lddxxxxxxxxxxxxxxxxxxxxxxxxkkkkkkkkxdl:;''',;:codxkkkkkkkkkkkkxxxxxxxxxxxc..lxxxd;.,oxxxdl'.oWM
MMNl.'odddddxxxxxxxxxxxxxxxxxxxxxkxdoc:,''',;codxkkkkkkkkkxxxxxxxxxxxxxxxxxxxl..cxxxxxo'.:dxdo,.cXMM
MMMXc.'odddddxxxxxxxxxxxxxxxxdoc:;,''',:codxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxl..cxxxxxxxc..ldo,.:KMMM
MMMMXc.'ldddddxddddddolcc:;,'''',;:lodxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxc..cdxxxxxxxo,.:o,.:KMMMM
MMMMMNo..'',,,,,,'''''''',;:clodxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdc..cxxxxxxdddd:....lXMMMMM
MMMMMMNx. .,;;;:::ccloodddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxd;.'ldxxxdddddddc. .dNMMMMMM
MMMMMMMW0;.'lddxddddxxxdddddddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxl'.,oxdddddddxddl'.,OWMMMMMMM
MMMMMMMMMXd'.;odddddddddddddddddddddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdxxxd:..:dxxddddddddo;..oXMMMMMMMMM
MMMMMMMMMMWKl..:oddddddddddddddddddddddddddddxxxxxxxxxxxxxxxxxddddxdl'.,lddddddddddo:..c0WMMMMMMMMMM
MMMMMMMMMMMMW0c..;odddddddddddddddddddddddddddddddddddddddddddddddl,..cddddddddddo:..cOWMMMMMMMMMMMM
MMMMMMMMMMMMMMW0l'.,codddddddddddddddxddddddddddddddddddddddddddl;..:odddddddddc,.'l0WMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWKd;..;coddddddddddddddddddddddddddddddddddddoc,.':oddddddddl;..;dKWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMW0o;..,:odddddddddddddddddddddddddddddddl;'.,coddddxdoc,..,oONMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMN0d:'.',:loddddddddddddddddddddxdoc;'.':ldxdddl:;'.':d0NMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMWXOd:,'.',;clodddddxdddoolc:,'..,:loolc:,'.',:okXWMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKkdc;,''''',,,,'...    ..',''''',;cok0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0xoc;'..          ...,:ox0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM""")
        elif choice == 0:
            print("Thank you for using cryptoIO!")
            print("Bye!")
            break
        else:
            print("Sorry, '{}' is not a valid choice. Pick 1, 2, 3, 4, or 0.".format(choice))
            continue


def encrypt():
    print("Preparing to encrypt...")
    data = get_encrypt_input()

    while True:
        file_name = input("Please enter your message's name: ").strip()
        if "{}".format(file_name) in os.listdir("msgs"):
            print("Sorry, there is already a secret message with that name. Choose another.")
        else:
            break

    while True:
        cypher = input(
            "1   : Ceaser (shift) Cypher\n2   : Block Cypher\n3   : Diffie-Hellman Cypher\nPlease select a cypher (1, 2, or 3): ")

        try:
            cypher = int(cypher)
        except ValueError:
            print("Sorry, {} is not a valid choice. Pick 1, 2, 3, 4, or 0.".format(cypher))

        if cypher == 1:
            encrypted = shift_cypher(data[0], data[1])
            break
        elif cypher == 2:
            chunk_list = block_pad(data[0])
            encrypted = block_shift(chunk_list, data[1])
            encrypted = "\n".join(str(s) for s in encrypted)
            break
        elif cypher == 3:
            msg_public_key = dh_base ** data[1] % dh_mod
            shared_key = dh_shared_key(dh_private_key, msg_public_key)
            encrypted = dh_shift(data[0], shared_key)
            break
        elif cypher == 0:
            return

    with io.open("msgs/{}.txt".format(file_name), 'w+', encoding="utf-8") as file:
        file.write(encrypted)
    print("Your message was successfully encrypted!\n")


def get_encrypt_input():
    msg = input("Please enter your secret message: ")
    key = get_key()
    return msg, key


def decrypt():
    print("Preparing to decrypt...")
    data = get_decrypt_input()

    while True:
        cypher = input(
            "1   : Ceaser (shift) Cypher\n2   : Block Cypher\n3   : Diffie-Hellman Cypher\nPlease select a cypher (1, 2, or 3): ")

        try:
            cypher = int(cypher)
        except ValueError:
            print("Sorry, {} is not a valid choice. Pick 1, 2, or 3.".format(cypher))

        if cypher == 1:
            decrypted = shift_cypher(data[0], -data[1])
            break
        elif cypher == 2:
            chunk_list = list(map(int, data[0].split("\n")))
            chunk_list = block_unshift(chunk_list, data[1])
            decrypted = block_rebuild(chunk_list)
            break
        elif cypher == 3:
            shared_key = dh_shared_key(data[1], dh_public_key)
            decrypted = dh_unshift(data[0], shared_key)
            break77
        elif cypher == 9:
            decrypted = brute_force(data[0])

        elif cypher == 0:
            return

    print("The decrypted message is:\n'{}'".format(decrypted))

    return


def get_decrypt_input():
    localMsgs = os.listdir("msgs")
    for i in range(len(localMsgs)):
        n = i + 1  # '0' is the choice for manual input, so we offset the count by +1
        padding = " "
        if n <= 99:
            padding += " "
        if n <= 9:
            padding += " "
        print("{}{}: {}".format(n, padding, localMsgs[i]))
    print()

    while True:
        choice = input("Please choose a message from above to decrypt (or, type 0 for manual entry): ")

        try:
            choice = int(choice)
        except ValueError:
            print("Sorry, {} is not a valid choice. Pick between 0 and {}.".format(choice, len(localMsgs)))
            continue

        if choice == 0:
            msg = input("Manually enter the encrypted message: ").strip()
            break
        elif choice <= len(localMsgs):
            with io.open("msgs/{}".format(localMsgs[choice - 1]), 'r', encoding="utf-8") as file:
                msg = file.read()
            break
        else:
            print("Sorry, {} is not a valid choice. Pick between 0 and {}.".format(choice, len(localMsgs)))

    key = get_key()
    return msg, key


def get_key():
    while True:
        try:
            key = int(input("Please enter your secret key: "))
            break
        except ValueError:
            print("The secret key should be a number. Try again. ")
    return key


# This line automatically runs the main def when you start the program.
if __name__ == "__main__":
    main()
