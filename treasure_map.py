row1=["X", "X", "X"]
row2=["X", "X", "X"]
row3=["X", "X", "X"]

map=[row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position=int(input("Where do you want to put the treasure? "))
item=input("Please type whatever you want to put at the said place ")

row1[position]=item
print(row1)

    