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
            print("de game is gestopt je hebt" ,score,"punten gescoord")
            poging = 10 
            ronden = 20 
            
        elif int(guess) == nummer:
            print("je hebt het goed geraden score is" , score)
            score+=1
            poging = 0
            break
            
        else:
            print("fout! probeer het nogmaals!")
            print("poging",poging)
            poging +=1
            poging > 10

        if guess.isdigit():
            
            if int (guess) < nummer:
                verschil =  nummer - int(guess)
                richting = 'hoger'
            else:
                verschil = int(guess) - nummer
                richting = 'lager'

            if verschil < 20:
                print("je hebt het bijna goed raad", richting)
            elif verschil < 50:
                print("niet goed raad wat", richting,"!")
            else:
                print("niet goed raad veel", richting,"!")


if ronden <20:
    print("game is afgelopen, je hebt totaal" , score,"punten gescoord!")           





            