with open("mars.txt", "r", encoding="utf-8") as f:
    liste = f.readlines()
counter = 0
with open("kita.txt", "w", encoding="utf-8") as f:
    for i in liste:
        counter += 1
        if counter %4 == 0:
            f.write(i + "\n")
        else:
            f.write(i)

with open("kita.txt", "r", encoding="utf-8") as f:
    print(f.read())


    
    
    
    




    
    
