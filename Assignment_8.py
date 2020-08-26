year = int(input("Please enter a year:  "))

if year % 4 == 0 or year % 400 == 0:
    print(year,"is leap year")
elif year % 100 != 0:
    print(year,"is not leap year")