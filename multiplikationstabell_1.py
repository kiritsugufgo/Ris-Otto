import random

result = 0
for i in range(1,11):
    
    
    tal_1 = random.randint(1,9)
    tal_2 = random.randint(1,9)
    lastTal = tal_1
    
    s_1 = set()
    s_1.add(tal_1)
    s_2 = set()
    s_2.add(tal_2)
    if tal_1 in s_1:
        tal_1 = random.randint(1,9)
    elif tal_2 in s_2:
        tal_2 = random.randint(1,9)
    print
    print tal_1,"*",tal_2
    print
    
    
    user = input("Svar:\n")
    
    
    if user == tal_1*tal_2:
        print "Correct!", tal_1,"*",tal_2," = ",tal_1*tal_2,". You entered ", user
        result = result + 1
    
    
    else:
        print "Incorrect!", tal_1,"*",tal_2," = ",tal_1*tal_2,". You entered ", user


print result,"/10"

