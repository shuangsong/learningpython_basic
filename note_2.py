#FOR LOOP (continuted)
friends = ["ED", "Mark","alice"]
for index in range(len(friends)):
    print(friends[index])

#create a for loop for exponent function:

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3,2))
print(raise_to_power(3,4))


#nested loop and 2d list

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[0][0]) # row 0 and column 0
#it is like a matrix layout


print(number_grid[0][2])


for row in number_grid:
    for col in row:
        print(col)
        #print out all the element in the array


#build a translator
def translate(phrase):
    translation  = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
        #or if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation +letter
    return translation

#test translation
print(translate(input("Enter a phrase:")))

'''
you can type comment in here in another way beside #
'''



#except command: really powerful thing protect program from create errors.
try:
    answer = 10/0 # this will create error
    number = int(input("enter a number:"))
    print(number)
except ZeroDivisionError as err: # store the error as a variable, # we can specify exact type of error
    print(err)
except ValueError:
    print("invalid input")


