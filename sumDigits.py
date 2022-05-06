#this program will add up the digits in a 3-digit number
value = int(input("Enter a 3-digit value ")) #this is the 3 digit number being added
sum = 0
while not value%10==0:  #this will make it repeat until the last digit is not equal to zero
    sum += value%10 # this will take the last value of the 3-digit number and it will be added to the sum
    value//=10  #this will remove the last digit of the 3-digit number
print("The sum of the 3-digit value is",sum) #this will print the output
