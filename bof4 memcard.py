memcard = open(input("memory card name: "), "r+b")

def c(x):
    s = 0
    for i in x:
        s ^= i
    return s

for i in range(3):
    memcard.seek(0x2000 * i)
    save_content = memcard.read(0x184f)
    chksum = c(save_content)
    memcard.seek(0x2000 * i + 0x184f)
    memcard.write(bytes([chksum]))
    print("{:x}".format(chksum))
    
memcard.close()
