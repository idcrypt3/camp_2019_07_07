import os, io, shutil

# uncomment the 3 lines below and replace the names of your files (do not include .py) and function defs
# leave "as name" as-is; this renames your functions so they are all compatible with this program,
# regardless of what you named them
from Ceaser_Cipher import shift_cipher as shift_cypher
from Block_Cipher import pad_message as block_pad, rebuild_message as block_rebuild
from Block_Cipher import apply_shift as block_shift, undo_shift as block_unshift
from Diffie_Hellman import find_shared_key as dh_shared_key, apply_shift as dh_shift, remove_shift as dh_unshift

# here I set the private key used in Diffie-Hellman encryptions. Feel free to change it.
# the public_base is set to 8 and public_modulus 29, as on GamePlan. You can change those too.
dh_base = 8
dh_mod = 29
dh_private_key = 49
dh_public_key = dh_base ** dh_private_key % dh_mod

#End print in color
def end_color():
    print("\033[0m")

def prRed (skk, end = "\n"):
    print("\033[1;31;00m{}".format(skk), end=end)
def prGreen (skk, end = "\n"):
    print("\033[1;32;00m{}".format(skk), end=end)
def prYellow (skk, end = "\n"):
    print("\033[1;33;00m{}".format(skk), end=end)
def prBlue(skk, end = "\n"):
    print("\033[1;34;00m{}".format(skk), end=end)
def prPurple(skk, end = "\n"):
    print("\033[1;35;00m{}".format(skk), end=end)
def prCyan(skk, end = "\n"):
    print("\033[1;36;00m{}".format(skk), end=end)
def prw(skk, end = "\n"):
    print("\033[1;17;00m{}".format(skk), end=end)
def prBlack(skk, end = "\n"):
    print("\033[1;90;47m{}".format(skk), end="")

def main():
    # Feel free to change this intro msg to whatever you want
    prw("Hello parents and staff! ", end = '')
    prw("Welcome to the", end = '')
    prCyan(" iD", end = '')
    prw(" Cryptography Package, cryptoIO!!")
    print("Here you can\033[1;36;00m encrypt\033[1;17;00m messages and save them for others to read.")
    print("But they will only be able to\033[1;36;00m decrypt\033[1;17;00m them if you (remember and) share the\033[1;36;00m secret keys\033[1;17;00m!")

    # infinite loop runs until the user quits
    while True:
        print() # newline for readability
        choice = input("Type 1 to\033[1;36;00m encrypt\033[1;17;00m, 2 to\033[1;36;00m decrypt\033[1;17;00m, or 0 to\033[1;31;00m quit\033[1;17;00m: ")
        if choice.strip() == "Clear cache":
            for filename in os.listdir("msgs"):
                filepath = os.path.join("msgs", filename)
                try:
                    shutil.rmtree(filepath)
                except OSError:
                    os.remove(filepath)
            continue
        if choice == "Clear Aiden05":
            print("Cyrus is gay!")
            continue
        try:
            choice = int(choice)
        except ValueError:
            print("Sorry, \"{}\" is\033[1;31;00m not a valid\033[1;17;00m choice. Pick 0, 1, or 2.".format(choice))
            continue

        if choice == 1:
            print("Preparing to\033[1;36;00m encrypt\033[1;17;00m...")
            encrypt()
        elif choice == 2:
            if len(os.listdir("msgs")) == 0:
                print("Sorry, there are\033[1;31;00m 0\033[1;17;00m messages to\033[1;36;00m decrypt\033[1;17;00m. Try\033[1;36;00m encrypting\033[1;17;00m a\033[1;36;00m secret message\033[1;17;00m first.")
                encrypt()
            else:
                decrypt()
        elif choice == 0:
            print("Thank you for using\033[1;36;00m iD\033[1;17;00m Tech cryptoIO!")
            print("Have a good\033[1;33;00m summer\033[1;17;00m!")
            break
        else:
            print("Sorry, '{}' is\033[1;31;00m not a valid\033[1;17;00m choice. Pick 1, 2, or 0.".format(choice))
            continue

def encrypt():
    data = get_encrypt_input()

    while True:
        file_name = input("Please enter your\033[1;36;00m message's name\033[1;17;00m: ").strip()
        if "{}.txt".format(file_name) in os.listdir("msgs"):
            print("Sorry, that name is\033[1;31;00m already taken\033[1;17;00m. Please choose another.")
        else:
            break

    while True:
        cypher = input(
            "1   : Ceaser (shift) Cipher\n2   : Block Cipher\n3   : Diffie-Hellman Cipher\nPlease select a\033[1;36;00m cipher\033[1;17;00m (1, 2, or 3) or 0 to\033[1;31;00m quit\033[1;17;00m: ")

        try:
            cypher = int(cypher)
        except ValueError:
            print("Sorry, \"{}\" is\033[1;31;00m not a valid\033[1;17;00m choice. Pick 1, 2, or 3.".format(cypher))
            continue

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
        elif cypher > 3 or cypher < 0:
            print("Sorry, \"{}\" is\033[1;31;00m not a valid\033[1;17;00m choice. Pick 1, 2, or 3.".format(cypher))

    with io.open("msgs/{}.txt".format(file_name), 'w+', encoding="utf-8") as file:
        file.write(encrypted)
    print("Your message was successfully\033[1;36;00m encrypted\033[1;17;00m!\n")

def get_encrypt_input():
    msg = input("Please enter your\033[1;36;00m secret message\033[1;17;00m: ")
    key = get_key()
    return msg, key

def decrypt():
    print("Preparing to\033[1;36;00m decrypt\033[1;17;00m...")
    data = get_decrypt_input()

    while True:
        cypher = input(
            "1   : Ceaser (shift) Cipher\n2   : Block Cipher\n3   : Diffie-Hellman Cipher\nPlease select a\033[1;36;00m cipher\033[1;17;00m (1, 2, or 3) or 0 to\033[1;31;00m quit\033[1;17;00m: ")
        try:
            cypher = int(cypher)
        except ValueError:
            print("Sorry, \"{}\" is\033[1;31;00m not a valid\033[1;17;00m choice. Pick 1, 2, or 3.".format(cypher))
            continue
        if cypher == 1:
            decrypted = shift_cypher(data[0], -data[1])
            break
        elif cypher == 2:
            try:
                chunk_list = list(map(int, data[0].split("\n")))
                chunk_list = block_unshift(chunk_list, data[1])
                decrypted = block_rebuild(chunk_list)
            except:
                decrypted = "Sorry,\033[1;31;00m unable\033[1;17;00m to decrypt message."
            break
        elif cypher == 3:
            shared_key = dh_shared_key(data[1], dh_public_key)
            decrypted = dh_unshift(data[0], shared_key)
            break
        elif cypher == 0:
            return
        elif cypher == int(cypher) and cypher > 3 or cypher < 0:
            print("Sorry, \"{}\" is\033[1;31;00m not a valid\033[1;17;00m choice. Pick 1, 2, or 3.".format(cypher))

    print("The decrypted message is:\n'{}'".format(decrypted))

    return

def get_decrypt_input():
    localMsgs = os.listdir("msgs")
    for i in range(len(localMsgs)):
        n = i + 1   # '0' is the choice for manual input, so we offset the count by +1
        padding = " "
        if n <= 99:
            padding += " "
        if n <= 9:
            padding += " "
        print("{}{}: {}".format(n, padding, localMsgs[i]))
    print()

    while True:
        choice = input("Please choose a message from above to\033[1;36;00m decrypt\033[1;17;00m (or, type 0 for manual entry): ")

        try:
            choice = int(choice)
        except ValueError:


            print("Sorry, \"{}\" is\033[1;31;00m not a valid\033[1;17;00m choice. Pick between 0 and {}.".format(choice, len(localMsgs)))
            continue

        if choice == 0:
            msg = input("Manually enter the\033[1;36;00m encrypted message\033[1;17;00m: ").strip()
            break
        elif choice <= len(localMsgs):
            with io.open("msgs/{}".format(localMsgs[choice - 1]), 'r', encoding="utf-8") as file:
                msg = file.read()
            break
        else:
            print("Sorry, \"{}\" is\033[1;31;00m not a valid\033[1;17;00m choice. Pick between 0 and {}.".format(choice, len(localMsgs)))

    key = get_key()
    return msg, key

def get_key():
    while True:
        try:
            key = int(input("Please enter your\033[1;36;00m secret key\033[1;17;00m: "))
            break
        except ValueError:
            print("The\033[1;36;00m secret key\033[1;17;00m should be a number. Try again. ")
    return key

# This line automatically runs the main def when you start the program.
if __name__ == "__main__":
    main()

# Ideas for new features:
# - Include your name or contact info in the comments and/or opening scroll.
# - Write some messages or stories and encrypt and save them to disk for your family and friends to discover.
# - Include color codes - red for failed encryption, green for passed (see the lesson Hexadecimal\Character Codes).
# - This program includes functionality you haven't seen in the form of file I/O, string formatting, and imported
# modules. See if you understand what's going on and reference the online documentation if you don't.
# - Errors are handled, but the user navigation could be more friendly (e.g. allowing users to return to a previous menu
# rather than forcing them to stick with the choice to encrypt or decrypt, even if they change their mind). Try expand-
# ing it!
# Prevent the user from attempting a Ceaser shift greater than +-26, or use mod (%) to correct it

# Advanced features:
# - Create a puzzle for users to solve by slowly ramping up the difficulty (e.g., the key to a block cypher could be
# written in a ceaser cypher (as a word - remember, our ceaser cypher only substitutes letters), and that block cypher
# could have a clue to a Diffie-Hellman cypher, and...)
# - Display the checksum or hash of messages as they are encrypted and decrypted.
# You could even save the checksum/hash alongside the messages, so users know if a file has been modified.
# - Expand your cyphers with more options, or write a new one from internet tutorials.

