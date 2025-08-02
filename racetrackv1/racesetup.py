import random #random number generator

'''define cars'''
class Car:
    def __init__(self, model: str, driver: str, mpg: float, price: int, topspeed: int, gastanksize: float, gasremaining: float, wrecked: bool, performpenalty: float, winnings: int, totalmilesraced:float, racetime:float, totalracetime:float ):
        """Initialize a new instance of the Car class. topspeed is measured in mph. gastanksize is measured in gallons. price in dollars,milesraced in miles,racetime in minutes"""
        self.model = model
        self.driver = driver
        self.mpg = mpg
        self.price = price
        self.topspeed = topspeed
        self.gastanksize = gastanksize
        self.gasremaining = gasremaining
        self.wrecked = wrecked
        self.performpenalty = performpenalty #Car has performance degradation due to mechanical issues, affects topspeed and mpg
        self.winnings = winnings
        self.totalmilesraced = totalmilesraced
        self.racetime = racetime #racetime of current track, need to reset after each race
        self.totalracetime = totalracetime

    def describe_car(self) -> str:
        return f"{self.model} driven by {self.driver} gets {self.mpg}mpg with at topspeed of {self.topspeed}mph. This car costs ${self.price}.\n   Gas remaining is {self.gasremaining} of {self.gastanksize} gallons. Total winnings ${self.winnings}. Miles raced {self.totalmilesraced}. Seconds raced {self.totalracetime}.  "
'''define racetracks'''
class RaceTrack:
    def __init__(self, name: str, city: str, length: float, maxspeed: int, dangerlevel: int, prizemoney: int):
        """Initialize a new instance of the RaceTrack class. maxspeed is measured in mph. length is measured in miles"""
        self.name = name
        self.city = city
        self.length = length
        self.maxspeed = maxspeed
        self.dangerlevel = dangerlevel #Risk factor of car degradation or wrecking
        self.prizemoney = prizemoney
    def describe_racetrack(self) -> str:
        return f"The racetrack {self.name} located in {self.city} is {self.length} mile(s) long per lap and the max speed on the track is {self.maxspeed}. Prize for winning ${self.prizemoney}. Danger level {self.dangerlevel}."
    
    def Race(self,cars) -> str:
        #verify at least one car has gas to race, game is over when no cars have gas, car with most winnings is the winner
        if not any(car.gasremaining > 0 for car in cars):  #--insert code to check if 0 cars were passed into Race
            return "No cars have fuel, the racing has come to an end. Please select option C to see who won the most money."
        # determine which cars are going to race
        carstorace = []

        if len(cars) == 1: 
            print("Only 1 car is available for this race")
            keys = [0]
            carstorace.append(cars[0])
        else:
            print("2 or more cars are available for this race")
            carstorace = random.sample(cars, 2)
            keys = random.sample(range(len(cars)) , 2) 

        for key,c in enumerate(cars):
            if key in keys:
                carstorace.append(c) 
                #note can access each cars by carstorace[x], where x is 0 or 1 because you selected 2 cars
        #randomly set number of laps from 1 to 10 for the race
        laps = random.randint(1,10)

        #Print out the track, number of laps for the race and the cars racing info 
        #--insert code to print out the describe_racetrack information
        print(self.describe_racetrack())  #Print out the track

        #--insert code to print out 'The race will have {laps} laps around the track'
        print(f"The race will have {laps} laps around the track.") # number of laps for the race
        #--insert code to print out the describe_car information for each car racing
        for car in carstorace:  #cars racing info
            print(car.describe_car())
########################

        #Run each lap
        for l in range(0,laps,1):
            #show number of laps N of Total
            print(f"-- LAP #{lap} of {laps}--")
            for lap in range (1, laps + 1):   #<--insert code to print out '--LAP #{l+1} of {laps}--'  
               # 
                #
            #calculate how long it takes the each car to get around the track, based on car speed, track top speed, driverperformance in seconds
             for c in carstorace:
                #driverperformance - a percentage from 80 to 110, can make a car go faster or slower, car speed * driverperformance
                driverperformance = random.uniform(0.8, 1.10) #--code to calculate drivers performance as a percentage from 80 to 110
                #check if the current car has gasremaining
                if car.gasremaining > 0: # code to check if the current car gasremaining > 0
                    speed = round(car.topspeed * driverperformance, 2) #--code to calculate topspeed * drivers performance
                    if speed > self.maxspeed:#--code to check if speed > maxspeed of the course
                         speed = round(self.maxspeed * driverperformance, 2)
                        #if speed is greater than the maxspeed on the course, calculate 
                         speed = round(self.maxspeed * driverperformance,2) #-- code to calculate maxspeed * drivers performance
                    laptime = round(self.length / speed * 60, 2) #-- code to calculate laptime, hint length of course divided by speed x timevalue to get to seconds 
                    gasused = round(self.length / car.mpg, 2) #--code to calculate gasused, hint length/mpg 
 ###################################                   #######################
                    #update the gasremaining, milesraced, racetime, totalracetime for each car
                    gas_per_mile = 1 /car.mpg
                    c.gasremaining = round(c.gasremaining - (self.length * gas_per_mile),2) #-- code to update gasremaining for current car
                    lap_time = round(self.length / speed * 60, 2)
                    for car in carstorace:
                        c.racetime += lap_time #-- code to update racetime for current car
                        c.totalmilesraced += self.length #--   code to update totalmilesraced for current car
                        c.totalracetime += lap_time  #--   code to update totalracetime for current car
                    #if gasremaining for current car is 0 or less than the car ran out of gas
                    if car.gasremaining <= 0: #--  code to check if gasremaining <= 0
                        c.gasremaining = 0 #set gasremaining to 0, gasremaining should not be negative
                        c.racetime = c.racetime + 999999 #car ran out of gas so increase time to a high amount so it does not win
                        print (f"{c.model} ran out of gas and is out of the race.")
                    else:
                        print (f"{c.model} went {speed} mph around {self.name} in {laptime} seconds. It used {gasused} gallons of gas and has {c.gasremaining} gallons left. ")
        
        for c in carstorace:
            if c.gasremaining == 0:
                print (f"{c.model} ran out of gas during the race and did not win.")
        
        #whichever car gets the lowest time wins, add the track prizemoney to the car winnings
        if len(carstorace)==1:
            if carstorace[0].gasremaining > 0:
                for c in carstorace:
                    c.winnings += self.prizemoney  #--  code to update winnings for current car based on track prizemoney
                    c.racetime = 0 #reset racetime
                    print (f"{c.model} won the prize money. Current total ${c.winnings}")
            else:
                print ("Bad racing day, the only car left has ran out of gas")
        else:
            if carstorace[0].racetime < carstorace[1].racetime and carstorace[0].gasremaining > 0 :
                print (f"{carstorace[0].model} won the race.")
                carstorace[0].winnings += self.prizemoney  #--code to update winnings for current car based on track prizemoney
                print (f"{carstorace[0].model} won the prize money. Current total ${carstorace[0].winnings}")
            elif carstorace[0].racetime > carstorace[1].racetime and carstorace[1].gasremaining > 0:
                print (f"{carstorace[1].model} won the race.")
                carstorace[1].winnings += self.prizemoney #-- code to update winnings for current car based on track prizemoney
                print (f"{carstorace[1].model} won the prize money. Current total ${carstorace[1].winnings}")
            else:
                print ("Bad racing day, both of the race cars ran out of gas")
            carstorace[0].racetime=0 #reset racetime
            carstorace[1].racetime=0 #reset racetime
        
        return ('---Thanks for racing---')
