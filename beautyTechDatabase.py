class Business:
    def __init__(self, key, contact, price, location, rate, exits):
        self.key = key
        self.contact = contact
        self.price = price
        self.location = location
        self.rate = rate
        self.exits = exits

    def look(self):
        print(self.contact)
        print(self.price)
        print(self.location)
        print(self.rate)

    def showExits(self):
        print(self.exits)

    def go(self, direction):
        if direction in self.exits:
            return self.exits[direction]
        else:
            print("Command does not exist")
            return self.key

    def do(self, command):

        if command == "look":
            self.look()
        elif command == "exits":
            self.showExits()
        elif command == "next":
            return self.go("next")
        elif command == "nextHair3":
            return self.go("nextHair3")
        elif command == "nextMakeup":
            return self.go("nextMakeup")
        elif command == "nextMakeup2":
            return self.go("nextMakeup2")
        elif command == "nextMakeup3":
            return self.go("nextMakeup3")
        elif command == "nextNails":
            return self.go("nextNails")
        elif command == "nextNails2":
            return self.go("nextNails2")
        elif command == "nextNails3":
            return self.go("nextNails3")
        elif command == "nextLashes":
            return self.go("nextLashes")
        elif command == "nextLashes2":
            return self.go("nextLashes2")
        elif command == "nextLashes3":
            return self.go("nextLashes3")
        elif command == "nextHair":
            return self.go("nextHair")
        else:
            print("Error: Command does not exist, try again.")
        return self.key
        

if __name__ == "__main__":

    businesses = {}
    currentService = "luxlifehairco"

    #Hair
    luxlifehairco = Business("luxlifehairco", "laidbymari@gmail.com", "$80-$120", "Albany", "10/10", {"next": "finessedbyfolake"})
    finessedbyfolake = Business("finessedbyfolake", "dm on instagram", "$70+", "Albany/NYC", "9/10", {"nextHair3": "hairbybritc"})
    hairbybritc = Business("hairbybritc", "hairbybrit.as.me", "$25-$145", "Albany/NYC", "10/10", {"nextMakeup": "precizionbyprecious"})
    #Makeup
    precizionbyprecious = Business("precizionbyprecious", "dm on instagram", "$30-$50", "Albany/NYC", "10/10", {"nextMakeup2": "tutuonthebeat"})
    tutuonthebeat = Business("tutuonthebeat", "dm on instagram", "$40-$65", "Albany", "10/10", {"nextMakeup3": "ozzythemua"})
    ozzythemua = Business("ozzythemua", "dm on instagram", "n/a", "Albany", "10/10", {"nextNails": "ik__nails"})
    #Nails
    ik__nails = Business("ik__nails", "iknailsofalbany.as.me", "$30-$120", "Albany", "10/10", {"nextNails2": "star_ling518"})
    star_ling518 = Business("star_ling518", "dm on instagram", "n/a", "Albany", "10/10", {"nextNails3": "nailedbyness"})
    nailedbyness = Business("nailedbyness", "517-969-9066", "$20-$35", "Albany", "7/10", {"nextLashes": "_therealturbo"})
    #Lashes
    _therealturbo = Business("_therealturbo", "917-244-5649", "$50-$60", "Albany/NYC", "10/10", {"nextLashes2": "belashed__"})
    belashed__ = Business("belashed__", "belashed1126.as.me", "$70-$250", "Albany", "7/10", {"nextLashes3": "minksbymilly"})
    minksbymilly = Business("minksbymilly", "dm on instagram", "$40-$65", "Albany/NJ", "9/10", {"nextHair": "luxlifehairco"})

    businesses["luxlifehairco"] = luxlifehairco
    businesses["finessedbyfolake"] = finessedbyfolake
    businesses["hairbybritc"] = hairbybritc
    businesses["precizionbyprecious"] = precizionbyprecious
    businesses["tutuonthebeat"] = tutuonthebeat
    businesses["ozzythemua"] = ozzythemua
    businesses["ik__nails"] = ik__nails
    businesses["star_ling518"] = star_ling518
    businesses["nailedbyness"] = nailedbyness
    businesses["_therealturbo"] = _therealturbo
    businesses["belashed__"] = belashed__
    businesses["minksbymilly"] = minksbymilly

    '''
    businesses[currentService].look()
    businesses[currentService].showExits()
    currentService = "finessedbyfolake"
    businesses[currentService].showExits()
    '''

    currentService = businesses[currentService].do("look")
    currentService = businesses[currentService].do("exits")
    currentService = businesses[currentService].do("next")
    currentService = businesses[currentService].do("look")
    currentService = businesses[currentService].do("exits")
    currentService = businesses[currentService].do("nextHair3")
    currentService = businesses[currentService].do("look")
    currentService = businesses[currentService].do("exits")
    currentService = businesses[currentService].do("nextMakeup")
    currentService = businesses[currentService].do("look")
    currentService = businesses[currentService].do("exits")
    currentService = businesses[currentService].do("nextMakeup2")
    currentService = businesses[currentService].do("look")
    currentService = businesses[currentService].do("exits")
    currentService = businesses[currentService].do("nextMakeup3")
    currentService = businesses[currentService].do("look")
    currentService = businesses[currentService].do("exits")
    currentService = businesses[currentService].do("nextNails")
    currentService = businesses[currentService].do("look")
    currentService = businesses[currentService].do("exits")
    currentService = businesses[currentService].do("nextNails2")
    currentService = businesses[currentService].do("look")
    currentService = businesses[currentService].do("exits")
    currentService = businesses[currentService].do("nextNails3")
    currentService = businesses[currentService].do("look")
    currentService = businesses[currentService].do("exits")
    currentService = businesses[currentService].do("nextLashes")
    currentService = businesses[currentService].do("look")
    currentService = businesses[currentService].do("exits")
    currentService = businesses[currentService].do("nextLashes2")
    currentService = businesses[currentService].do("look")
    currentService = businesses[currentService].do("exits")
    currentService = businesses[currentService].do("nextLashes3")
    currentService = businesses[currentService].do("look")
    currentService = businesses[currentService].do("exits")
    currentService = businesses[currentService].do("nextHair")

myEmptyDictionary={}
myDictionary={
"hair":("luxlifehairco", "finessedbyfolake", "hairbybritc"), 
"makeup":("precizionbyprecious","tutuonthebeat", "ozzythemua"), 
"nails":("ik__nails", "star_ling518", "nailedbyness"), 
"lashes":("_therealturbo", "belashed__", "minksbymilly")} 
