import time
import random

print("""Please pick your car for the Race:

1 > Ferrari
2 > Porsche
3 > Lamborghini
4 > McLaren""")

def user_input():
    user_input1 = input("Pick the number: ")
    
    if user_input1 == 1:
        print("\nYou chose the Ferrari")

    elif user_input1 == 2:
        print("\nYou chose the Porsche")

    elif user_input1 == 3:
        print("\nYou chose the Lamborghini")

    elif user_input1 == 4:
        print("\nYou chose the McLaren")
        print("Your winning car is on the track number " + str(user_input1))
	
    else:
        UserError()
	
def UserError():
    if user_input > 4 or user_input == 0 or user_input < 0:
        print("\nPlease choose 1-4")
        user_input() 
    else:
        pass
        
user_input()   
	    
time.sleep(2)

print("The Ultimate Race is on its way, who's gonna be the winner?")

time.sleep(2)

print("Ready? Set, GO!")
time.sleep(2)

def process(car):
    print(car)
RacingCars = ["Ferrari", "Porsche", "Lamborghini", "McLaren"]
#print(random.choice(RacingCars))

def improved():
    size = len(RacingCars)
    while size:
        index = random.randrange(size)
        elem = RacingCars[index]
        RacingCars[index] = RacingCars[size-1]
        size = size - 1
        process(elem)
        
improved()
