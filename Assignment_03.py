Assignment-3

Name-Sushant Kumar
SID-21103125


#-----------------------------------------------------------------------------------------------------------------------------------------------


#Queation-1

print("Question 1 :  To count the number of words in a string or characters . \n")

input_str = input("Enter a string : ")
str = input_str.lower()
word_list = [x.strip() for x in str.split()]

num_words ={}
if len(word_list)==1:
    print("Since word length is 1 so checking for the number of same  characters :")
    for ch in word_list[0]:
        if ch not in num_words:
            num_words[ch]=1
        else:
            num_words[ch]+=1
else:
    print("Since word length is greater than 1 so checking for the number of same words :")
    for words in word_list:
        if words not in num_words:
            num_words[words]=1
        else:
            num_words[words]+=1

for word in num_words:
    print("{:<13}:{:<10}".format(word,num_words[word]))


#-----------------------------------------------------------------------------------------------------------------------------------------------


#Queation-2

dt=int(input("Day-"))
mth=int(input("Month-"))
yr=int(input("Year-"))

if(yr%4==0):
    if(yr%400==0):
      leap=True
    elif(yr%100!=0):
      leap=True
    else:
      leap=True
else:
    leap=False

def last_date(month):
 if(month%2==1):
   if(month<=7):
    lst_dt=31
   if(month>7):
    lst_dt=30
 if(month%2==0 and month!=2):
   if(month<=7):
    lst_dt=30
   if(month>=7):
    lst_dt=31
 if(month==2):
   if leap==True:
    lst_dt=29
   if leap==False:
    lst_dt=28
 return lst_dt

if(1<=mth and mth<=12 and 1<dt and dt<=31 and 1800<=yr and yr<=2025):
 if(dt<=last_date(mth)):
  if (dt==last_date(mth) and mth!=12):
    dt=1
    mth=mth+1
  elif(dt==31 and mth==12):
    dt=1
    mth=1
    yr=yr+1
  else:
    dt=dt+1
    print(f"Next Date is: {dt}/{mth}/{yr}")
 else:
    print('error')


#-----------------------------------------------------------------------------------------------------------------------------------------------


#Question-3

print("\n\nQuestion 3: to create a list of tuples having first element as the number and second as the square of the number. \n")
list_numbers = [int(x) for x in input("Enter all the numbers in a single line separated by space : ").split()]

new_list = []

for num in list_numbers :
    new_tuple =(num,num**2)
    new_list.append(new_tuple)

print("New list is :\n",new_list)


#-----------------------------------------------------------------------------------------------------------------------------------------------


#Question-4

marks=int(input("Marks\n"))

if(marks>=4 and marks<=10):
  if(marks==4):
      grade="D"
      perf="poor"
  elif(marks==5):
      grade="C"
      perf="below Average"
  elif(marks==6):
      grade="C+"
      perf="average"
  elif(marks==7):
      grade="B"
      perf="good"
  elif(marks==8):
      grade="B+"
      perf="very Good"
  elif(marks==9):
      grade="A"
      perf="excellent"
  elif(marks==10):
      grade="A+"
      perf="outstanding"
else:
    print("error")

print(f"Your Grade is {grade} an your performance is {perf}.")


#-----------------------------------------------------------------------------------------------------------------------------------------------


#Question-5

print("\n\nQuestion 5: Pattern printing.\n")
Ascii_A = ord("A")

for line in range(6):
    print(" "*(line),end="")
    for char_num in range(11-(2*line)):
        print(chr(Ascii_A + char_num),end="")
    print()


#-----------------------------------------------------------------------------------------------------------------------------------------------


#Question-6

print("\n\nQuestion 6 : Dictionary functions and sorting.\n")
program_flow = True
user_data={}
while(program_flow):
    student_name = input("Enter name : ")
    input_ok = False
    while(input_ok == False):
        student_sid = input("Enter  SID  :")
        if student_sid.strip().isdigit():
            input_ok = True  
        else:
            print("\nSID can only be a combination of numbers!!! ")

    user_data[student_sid]=student_name
    str = "k"
    while(str.lower()!="y" and str.lower()!="n"):
        str=input("\nDo you want to store more student data (Y/N) : \n")
        if str.lower()=="n":
            program_flow = False
        elif str.lower()!="y" :
            print("\nPlease enter Y or N only!!!\n")

# a. Print students details stored in the dictionary.

print("\nStudent data in the order as entered by the user : ")
for student_sid , student_name in user_data.items() :
    print(student_sid," : ",student_name)

# b. Sort dictionary using student names.
sorted_names = sorted(user_data.values())
new_user_data ={}
for student_name in sorted_names:
    for student_sid , names in user_data.items():
        if(names==student_name):
            new_user_data[student_sid]=student_name

print("\nSorted dictionary according to student names :")
for student_sid ,student_name  in new_user_data.items() :
    print("{:<15}:{:<15}".format(student_sid,student_name))

# c. Sort dictionary using student sids.

sorted_sids = sorted(user_data.keys())
new_user_data ={}
for student_sids in sorted_sids:
    for student_sid , student_name in user_data.items():
        if(student_sid==student_sids):
            new_user_data[student_sid]=student_name

print("\nSorted dictionary according to student sids :")
for student_sid,student_name in new_user_data.items() :
    print(student_sid," : ",student_name)

# d. Search a student details with SID and print name of that student.

input_ok = False
while(input_ok == False):
    search_sid = input("\nEnter the SID whose name you want to search :")
    if search_sid.strip().isdigit():
        input_ok = True
    else:
        print("\nSID can only be a combination of numbers!!! ")

if search_sid in user_data:
    print("\nName of the student with SID {} is {}.".format(search_sid,user_data[search_sid]))
else:
    print("SID {} is not present in our data.".format(search_sid))


#-----------------------------------------------------------------------------------------------------------------------------------------------


#Question-7

print("\n\nQuestion 7 :  Printing of Fibonacci series .")

def Fibonacci(num,sum=0,last=1,second_last=1):
    if last==1 and second_last==1:         #  function will first start from this block  as initially no argument will be passed for last and second_last.
        print(second_last,last,end=" ")
        sum=sum+2
        temp = last
        last = last + second_last
        second_last = temp
        num-=2
        Fibonacci(num,sum,last,second_last)
        return sum   # returning sum which will be used for calculating average.
    elif num>0:
        print(last,end=" ")
        sum=sum+last
        temp = last
        last = last + second_last
        second_last = temp
        num-=1
        Fibonacci(num,sum,last,second_last)
        return sum

# checking for the input if number of terms is a integer and greater than 0.

input_ok = False
while input_ok == False:
    num = input("Enter the number of terms to which you want the Fibonacci Series :")
    if num.strip().isdigit():
        num =int(num)
        if(num<=0):
            print("Numbers of terms cannot be less than 0 !!!")
        else:
            input_ok = True
    else:
        print("Numbers of terms can only be a  number not a alphabet !!!")
print()
sum = Fibonacci(num) # accepting the value returned by the Fibonacci function.
avg = sum/num
print("\n\nAverage is ",avg)


#-----------------------------------------------------------------------------------------------------------------------------------------------


#Question-8

print("\n\nQuestion 8 :  Set methods -  union , intersection , difference .")
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}

print("Given sets are :")
print("Set1 = ",Set1)
print("Set2 = ",Set2)
print("Set3 = ",Set3)


#****************************************************************
# We can use |(or) operator or union method on sets to find Union.
# We can use &(and) operator or Intersection on sets to find Intersection.
# We can use -(difference )  operator  for Difference between sets.
#****************************************************************




# a. Create a new set of all elements that are in Set1 and Set2 but not both.

new_set = Set1.union(Set2) - Set1.intersection(Set2)
print("\nNew set of all elements that are in Set1 and Set2 but not both : ", new_set)

# b. Create a new set of all elements that are in only one of the three sets Set1, Set2 and Set3.

unique_element_set = (Set1|Set2|Set3) - (Set1 & Set2)-(Set2 & Set3) - (Set3 & Set1)
print("\nNew set of all elements that are in only one of the three sets Set1, Set2 and Set3 :",unique_element_set)

# c. Create a new set of elements that are exactly two of the sets Set1, Set2 and Set3.  

exactly_two = (Set1 & Set2)|(Set2 & Set3)|(Set3 & Set1)-(Set1 & Set2 & Set3)
print("\nNew set of elements that are exactly two of the sets Set1, Set2 and Set3 : ",exactly_two)

# d. Create a new set of all integers in the range 1 to 10 that are not in Set1.

set_in_range = set(x for x in range(1,11)) - Set1
print("\nNew set of all integers in the range 1 to 10 that are not in Set1 :", set_in_range)

# e. Create a new set of all integers in the range 1 to 10 that are not in Set1,Set2 and Set3.

new_set_in_range = set(x for x in range(1,11)) - (Set1|Set2|Set3)
print("\nNew set of all integers in the range 1 to 10 that are not in Set1,Set2 and Set3:",new_set_in_range)
