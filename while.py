"""

Start

1. Create a variable that counts each time a number is entered

2. Ask user to enter a number (using while loop)

3. If the user enters “-1”, the program should stop requesting the user
to enter a number,

4. The program must then calculate the average of the numbers entered,
excluding the -1.

Stop

"""

numbers = [] #Create a variable/ container to store numbers

while True:
    num = input("Please enter a number (or enter -1 to stop)") #Ask user to enter a number

    if num == "-1":
        break

    numbers.append(int(num)) #Add the new numbers to the storage container

if numbers:          #If numbers are entered, work out the average
   average = sum(numbers)/len(numbers)     
   print("The average is: ", average)

else:
    print("No numbers entered")