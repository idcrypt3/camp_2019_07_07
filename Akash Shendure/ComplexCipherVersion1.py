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
    shifted=number+shift
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
def tlst(text):
    list=[]
    for letter in text:
        list.append(binr(numb(letter)))
    return list
def flst(list):
    text=""
    for index in list:
        text+=char(decm(index))
    return text
def keyf(key):
    shift=""
    for fragment in tlst(key):
        shift+=fragment
    return int(shift)%64
characters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ."
#message=input("Message:\n")
key=input("\nKey:\n")
print(keyf(key))