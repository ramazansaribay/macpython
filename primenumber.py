num = 101
liste = []
for a in range(2, num+1):
    for b in range(2, a):
        if (a % b) == 0:
            break
    else :
            liste.append(a)
print(liste)