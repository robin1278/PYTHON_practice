student_heights=input("Input a list  of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n]= int(student_heights[n])

print(student_heights)  

# need to find average height using for loop

def avg_height(student_heights):
    first_height=0
    for n in student_heights:
        first_height=first_height+n        # n=n+1
        
    average_height= first_height/len(student_heights)
    print(average_height)

avg_height(student_heights)        

