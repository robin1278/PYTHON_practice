Game=input('''Let's play a game of Rock, Paper and scissors.

The rules  are simple: 
1 Rock wins against scissors;
2 paper wins against rock;
3 scissors wins against paper;
4 If both players throw the same hand signal, it is considered a tie, and play resumes until there is a clear winner.

Please type '1' for 'Rock', please type '2' for 'paper' and please type '3' for scissors.''')

new_number=int(Game)

import random
x=random.randint(1,3)

if new_number==x:
    print("it's tie")

elif new_number==1 and x==2:
    print("You lose")

elif new_number==1 and x==3:
    print("You won")

elif new_number==2 and x==1:
    print("You won")

elif new_number==2 and x==3:
    print("You lose")

elif new_number==3 and x==2:
    print("You won")

elif new_number==3 and x==1:
    print("You lose")

