print("Welcome to the python pizza delivery!")
size=int(input("What size pizza do you want? 1-Small, 2-Medium, 3-Large "))

if size ==1:
    print("You chose small size pizza, which will cost $20")
    add_pepperoni=int(input("Do you want a pepperoni ? 1-yes and 0-No "))
    extra_cheese=int(input("Do you want extrab cheese ? 1-Yes and 0-No"))
    if add_pepperoni==1 and extra_cheese==1:
        print('''You have got small size pizza with extra added pepperoni and cheese, whch will cost $5. so the new price will be $25''')
    elif add_pepperoni==1 and extra_cheese==0:
        print("you have a small size pizza with extra cheese costing $22")
    elif add_pepperoni==0 and extra_cheese==1:
        print("You have got small size pizza with extra cheese, which will cost you $23")
    else:
        print("You have have ordered small size pizza in youir delivery, which will cost $20")

elif size==2:
    print("You chose medium size pizza, which will cost $25")
    add_pepperoni=int(input("Do you want a pepperoni ? 1-yes and 0-No "))
    extra_cheese=int(input("Do you want extrab cheese ? 1-Yes and 0-No"))
    if add_pepperoni==1 and extra_cheese==1:
        print('''You have got meium size pizza with extra added pepperoni and cheese, whch will cost $5. so the new price will be $30''')
    elif add_pepperoni==1 and extra_cheese==0:
        print("you have a meium size pizza with extra cheese costing $27")
    elif add_pepperoni==0 and extra_cheese==1:
        print("You have got meium size pizza with extra cheese, which will cost you $28")
    else:
        print("You have have ordered meium size pizza in youir delivery, which will cost $25")

elif size==3:
    print("You chose large size pizza, which will cost $30")
    add_pepperoni=int(input("Do you want a pepperoni ? 1-yes and 0-No "))
    extra_cheese=int(input("Do you want extrab cheese ? 1-Yes and 0-No"))
    if add_pepperoni==1 and extra_cheese==1:
        print('''You have got large size pizza with extra added pepperoni and cheese, whch will cost $5. so the new price will be $35''')
    elif add_pepperoni==1 and extra_cheese==0:
        print("you have a large size pizza with extra cheese costing $32")
    elif add_pepperoni==0 and extra_cheese==1:
        print("You have got large size pizza with extra cheese, which will cost you $33")
    else:
        print("You have have ordered large size pizza in youir delivery, which will cost $30")

