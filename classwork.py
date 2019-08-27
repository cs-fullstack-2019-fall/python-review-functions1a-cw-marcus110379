## Problem 1
#Create a ```printNumbers``` function to print integers from -25 to 20 to the console (print in the function)
def numbers():
    for i in range(-25, 21, 1):
        print(i)
numbers() # function called

### Problem 2
#Create a function called checkPassword. Send two string variables to the checkPassword function to check if the strings are equal. Return true if they are equal and false if they are not equal. Print the function's return value.
def checkPassword(strg1, strg2): #arguments are passed in to parameters
    if strg1 == strg2: # if arguments are equal, true is return, else false return
        return "true"
    else:
        return "false"
# !! : this could easily be user input instead of hard coded 
print(checkPassword("horse", "people"))

## Problem 3
#Write a function that determines if a number passed to it is odd or even. Pass a number of your choosing (using input a good idea) and then using the result from the function, print if the number was even or not.
def main():
    userInput= int(input("enter a number "))
    oddEven(userInput)
def oddEven(userInput):
    if userInput % 2 == 0:  #if userinput is even, even is printed
        print( "even")
    else:
        print( "odd")  #if userinput is odd, odd is printed
main() # function called

### Problem 4
# * Create a function for the challenge that you call from your ```main```
# * Create a *second* function that takes NO parameters
# * Create a *third* function that takes a single greeting parameter (ex. ```Howdy```) and returns a string using the passed in greeting and 'World' (ex. ```Howdy World!```)
# * From your *first* function, call the function(s) and print out the final result returned
def main():
    func2()
    print(func2())
def func2():
	# !! : this could easily be user input instead of hard coded 
    return func3("Howdy")

def func3(greeting):
    return greeting + " world"
main()

## Problem 5:
##### We will keep having this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.
def loop():
    userInput = input("enter a string ")
    while userInput != "q":     # if userinput is not equal to "q" loop continues
        userInput = input("enter another string ")
loop()