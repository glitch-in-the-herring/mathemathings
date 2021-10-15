import codecs

a = codecs.open("hiragana.txt", "r", "utf-8")
b = codecs.open("katakana.txt", "r", "utf-8")
c = codecs.open("kanji.txt", "r", "utf-8")

d = codecs.open("htable.txt", "w", "utf-8")
e = codecs.open("ktable.txt", "w", "utf-8")
f = codecs.open("kanjitable.txt", "w", "utf-8")

hi = 0x5e
ka = 0xae
kj = 0x1200

while len(x := a.readline()) > 0:
    d.write("    0x{:x}            {}\n".format(hi, x[0:-2]))
    hi += 1

while len(x := b.readline()) > 0:
    e.write("    0x{:x}            {}\n".format(ka, x[0:-2]))
    ka += 1

while len(x := c.readline()) > 0:
    f.write("    0x{:x}          {}\n".format(kj, x[0:-2]))
    kj += 1
    
a.close()
b.close()
c.close()
d.close()
e.close()
f.close()
