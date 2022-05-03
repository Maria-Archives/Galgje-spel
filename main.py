print("Het Galgje spel")

woord = input("Vul een woord in: ")

print(woord)

spelen = True
fouten = 0
woordenlijst = []
for index in woord:
    woordenlijst += "_"

while spelen:
    letter = input("Vul een letter in: ")

    letterinwoord = letter in woord #True of False
    if letterinwoord == False:
        fouten = fouten + 1
        print("Dat is nog niet helemaal goed, probeer het een keer.")
    else: 
            for index in range(len(woord)):
                if woord[index] == letter:
                    woordenlijst[index] = letter
            
            if fouten > 8:
                print("Game over! Probeer het nog een keer.")
                spelen = False
                
            geraden_woord = ''.join(woordenlijst)
            if (geraden_woord == woord):
                print("Gefeliciteerd! Je hebt gewonnen!!!")
                spelen = False
            print(woordenlijst)