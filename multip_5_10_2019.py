"""Challenge 1: bedömningskriterierna när
För att få de fulla 60 poängen av uppgiften måste ni:

Ha en fullständigt korrekt lösning
Använda en for-loop som räknar varven (inte while, inte rekursion!!)
Använda funktioner enligt konstens regler (all datatrafik via parametrar och return) om ni alltså använder funktioner
(dvs inga globala variabler i dem accepteras)
Implementera (bra, så att det blir intressant att använda programmet) alla de extra features (1-3) som nämns i slutet av uppgiftstexten
Strukturera koden bra och välja variabelnamn som är självdokumenterande (inte a, b, c, x, y, z ...).

Logiska fel (att programmet räknar fel, ger fel svar eller fel feedback, fel antal varv etc.) leder till poängavdrag på 5-10p/fel.

You can do it! =D

    Annamari & co."""


"""Planering:
1. En funktion som håller reda på hur många rätta svar andvändaren givit.
2. En funktion som baserat på antal rätta svar justerar svårighetsgraden.
3. Ett facit i slutet.
4. möjligtvis något till."""

"""Har försökt skriva programmet luftigt så att det lättare ska gå att dechiffrera."""


import random




def resultat(x): #justera efter att andra delar blivit klara så du vet vad du ska göra med den här
    x = x + 1
    print "------"
    print "Score:", x
    print "------"
    return x

def difficulty(y):
    
    if y >= 4 and y < 7:
        print
        print "Difficulty: 2"
        tal_1 = random.randint(5,15)
        tal_2 = random.randint(11,20)
        timesTal = tal_1 * tal_2
        print tal_1, "*", tal_2
        
            

    elif y >= 7 and y < 20:
        print
        print "Difficulty: 3"
        tal_1 = random.randint(8,20)
        tal_2 = random.randint(13,28)
        timesTal = tal_1 * tal_2
        print tal_1, "*", tal_2
        
            

    elif y >= 20:
        print "Binary multiplication!"
        #fortsättning följer...

    else:
        print
        print "Difficulty: 1"

        if score >= 1:
            for i in range(0, (score+1)): #för att lätt och obemärkt öka snäppet på svårighetsgraden inom nivå 1
                tal_1 = random.randint(i,10)
                tal_2 = random.randint(i,10)

        else:
            tal_1 = random.randint(1,10)
            tal_2 = random.randint(1,10)

        timesTal = tal_1 * tal_2
        print tal_1, "*", tal_2
        
    return timesTal

def grade(a,b):
    percent = (a/b)*100
    if 50 <= percent < 60:
        print "1/5"
    elif 60 <= percent < 70:
        print "2/5"
    elif 70 <= percent < 80:
        print "3/5"
    elif 80 <= percent <= 90:
        print "4/5"
    elif 90 < percent:
        print "5/5"
    else:
        print "0/5, better luck next time"


    
print "------------------------------------------------"
print "Test on multiplication."
print "You will be handed a key at the end.\nGood luck!"
print "------------------------------------------------"


questionAmount = input("How many questions are you prepared to answer?\nThe more questions you get right, the more difficult it becomes!\nAmount of questions:")


score = 0

facit = {}

#Main loop

for i in range(0,questionAmount):
    
    

    checkIfCorrect = difficulty(score)
    
    userInputOnQuery = input("Your answer:\n")
    
    if userInputOnQuery == checkIfCorrect:
        print
        print "Correct!"
        print
        score = resultat(score)

    else:
        print
        print "Incorrect!"
        print 

    facit.update({i+1:checkIfCorrect})
    

print "Key: "
print facit
print "Grade: "
grade(score, questionAmount)







        
        
