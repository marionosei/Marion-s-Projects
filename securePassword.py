#This program will generate a new and secure password

#This will input which day in the month the customer was born
day = input("Input the day in the month you were born in: ")

#This will input the customers' favorite animal
animal = input("Input your favorite animal: ")

#This will input the first name of the customer
name = input("Input your first name: ")

#This will calculate the password using the given information
password = name[-2:]+day+animal[:3]+name[0].upper()+"**"

#This will print out the new and secure password for the customer
print("The new and secure password is now: ",password)
