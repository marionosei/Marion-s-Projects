# Credit Card and card number generator

try:
    creditCard = []
    count = 0
    with open("creditCards.txt", "r") as file1:
        for creditCard in file1:
            creditCards.append(creditCard.split("/n")[0])
    print(file1.readlines())   
    
except: print("ERROR - File could not be found")
else:
    if len(creditCard) != 16:
         if (creditCard.isdigit()):
             
             if creditCard < 4000000000000000 or creditCard > 4999999999999999:
                 print('valid')

             elif creditCard < 5000000000000000 or creditCard > 5999999999999999:
                 print('valid')

             elif creditCard < 2000000000000000 or creditCard > 2999999999999999:
                 print('valid')
       
             else:
                 print(str(creditCard) + 'is invalid.')
         else:
             print(str(creditCard) + 'is invalid.')
    else:
        print(str(creditCard) + 'is invalid.')

file1.close()
    

