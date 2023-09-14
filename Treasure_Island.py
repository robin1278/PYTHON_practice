Way= input('''Welcome to the treasure Island. Your mission is to find the treasure.
You have two ways 1 or 2.
Please select either ''')
if Way=="1":
    Choise1=input("now you have two option, you can either choose to swim or wait for the boat")
    if Choise1=="wait":
        Choise2=input("Now you have walked to three doors and all of which are different colors. Blue, Yellow and Red. Please choose between these three.")
        if Choise2=="yellow":
            print("You got it!. you found the treasure")        
             
        else:
            print("Your game is over") 
                      
    else:
        print("Your game is over, you are sunk in the ocean and are dead")    
else:
    print("There is no treasure in 2nd way, you will have to walk 1st way") 
    