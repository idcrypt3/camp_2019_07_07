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
    number=characters.find(character.lower())+1
    if number==0:
        number=64
    return number
def loop(value,min=1,max=64):
    range=max-min+1
    while value<min:
        value+=range
    while value>max:
        value-=range
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
    decimal=int(format)
    return decimal+1
characters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ."
#message=input("Message:\n")
#key=input("\nKey:\n")
print(decm("111111"))