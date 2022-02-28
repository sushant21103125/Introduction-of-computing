#Name = Sushant Kumar
#SID = 21103125
#Branch = CSE

#-----------------------------------------------------------------------------------------------------------------------------------------------
                                  #Assignment-4
#-----------------------------------------------------------------------------------------------------------------------------------------------


# Question-1

def TowerOfHanoi( x, from_rod, to_rod, middle_rod):
	if x == 0:
		return
	TowerOfHanoi(x-1, from_rod, middle_rod, to_rod)
	print("Move disk",x,"from rod",from_rod,"to rod",to_rod)
	TowerOfHanoi(x-1, middle_rod, to_rod, from_rod)
x = 3
TowerOfHanoi(x, 'A', 'C', 'B')


#-----------------------------------------------------------------------------------------------------------------------------------------------

# Question-2

from math import factorial
n=int(input("Enter the size of pascals triangle "))

print("By use of function")

for i in range(n):
	for j in range(n-i+1):
		print(end=" ")

	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")	#(Binomial Formula) nCr = n!/((n-r)!*r!)
	print()
print("\n\n")

print("By Use of Recursion")

def pascal_triangle(n,originalength=n):
    if n == 0:
        return
    pascal_triangle(n-1,originalength)
    #print spaces
    print('  '*(originalength-n), end='')

    #start with 1
    start = 1
    for i in range(1, n+1):

        print(start, end ='   ')

        #using Binomial Coefficient
        start = start * (n - i) // i
    print()
pascal_triangle(n)
print("\n")


#-----------------------------------------------------------------------------------------------------------------------------------------------

# Question-3

int1, int2 = map(int,input("Enter 2 numbers: ").split())
Quotient = int1 // int2
Remainder = int1 % int2
print("Part a")
print("a. Checking if the quotient and remainder is a callable value or not.")
print(callable(Quotient))
print(callable(Remainder))
print("Part b")
if (Quotient == 0):
    print("<b> The quotient is zero")
if (Remainder == 0):
    print("<b> The reminder is zero")
if (Quotient != 0 and Remainder != 0):
    print("<b> All the values are non zero")
print("Part c")
partClist = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]
result = []
for i in range(len(partClist)):
    if partClist[i] > 4:
        result.append(partClist[i])
print(f"<c> Filtered out numbers that are greater than 4 are : {result}")
print("Part d")
setresult = set(result)
print("<d> Set:",setresult)
print("Part e")
immutableSet = frozenset(setresult) #frozen Set is used to make the set immutable
print("<e> Immutable set:",immutableSet)
print("Part f")
print("<f> Hash value of the max value from the above set:", hash(max(immutableSet)))


#-----------------------------------------------------------------------------------------------------------------------------------------------

# Question-4

class Student:
    def __init__(self, student, roll_no):
        self.name = student
        self.roll_no = roll_no

    def __del__(self):
        print("Object deleted")


# creating object
student1 = Student("Sushant",21103125)
print("Object created")
print(f"The name of the student is {student1.name} and SID is {student1.roll_no}.") # printing the assigned values
del student1# deleting object


#-----------------------------------------------------------------------------------------------------------------------------------------------

# Question-5

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
#creating employee Object
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)
#part 1st updating salary
employee1.salary = 70000
print(f"(a) The updated salary of {employee1.name} is {employee1.salary} ")
#part 1st deleting a record
print("(b) Record of Viren deleted")
del employee3



#-----------------------------------------------------------------------------------------------------------------------------------------------

# Question-6

word =input("Enter the word: ")
word = word.lower()
# inputting a meaningful word with the exact same letters
testword = input("Enter a new meaningful word using the exact same letters to test your friendship: ")
testword = testword.lower()


# defining dictionary
def count_in_dict(word):
    count = {}
    list1 = list(word)

    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count


# shopkeeper's input to verify the word's meaning
def userinput():
    if count_in_dict(word) != count_in_dict(testword):
        print("The letters aren't exact, friendship is fake")
        return
    ans = input("Does the word makes sense?(y/Y or n/N )")
    if ans == 'y' or ans == 'Y':
        print("The friends pass the friendship test")
    elif ans == 'n' or ans == 'N':
        print("The word doesn't have a meaning, friendship is fake")
    else:
        print("Invalid input,try again with y/Y or n/N ")
        userinput()


userinput()

