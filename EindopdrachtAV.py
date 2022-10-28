
def sceneA1(): 
    print("Avernus it is.")
    print("It isn't perfect but it'll have to do.")
    print("A ticktet isn't cheap, it's about 1300 Eddies. Joslyn brought 2000 Eddies.")
    print("She'll need her Eddies on Avernus.")
    print("The airport is so chaotic, she might have a chance of sneaking past the security")
    #time.sleep(8)
    vraagA2()

def vraagB2():
    print("\n")
    print("So, what are we going to do? Try to sneak past or pay for the ticket?")
    print("A: Sneak past")
    print("B: Pay for the ticket")
    antwoord = input("Option:")
    if antwoord == ("A"):
        sceneC2()
    elif antwoord == ("B"):
      scene2D()
    else:
      print("This is not an option, try again.")
      vraagB2()

def sceneC2():
    print("A risky move for sure.")
    print("Gate 13A, the board says.")
    print("Joslyn looks around and finds a sign for gate 13B")
    print("First she goes through security control, she has nothing illegal on her so she's cleared to pass through.")
    print("When she gets to the gate, she sees exactly what she expected, pure chaos.")
    print("This is in her favour.")
    #time.sleep(8)
    print("She can only see 3 flight attendents. All of them are busy with the other passengers.")
    print("She has to play it smart.")
    print("The doors to the shuttle have already opent, but is guarded ny one of the attendents.")
    print("Joslyn looks around the gate, what can she do?")
    #time.sleep(8)
    print("On Joslyn's left, there is a family with 3 kids. They look stressed out.")
    print("It isn't pretty, but Joslyn has an idea.")
    print("She walks up to the father of the family and says:")
    print('"Sir, you do know that they only let one of the parents come on the plain right?"')
    print("The colour drains from the man's face.")
    #time.sleep(8)
    print('"What?!?!" He says. "That cannot be true!"')
    print('"I am very sorry but they just announced it in the main hall, it is so that more families have a chance to leave" Joslyn anwsers.')
    print("The man starts yelling, grabbing the attention of other families.")
    print("Other fathers seem to get upset and start throwing a fit.")
    print("It grabs the attention of the flight attendent, she walks up to the men, leavin the door ungaurded.")
    #time.sleep(8)  
    print("While everyone is paying attention to the men, Joslyn sees her chance.")
    print("She sneaks on board of the shuttle.")
    print("She can't just take a seat tho, they will notice there is one passenger too many.")
    print("Her only option is to hide in the bathroom and hope they won't check before launch.")
    #time.sleep(8)
    print("\n")
    print("Thankfully, nobody comes to check.")
    print("Some times goes by before they take off. It is far from ideal to take off while hidden in a bathroom, but Joslyn survives the rocky launch.")
    print("The flight isn't a long one, about 2 hours. Some people have come knocking on the door but non pushed her to open up.")
    print("It doens't take too long before they land and Joslyn comes out, they won't ask for her ticket now, will they?")
    #time.sleep(8)

#Hier komt scene 2D
#
#