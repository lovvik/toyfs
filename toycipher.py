#key = (12, 5)

key = (0,9)
sbox = [0xc,5,6,0xb,9,0,0xa,0xd,3,0xe,0xf,8,4,7,1,2]

IV = 5
#IV must be < 16

def round (block, tour) :
    if(block>15) :  raise ValueError("runs on 4 bits")
    x = block ^ key[tour%2]
    x = sbox[x]
    return x

def back_round(encblock, tour) :
    if(encblock>15) : raise ValueError("runs on 4 bits")
    x = sbox.index(encblock)
    x = x ^ key[tour%2]
    
    
    return x
    


def enc(message) :

    enc = []
    for i in range(len(message)) :
        enc.append(round(message[i], i))
    
    return enc


def dec (encmessage) :
    msg = []
    for i in range(len(encmessage)) :
        msg.append(back_round(encmessage[i],i))
    
    return msg


def enc_byte(char) :
    if(char>255) :  raise ValueError("runs on a byte")
    ms = round(char // 16, 0)*16
    ls =round(char%16, 1)
    return ms+ls


def dec_byte(char) :
    if(char>255) :  raise ValueError("runs on a byte")
    ms = back_round(char // 16, 0)*16
    ls = back_round( char%16, 1)
    return ms+ls





def enc_ba(ba:bytearray) :
    re = bytearray()
    for i in range(len(ba)) :
        re.append(enc_byte(ba[i]))
    return re
    
def dec_ba(ba:bytearray) :
    re = bytearray()
    for i in range(len(ba)) :
        re.append(dec_byte(ba[i]))
    return re





def enc_file(filepath) :
    with open(filepath,'rb') as fichier, open(filepath+".enc", 'wb') as enc_f :
        octets = fichier.read(-1)
        
        enc_f.write(enc_ba(bytearray(octets)))
        
            


        #enc_f.write(octets)


def dec_file(filepath) :

    with open(filepath,'rb') as fichier, open(filepath.replace(".enc",".dec"), 'wb') as dec_f :
        octets = fichier.read(-1)

        dec_f.write(dec_ba(bytearray(octets)))



def enc_cbc_ba(ba:bytearray) :
    prev = IV
    
    re = bytearray()
    
    for i in range(len(ba)) :
        re.append(enc_byte(ba[i]^prev))
        prev = re[i]
    return re
    
def dec_cbc_ba(ba:bytearray) :
    temp = bytearray()
    
    for i in range(-1, -len(ba)-1, -1) :
        if(i==-len(ba)) : 
            prev = IV
        else :
            prev = ba[i-1]
        temp.append(dec_byte(ba[i])^prev)

    temp.reverse()
    return temp

def enc_cbc_file(filepath) :
    with open(filepath,'rb') as fichier, open(filepath+".enc", 'wb') as enc_f :
        octets = fichier.read(-1)
        
        enc_f.write(enc_cbc_ba(bytearray(octets)))


def dec_cbc_file(filepath) :

    with open(filepath,'rb') as fichier, open(filepath.replace(".enc",".dec"), 'wb') as dec_f :
        octets = fichier.read(-1)

        dec_f.write(dec_cbc_ba(bytearray(octets)))

    

        
if(__name__ == '__main__') : 
    enc_cbc_file("img.png")
    dec_cbc_file("img.png.enc")
