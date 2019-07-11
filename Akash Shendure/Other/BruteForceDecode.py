from CaesarCipher import cipher


def main():
    print("Message: ")
    message = input()
    print("\nPossible decoded messages:")
    for shift in range(0, 26):
        decodedMessage = cipher(message, shift)
        print(decodedMessage)


if __name__ == "__main__":
    main()
