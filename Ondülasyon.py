f = open("raw.txt", "r")
gs = f.readlines()
x = (gs [9::9])
x.pop()
ond = input("What is ondulation?" '\n')
for line in x:
    line = line.replace("GS,","")
    line = line.replace("PN","")
    line = line.replace("N ","")
    line = line.replace("E ","")
    line = line.replace("EL","")
    line = line.split(",")
    print(line[0], line[1], line[2], format(float(line[3]) - float(ond),'.6f'),)



