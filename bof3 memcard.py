memcard = open(input("memory card name: "), "r+b")

def tl(x):
    low = x & 0xff
    high = (x & 0xff00) >> 8
    return bytes([low, high])

for i in range(3):
    memcard.seek(0x2000 * (i + 1) + 0x270)
    memcard.write(b'\x00\x00')
    memcard.seek(0x2000 * (i + 1) + 0x200)
    save_content = memcard.read(0x1e00)
    chksum = sum(save_content)
    memcard.seek(0x2000 * (i + 1) + 0x270)
    memcard.write(tl(chksum))
    print(tl(chksum))
    
memcard.close()
    
