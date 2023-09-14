year=int(input("Which year you wanrt to check: "))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("The year is leap year")
        else:
            print("The year is not a leap year")
    else:
        print("The year is not a leap year")            
else:
    print("The year is not a leap year")
