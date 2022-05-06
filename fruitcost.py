#cost of mangos and avacados
#mango price = (.45)
#avacado price = (.70)
try:
    mangos = int(input("enter amount of mangos: "))
    avacados = int(input("enter amount of avacados: "))
except:
    print('ERROR, ENTER A NUMBER')
else:
    solution = round(((.45) * (int(mangos)) + (.70) * (int(avacados))),2)
    print('Your total is $', solution)
