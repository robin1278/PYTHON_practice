# output_message = input("Welcome to the pypassword generator ")
import random
alphabets = "qwertyuiopasdfghjklzxcvbnm"
numbers = "1234567890"
symbol = "!@#$%^&*"

question_1 = input("How many letters would you like in your password ? ")
question_2 = input("How many symbols would you like ? ")
question_3 = input("How many numbers would you like ? ")

# Here we are going to use shuffle, choices and sample(maybe
# random.choices(sequence, weights=None, cum_weights=None, k=1))

x=random.choices(alphabets, k=4)
y=random.choices(numbers, k=4)
z=random.choices(symbol, k=4)
A=x+y+z
print(" so the password would be ")
# print(x+y+z)
print(''.join(A))