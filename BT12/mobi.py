string = "QflMn`fH,ZHVW^7c"
flag = ""
for i, char in enumerate(string):
    tmp = ord(char)
    if i < 8:
        tmp -= 3
    flag += chr(tmp+i)
print(flag)
