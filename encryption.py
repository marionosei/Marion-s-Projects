#Numeric Encryption Scheme Program
finalCode=""
print('Enter the five digits of your PIN #, one at a time')
for num in range(1,6):
    digit = input('enter a digit: ')
    digit = int(digit)
    if digit == 1:
        code = 'o'
    elif digit == 2:
        code = 'Tw'
    elif digit == 3:
        code = 'Th'
    elif digit == 4:
        code = 'Fo'
    elif digit == 5:
        code = 'Fi'
    elif digit == 6:
        code = 'Si'
    elif digit == 7:
        code = 'Se'
    elif digit == 8:
        code = 'E'
    elif digit == 9:
        code = 'N'
    else:
        code = 'z'
    finalCode = finalCode + code
    print("Your encrypted PIN # is: ", finalCode)
