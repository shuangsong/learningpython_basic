#Reading from external files:
employee_file = open("employee_file.txt", "r") #if file and your python file in the same directory.
#employee_file = open("employee_file.txt", "a")
#read mode could be:
'''
"r" mode --read file
"w" mode -- write file , change 
"a" mode -- append file, add new information to the file
"r+" mode -- read and write file
'''
print(employee_file.readable())
#return a boolean value to tell whether it is readable (read mode is on)
print(employee_file.read())
#will return all the information from the txt file.
print(employee_file.readline())
#read first line of the file

print(employee_file.readlines())
#print all lines in a array.

for employee in employee_file.readlines():
    print(employee)



#employee_file.close() #after you read the file you can close.


#Writing to files, appending
employee_file = open("employee_file.txt","a")
#if i want to append more information to the file

employee_file.write("\nToby -- Human resources")
employee_file.write("\nKelly --customer service")
#\n means you append at new line not existing line.
#print(employee_file.readlines())
employee_file.close()

#append you should be careful you could append everytime when you run command.
#when mode is "W" , you will overwrite everything in the old file.
employee_file1 = open("employee_file1.txt", "w")
employee_file1.write("\nhello world!")
employee_file1.write("\nhow are you!")
#employee_file1.close()
#you will write a new file now.
employee_file1 = open("employee_file1.txt", "r")
print(employee_file1.readlines())
employee_file1.close()
