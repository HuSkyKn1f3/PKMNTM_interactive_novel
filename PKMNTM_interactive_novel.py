import random
import time

HP=10

Caterpie=0
Metapod=0
Butterfree=0

def main():
    global HP

#intro ok
    print("--------------------------------")
    print("Welcome to 1st person pokemonTM!") #tecnically: Interactive PokemonTM Novel!
    print("---a mini pokemonTM adventure---")
    print("--------------------------------")
    time.sleep(1)

#first step: enter in the world ok

    user_input = input("To PLAY press P <> To quit press X: ").lower()

    while user_input!="x" and user_input!="p":
        print("Enter valid command pls")
        user_input = input("To PLAY press P <> To quit press X: ").lower()

    if user_input=="x":
        print("---------")
        print("Game over")
        print("---------")
    if user_input=="p":

#second step:to do in the world
        time.sleep(1)
        print("-------------------------------------------------------------")
        print("You are in the garden in front of your house with Charmander.")
        print("-------------------------------------------------------------")
        
        user_input2 = ""
        while user_input2 != "x":
            global HP
            time.sleep(1)
            #print(str(HP))
            if HP<=3:
                print("Charmander's flame flickers weakly.")
            if HP>=4 and HP<=6:
                print("Charmander's flame looks weak.")
            if HP>=7:
                print("Charmander's flame burns with energy")

            time.sleep(1)
            user_input2 = input("To go in the house press H <> To go in the grass press G <> To exit press X: ").lower()

            if user_input2!="h" and user_input2!="g" and user_input2!="x":
                print("Enter valid command pls")

            if user_input2 == "h":
                house()

            if user_input2 == "g":
                grass()
#in the house: get pkmn from mon-rest talking to mom.

# #in the grass: search pkmn-run-fight-look at pkmn-if hp pkmn zero go home talk to mom

        game_over() # this calls game over

def game_over():
    print("------------------")
    print("----Game over.----")
    print("Thanks for playng!")
    print("------------------")

def pokedex():
    time.sleep(1)
    print()
    print("POKEDEX")
    print()

    time.sleep(1)
    print("CHARMANDER:")
    print("A cute litte orange lizard, with a burning flame on the tail. If the flame is weak, Charmander is hurt.")

    print("CATERPIE:" + str(Caterpie) + "/3")
    if Caterpie == 3:
        print("A cute little green worm.")
    else:
        print("???")

    print("METAPOD:" + str(Metapod) + "/3")
    if Metapod == 3:
        print("A fun to fight in the PKMN games...")
    else:
        print("???")

    print("BUTTERFREE:" + str(Butterfree) + "/3")
    if Butterfree == 3:
        print("Despite the name it contains butter.")
    else:
        print("???")

def house():
    time.sleep(1)
    print("You go in the house.")
    time.sleep(1)

    user_input4 = input("To go rest press R <> To open the Podedex press P <> To exit press X: ").lower()
    while user_input4!="r" and user_input4!="p" and user_input4!="x":
        print("Enter valid command pls")
        user_input4 = input("To go rest press R <> To open the Podedex press P <> To exit press X: ").lower()

    if user_input4 == "r":
        time.sleep(2)
        print()
        print("You and Charmander feel restored.")
        global HP
        HP=10 # full HP

    if user_input4 == "p":
        time.sleep(1.5)
        print()
        print("You open the Podedex.")
        pokedex()

    print()        
    print("You go back to the garden.")
    print()
     
def grass():
    time.sleep(1)
    print("You go in the grass looking for a PKMN.")
    encounter = random.randint(1,2)
    if encounter ==2:
        time.sleep(2)
        print("But you found nothing...")

    else:
        time.sleep(2)
        print("You find a PKMN!")
        battle()

    print()

def battle():
    global HP
    foe_hp=random.randint(4,9)
    
    if foe_hp<=5:
        pkmn_foe="Caterpie"
    if foe_hp>5 and foe_hp<=6:
        pkmn_foe="Metapod"
    if foe_hp>=7:
        pkmn_foe="Butterfree"

    user_input3=""
    print()
    time.sleep(1)
    print("A wild " + pkmn_foe + " appear!")
    time.sleep(2)
    print("Go Charmender!")
    while foe_hp>0 and HP>0 and user_input3!="r":
        time.sleep(1)
        print()
        print("Foe " + pkmn_foe + " has "+ str(foe_hp) + " HP.")
        print("Charmander has " + str(HP) + " HP.")
        print()
    
        user_input3 = input("To FIGHT press F <> To RUN press R: ").lower()
        while user_input3!="f" and user_input3!="r":
            print("Enter valid command pls")
            user_input3 = input("To FIGHT press F <> To RUN press R: ").lower()

        if user_input3=="f":
            print()
            #my turn
            if HP>0:
                damage1=random.randint(1,2)
                foe_hp-=damage1
                time.sleep(1)
                print("Charmander attack for " + str(damage1) + "!")
            #foe turn
            if foe_hp>0:
                damage2=random.randint(1,3)
                HP-=damage2
                time.sleep(1)
                print("Foe " + pkmn_foe + " attacks for " + str(damage2) + "!")
            print()

        else:
            print()
            print("You run away!")

    if HP<=0:
        time.sleep(1)
        print("Oh no!Charmander fainted!")
        time.sleep(2)
        print("You went home to heal him!")
        HP=10 # full hp
        print()

    if foe_hp<=0:
        if pkmn_foe=="Caterpie":
            global Caterpie
            Caterpie+=1

        if pkmn_foe=="Metapod":
            global Metapod
            Metapod+=1

        if pkmn_foe=="Butterfree":
            global Butterfree
            Butterfree+=1

        time.sleep(1)
        print("Foe " + pkmn_foe +" fainted!")
        print()
    

        #print(str(foe_hp))#
        #print(str(HP))#
        #print(str(Caterpie))#
        #print(str(Metapod))#
        #print(str(Butterfree))#

# no modify under

if __name__ == '__main__':
    main()