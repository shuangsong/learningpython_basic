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
            translation = translation + "g"
        else:
            translation = translation +letter
    return translation

#test translation
print(translate(input("Enter a phrase:")))

