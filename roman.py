def exit():
    global z, i
    if z == "exit":
        print('"Exiting the program... Good Bye"')
        i = False
    return i
def roma(rakam, a, b = "V", c = "X"):
    if rakam < 4:
        return rakam * a
    elif rakam == 4:
        return a + b
    elif rakam == 5:
        return b
    elif rakam < 9:
        return b + (rakam - 5) * a
    elif rakam == 9:
        return a + c
    else:
        pass
print ('###  This program converts decimal numbers to Roman Numerals ###\n(To exit the program, please type "exit")')
i = True
z = input ("Please enter a number between 1 and 3999, inclusively :")
exit()
while i:
    while not z.isdigit():
        print('"Not Valid Input!!!"')
        z = input ("Please enter a number between 1 and 3999, inclusively :")
        exit()
        if not i:
            break
    if not i:
        break
    while int(z) < 1 or int (z) > 3999:
        print('"Not Valid Input!!!"')
        z = input ("Please enter a number between 1 and 3999, inclusively :")
        exit()
        if not i:
            break
    if not i:
        break
    sonuc = ""
    for j in range(len(z), 0, -1):
        if j == 4:
            sonuc += roma(int(z[len(z) - j]), 'M')
        if j == 3:
            sonuc += roma(int(z[len(z) - j]), 'C', 'D', 'M')
        if j == 2:
            sonuc += roma(int(z[len(z) - j]), 'X', 'L', 'C')
        if j == 1:
            sonuc += roma(int(z[len(z) - j]), 'I', 'V', 'X')
    print(sonuc)
    z = input ("Please enter a number between 1 and 3999, inclusively :")
    exit()
    if not i:
        break