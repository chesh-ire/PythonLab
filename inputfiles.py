
ipfile = open("input.txt", 'r')
lines = ipfile.readlines()
ipfile.close()


oddlines = lines[::2]


opfile = open("output.txt", 'w')
for line in oddlines:
    opfile.write(line)
opfile.close()
