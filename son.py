from decimal import Decimal
ond = input("What is ondulation?"'\n')
f = open("raw.txt", "r")                        
gs = f.readlines()
x = (gs[9],gs[27],gs[45],gs[63],gs[81],gs[99],gs[117],  # There are some specific lines which I need
gs[135],gs[153],gs[171],gs[189],gs[207],gs[225],gs[243],gs[261])
for line in x:
        if line.startswith("GS"):
            line = line.replace("GS,PN","")
            line = line.replace("E ","")
            line = line.replace("N ","")
            degerlerim = line.split(",")
        for deger in degerlerim:
            if deger.startswith("EL"):
                d = float(deger.replace("EL","")) - float(ond)
                print (line, format(d,'.6f'))  # format ve '.6f' noktadan sonra kaç hane geleceğini göstermeme yarıyor.