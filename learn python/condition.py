marks1 = int(input("Enter marks for subject 1 : "))
marks2 = int(input("Enter marks for subject 2 : "))
marks3 = int(input("Enter marks for subject 3 : "))
marks4 = int(input("Enter marks for subject 4 : "))
marks5 = int(input("Enter marks for subject 5 : "))

marks = {"subject1":marks1,"subject2":marks2, "subject3":marks3, "subject4":marks4, "subject5":marks5}
print(marks)

total_percentage = (marks1 + marks2 + marks3 + marks4 + marks5) / 500 * 100
print("Total percentage is: ", total_percentage)

if total_percentage >= 90:
    print("Grade A")
    
elif total_percentage >= 80:
    print("Grade B")  # this will print the grade b as it satisfies the condition of 80% or above.
    
elif total_percentage <= 70:
    print("Grade C")   # this will print the grade c as it satisfies the condition of 40% or above.    
    
elif total_percentage <= 30:
    print("you failed try again next year")   # this will print the grade c as it satisfies the condition of 30% or above.
    
else:
    print("data  is not correct")  # this will print the grade c as it satisfies the condition of 30% or above.
    
    
    
    
    
    
username = input("Enter your username: ")

if (len(username) < 10):
    print("Username must be at least 10 characters long")  # this will print the grade c as it satisfies the condition of 30% or above.
    56