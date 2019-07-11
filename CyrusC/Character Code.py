numbers = [0x69, 0x44, 0x54, 0x65, 0x63, 0x68]
text = ""
for i in numbers:
    text += chr(i)
print(text)
for c in text:
    N = ord(c)
print (hex(N))

csi = "\x1b["
color = "34m"
colored_text = csi + color + text
print (colored_text)

escape = "\x1b["
color = "31m"
colored_text = escape + color + text
print(colored_text)

cool = "\x1b["
color = "41m"
colored_text = cool + color + text
print(colored_text)
