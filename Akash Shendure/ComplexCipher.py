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
    if character=="{":
        character="["
    if character=="}":
        character="]"
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
def ctxt(text):
    binr=[]
    for letter in text:
        decimal=numb(letter)-1
        binary=format(decimal,"#80b")
        binr.append(binary)
    print(binr)
def cbin(binr):
    print()
#characters="""5t'.g:0~&<p-(!fi@koy]ul1+9w_=[^,nh%vsbm2>j4ra/?zx7#"e3$;6d)c8*q """
#message=input("Message:\n")
#key=input("\nKey:\n")

#ctxt("5 oingosfnrpinf")

format(decimal,"#80b")