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
characters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ."
message=input("Message:\n")
key=input("\nKey:\n")
while len(key)<4:
    print("Key must be more than 3 characters long.")
    key = input("\nKey:\n")
print()
message=tlst(message,keyc(key))
print(message)
print(keys(key,len(message)))
message=flst(message,keyc(key))
print(message)