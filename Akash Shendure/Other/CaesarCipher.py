def binaryQuestion(question,answer1,answer2):
    print(question)
    print(" 1) "+answer1)
    print(" 2) "+answer2)
    answer=input("Answer: ")
    while answer!="1" and answer!="2":
        print("Please answer with 1 or 2.")
        print(question)
        print(" 1) " + answer1)
        print(" 2) " + answer2)
        answer = input("Answer: ")
    return int(answer)

def cipher(message,shift):
    shiftedMessage=""
    originalLower="abcdefghijklmnopqrstuvwxyz"
    originalUpper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    original=originalLower+originalUpper
    startLower=originalLower[shift:]
    endLower=originalLower[:shift]
    shiftedLower=startLower+endLower
    startUpper = originalUpper[shift:]
    endUpper = originalUpper[:shift]
    shiftedUpper = startUpper + endUpper
    shifted=shiftedLower+shiftedUpper
    for letterIndex in range(0,len(message)):
        letter=message[letterIndex]
        alphabetIndex=original.find(letter)
        if alphabetIndex==-1:
            shiftedMessage+=letter
        else:
            shiftedLetter=shifted[alphabetIndex]
            shiftedMessage+=shiftedLetter
    return shiftedMessage

def main():
    encodeOrDecode=binaryQuestion("Would you like to endcode or decode text?","Encode","Decode")
    print("Message: ")
    message=input()
    invalidShift=True
    while invalidShift:
        shift=input("Shift: ")
        invalidShift=False
        try:
            shift=int(shift)
        except:
            print("Invalid shift. Please enter an integer.")
            invalidShift=True
    if encodeOrDecode==2:
        shift*=-1
    while shift<=0:
        shift+=26
    while shift>26:
        shift-=26
    message = cipher(message, shift)
    if encodeOrDecode==1:
        print("\nEncoded message:")
    else:
        print("\nDecoded message:")
    print(message)

if __name__ == "__main__":
    main()