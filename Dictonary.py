import random
import math
import json

f = open('names.json')
data =json.load(f)
f.close()

cities = data["cities"]
namePerson = data["namePerson"]

personer = {}
person = {
    "Navn": "",
    "Efternavn": "",
    "By": "",
    "Postnummer": "",
    "Skole": "",
    "Klasse": "",
    "Alder": ""
}
try:
    with open("savedPersoner.json","r") as f:
        personer = json.loads(f.read())
except:
    print("")

def addPersonsToPersoner(amount):
    for addToPersoner in range(int(amount)):
        tempPerson = dict(person)
        for keyPerson in person:
            tempPerson[keyPerson] = input(keyPerson + ":\n")
        personer[len(personer)] = tempPerson
        print(tempPerson)

def addRandomPersonsToPersoner(amount):
    for addToPersoner in range(int(amount)):
        cityPerson = cities[random.randrange(len(cities))]
        classYear = math.floor(random.randrange(1,10))
        fullName = namePerson[math.floor(random.randrange(len(namePerson)))]
        if " " in fullName:
            fullName = fullName.split(" ")
            secondName = fullName[1]
        else:
            secondName = ""
        tempPerson = dict(person)

        tempPerson["Navn"] = fullName[0]
        tempPerson["Efternavn"] = secondName
        tempPerson["By"] = cityPerson
        tempPerson["Postnummer"] = str(math.floor(random.randrange(100,9999)))
        tempPerson["Skole"] = cityPerson + " School"
        tempPerson["Klasse"] = str(classYear)
        tempPerson["Alder"] = str(classYear+math.floor(random.randrange(7,20)))
        personer[str(len(personer))] = tempPerson
        print(tempPerson)

def main():
    menuNav = input("\n1: Edit\n2: Add\n3: Search\n4: List Full\n5: Generate random\n6: Save All\n")
    match menuNav:
        case "1":
            idPerson = input("Which ID of person you want to edit?:\n")
            print(personer.get(str(idPerson)))
            confirmEdit=input("y/n\n")
            if confirmEdit == "Y" or confirmEdit == "y":
                editKey = input("Navn, Efternavn, By, Postnummer, Skole, Klasse, Alder\n")
                personer.get(str(idPerson)).update({editKey:input("Edit to?:\n")})
                print(personer.get(str(idPerson)))
        case "2":
            addPersonsToPersoner(input("How many you wanna add?\n"))
        case "3":
            searchingIn = input("Navn, Efternavn, By, Postnummer, Skole, Klasse, Alder\nWhat you searching for?\n")
            searchingFor = input("Search:")
            for idPerson, infoPerson in personer.items():
                if searchingFor in infoPerson.get(searchingIn):
                    print(idPerson, infoPerson)
        case "4":
            for idPerson, infoPerson in personer.items():
                print(idPerson, infoPerson)
        case "5":
            addRandomPersonsToPersoner(input("Amount of random\n"))
        case "6":
            saveString = json.dumps(personer, indent=2)
            with open("savedPersoner.json","w") as f:
                f.write(saveString)
        case _:
            print("Did not understand!")
            print(personer)
    main()

main()
