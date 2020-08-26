ond = input("What is ondulation?")
f = open("raw.txt", "r")
mylines = f.readlines()
for line in mylines:
    if line.startswith("GS"):
        line.replace("GS,","")
        line.replace("N ","")
        line.replace("E","")
        degerlerim = line.split(",")
        for deger in degerlerim:
            if deger.startswith("EL"):
                d = float(deger.replace("EL","")) - float(ond)
                print (line + str(d))