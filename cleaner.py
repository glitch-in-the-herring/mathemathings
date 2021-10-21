filename = input()
file = open(filename, "r")
file2 = open(filename + "_cleaned", "w")

while len(x := file.readline()) > 0:
    file2.write(''.join([i for i in ' '.join(x.split()[1:]) if i != '\0']) + '\n')

file.close()
file2.close()
