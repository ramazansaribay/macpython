f = open("raw.txt", "r")
gs = f.readlines()
x = (gs [9::18])
for line in x:
    if line.startswith("GS"):
            line = line.replace("GS,PN","")
            line = line.replace(",N ","\t")
            line = line.replace(",E ","\t")
            line = line.replace(",EL","\t")
            print(line)
