import random
x=random.randint(1,100)
y=str(x)
# z=range(1,6)
for item in range(1, 10):

    guess_number=(input("please guess a number between 1-100 "))
    
    if guess_number==y:
      print("Your guess is correct, you won!!!")  
    elif guess_number>y:
      print("your guess is larger, please guess a smaller number")
    elif guess_number<y:
      print("Your guess is smaller, please guess a larger number")   

else:
    print("You lose, you couldn't guess the number.")     