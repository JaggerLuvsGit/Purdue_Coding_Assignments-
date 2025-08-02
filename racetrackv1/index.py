from racesetup import RaceTrack, Car
import random #random number generator

def present_menu() -> str:  
    #Presents a menu of options to the user and requests input until valid input is found.
    menu_options = {
        'C': 'See Current Car Stats',
        'R': 'Race',
        'X': 'Exit the program'
    }
    print ("Racing Menu")
    for key, value in menu_options.items():
        print(f"{key}: {value}")
    while True:
        choice = input("Please enter your choice (C/R/X): ").upper()
        if choice in menu_options:
            return choice
        else:
            print("Invalid input. Please try again.")

def main():

    #setup car variables
    cars=[]
    cars.append(Car('Ferrari','Alfonso',3.5,100000,240,21,21,False,0,0,0,0,0))
    cars.append(Car('Pontiac Grand Prix','Ralph',8,40000,160,18,18,False,0,0,0,0,0))
    cars.append(Car('Porsche 911 Carrera','Leo',6,90000,205,15,15,False,0,0,0,0,0))

    #setup track variables
    tracks=[]
    tracks.append(RaceTrack('Indianapolis Motor Speedway', 'Indianapolis, USA', 2.5,170,2,10000))
    tracks.append(RaceTrack('Le Mans', 'Sarthe, France', 8.4,240,6,20000))
    tracks.append(RaceTrack('Monza', 'Milan, Italy', 3.6,220,4,15000))

    for c in cars:
        print(c.describe_car())
    
    for t in tracks:
        print(t.describe_racetrack())

    while True:
        #Create a new list of cars with gas to use for racing
        carswithgas = []
        for c in cars:
            if c.gasremaining > 0:
                carswithgas.append(c)

        choice = present_menu()
        if choice == 'X':
            print("Thanks for racing with us today")
            break
        elif choice == 'C':
            for c in cars:
                print(c.describe_car())     
        elif choice == 'R':
            #select a track randomly for the race
            tracktorace =[]
            keys = (random.sample(range(len(tracks)), 1))
            for key,t in enumerate(tracks):
                if key in keys:
                    result = t.Race(carswithgas)

            #result = racesetup.Race(carswithgas, tracks)                
            print(result)

if __name__== "__main__":
  main()