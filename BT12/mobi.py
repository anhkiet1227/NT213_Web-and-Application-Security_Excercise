# main function
if __name__ == '__main__':
    
    # declare variable
    string = "QflMn`fH,ZHVW^7c"
    flag = ""
    
    # loop through string
    for i, char in enumerate(string):
        
        # convert char to ascii
        tmp = ord(char)
        
        # check if i is less than 8
        if i < 8:
            
            # tmp minus 3
            tmp -= 3
            
        # add char to flag
        flag += chr(tmp+i)
        
    # print flag
    print(flag)
