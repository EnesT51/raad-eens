import random

ronden = 1
poging = 1
score = 1

while ronden < 20:
    nummer = random.randint(1,1000)
    print(nummer)
    print("dit is ronden", ronden)
    ronden +=1
    poging = 1

    while poging < 10:
        guess = input("raad het getal tussen 1 en de 1000. of als je wilt stoppen type stop!: ")

        if guess == "stop":
            print("game is gestopt")
            poging = 10 
            

        elif int(guess) == nummer:
            print("je hebt het goed geraden score is" , score)
            score+=1
            poging = 1
            break
            
        else:
            print("fout! probeer het nogmaals!")
            print("poging",poging)
            poging +=1
            poging > 10

        # if guess > nummer and guess < nummer +20:
        #     print("je hebt het bijna goed raad lager")
        # elif guess < nummer and guess > nummer -20:
        #     print("raad wat hoger")
            





            