# ASSIGNMENT-1

# Name = Sushant Kumar(CSE)
# SID = 21103125


#Assignment Question-1

a=input("Enter first number")
b=input("Enyter second number")
c=input("Enter third number")
d=(int(a)+int(b)+int(c))/3 #count the average of the number
print("The average of three numbers is :")
print(float(d))



#Assignment Question-2

standard_deduction=10000
depend_deduction=3000
gross=input("enter your gross income")
No_of_dependents=input("Enter your number of dependents")
taxable_income=int(gross)-int(standard_deduction)-(int(depend_deduction)+int(No_of_dependents))
tax=(float(taxable_income)*0.2)
print("Your income tax is :")
print(float(tax))



#Assignment Question-3

SID=input("Enter your SID")
Name=input("Enter your name")
Gender=input("Enter your Gender ")
Course_name=input("Enter your course name")
CGPA=float(input("Enter your CGPA"))
STUDENT=[SID,Name,Gender,Course_name,CGPA] #creating the list of elements
print(STUDENT) #printing the list


#Assignment Question-4

marks=[]
for i in range(5):
    marks.append(input("Enter marks of students"))
marks.sort()
print(marks)



#Assignment Question-5

colour=['Red','Green','White','Black','Pink','Yellow']
colour.remove(colour[3])
print("Part a question : ",colour)
colour=['Red','Green','White','Black','Pink','Yellow']
colour[3:5]=['Purple'] #change the elements of dictonary in one line
print("Part b of question :",colour)
