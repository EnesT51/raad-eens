import random

ronden = 0
score = 0

while ronden < 20:
    nummer = random.randint(1,1000)
    print(nummer)
    print("dit is ronden", ronden)
    ronden +=1
    poging = 1
    
    while poging < 10:
        
        guess = input("raad het getal tussen 1 en de 1000. of als je wilt stoppen type stop!: ")
        
        if guess.isdigit()==False:
            poging = 10
            ronden = 20
            
        elif int(guess) == nummer:
            score+=1
            print("je hebt het goed geraden score is" , score)
            poging = 0
            break
            
        else:
            print("poging",poging)
            poging +=1

        if guess.isdigit():
            
            if int (guess) < nummer:
                verschil =  nummer - int(guess)
                richting = 'hoger'
            else:
                verschil = int(guess) - nummer
                richting = 'lager'

            if verschil < 20:
                print("je hebt het bijna goed raad", richting,"!")
            elif verschil < 50:
                print("niet goed raad wat", richting,"!")
            else:
                print("niet goed raad veel", richting,"!")

print("game is afgelopen, je hebt totaal" , score,"punten gescoord!")           





            