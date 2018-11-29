#below are the notes of learn python- Full course for beginners(Youtube) giraffe academy

# at the beginning of this course, please go to www.jetbrains.com/pycharm to download pycharm .
# this note record the most used command and function. is not fully explain python.

# python will execute command line in order.

print("Giraffe\" academy")  # if you want to print string with "" inside.
#string function
#string.lower ()
#string. upper()
#string.islower()
#string.isupper()
#or can use both of function of stirng:
#string.upper().islower()

#index function

#string.index("G")
#string.replace("old", "replacemenbt")

#math
abs(-3)
pow(3,2) # or can type 3 **2 means power
max(4,5)
min(4,6)
round(3.7)
floor(3.6) # returns 3
ceil(3.7) # returns 4
sqrt(36)

#input command default will return string, you can convert to float ( number ).


int(3.5)
float(4.5)

# list can contain multiple type of data. (boolean, number, string)
list = ["Kevin", 5, True]

#append list together:
#list.extend(list2)
#list.append("string")
#list.insert(index, "string")  index is what i want to append.
#list.remove("string")
#list.clear()
#list.pop() remove last element in the list
#list.index("element")
#list.count("element") count how many times that element appears.
#list.sort
#list.reverse() in ascending order.
#list.copy()

# Tuple

#tuple can not change once created, is better to use as coordinate, etc.
Tuple = (4,5)




def sayhi(name):
    print("hello world")
print("max")

sayhi("mike")

def cube(num):
    return num**3 # cube function format is slightly different with R

print(cube(3))

#if function sample:
is_male = True
if is_male:
    print("you are a male")

#create a simple calculator to specify which number is the largest:
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2>=num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3,4,5))

#build a calculator (simple one):
num1 = float(input("enter the first number: "))
op = input("enter the operation: ")
num2 = float(input("enter the second number: "))

if op == "+":
    print (num1 + num2)
elif op =="-":
    print(num1 - num2)
elif op =="/":
    print (num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("invalid")

#dictionary

monthConversion = {"Jan": "January", "Feb": "February", "Mar": "March"}
print(monthConversion.get("Jan"))

#the get function in dictionary is very useful since it can add new key and new value in the dic.

#while loop :
i = 1
while i <= 10:
    print(i)
    i+=1
print("Done with loop")


#create a guessing game app:
secret_word = "giraffe"
guess = ""
guess_count = 0
while guess != secret_word:
    guess = input("Enter guess : ")
    guess_count += 1
print ("You win !!")
print(guess_count)

#while operates when condition is True, and stop operate when the condition meets false.









