def xor(x, y) : 
    return x ^ y 
    
def powsum1(y) : 
    sum = 0 
    for i in range(0, y) : 
        sum += pow(2, i) 
    return sum 
def powsum2(y) : 
    sum = 0 
    for i in range(8 - y, 8) : 
        sum += pow(2, i) 
    return sum 

def bit1(x, y) : 
    y = y % 8 
    ps = powsum1(y) 
    ps = (x & ps) << (8 - y) 
    return ps + (x >> y) 

def bit2(x, y) : 
    y = y % 8 
    ps = powsum2(y) 
    ps = (x & ps) >> (8 - y) 
    return (ps + (x << y)) & 0x00ff 
    
def bit(x, y) : 
    return bit2(x, y) 

def encrypt(salt, key) : 
    pwd = '' 
    key_len = len(key) 
    if key_len > 0 : 
        for i, c in enumerate(salt) : 
            x = ord(c) 
            y = ord(key[i % key_len]) 
            if i > 0 and ord(pwd[i - 1]) % 2 != 0 : 
                y = y % 8 
                z = bit(x, y) 
            else : 
                z = xor(x, y) 
            pwd += chr(z)
    return pwd 
    
def check(key, pwd) : 
    checksum = 0
    for c in pwd : 
        checksum += ord(c)
    flag = (checksum == 8932) 
    if flag : 
        pass
    print('%s(%i): \n\tkey=%s\n\tpwd=%s' % ('Bingo' if flag else 'Fail', checksum, key, pwd)) 
    return flag 

if __name__ == '__main__' : 
    salt = "\x71\x11\x24\x59\x8d\x6d\x71\x11\x35\x16\x8c\x6d\x71\x0d\x39\x47\x1f\x36\xf1\x2f\x39\x36\x8e\x3c\x4b\x39\x35\x12\x87\x7c\xa3\x10\x74\x58\x16\xc7\x71\x56\x68\x51\x2c\x8c\x73\x45\x32\x5b\x8c\x2a\xf1\x2f\x3f\x57\x6e\x04\x3d\x16\x75\x67\x16\x4f\x6d\x1c\x6e\x40\x01\x36\x93\x59\x33\x56\x04\x3e\x7b\x3a\x70\x50\x16\x04\x3d\x18\x73\x37\xac\x24\xe1\x56\x62\x5b\x8c\x2a\xf1\x45\x7f\x86\x07\x3e\x63\x47"
    key = "MyP4sS"
    pwd = encrypt(salt, key) 
    check(key, pwd)