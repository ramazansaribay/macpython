f = open("raw.txt", "r") 
for line in f:
        if line.startswith("GS"):
            line = line.replace("GS,PN","")
            line = line.replace("EL","")
            line = line.replace("E ","")
            line = line.replace("N ","")
            print(line, end='\b')
