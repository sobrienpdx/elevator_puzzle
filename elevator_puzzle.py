# Assiuming this is one of the fancy elevators where you don't just press up/down but you have to enter your destination to summon the car and you are assigned which elevator to get in.

# - there are 10 floors
# - there are 3 elevators
# - let's assume each elevator takes at least 2 minutes to deliver a single passenger
# - let's assume one additional minute per passenger


# Data set generator:
# - half the time the start/destination number should be 1 because that's where the exit is
# - the other half of the time the number should be randomly selected from 2-10
# - we can generate a set of between 10 and 60 people for each 30 min segment (assumes this particular elevator usually has at least 10 people per half hour and at most 60)
# - "people" here means social units of people traveling together (two people together only press the buttons once)
# - each of the 60 people should be assigned an arrival time
# - for simplicity's sake we will assume that everyone gets either on or off at the 1st floor and that there is no reason to travel between floors (and nobody ever gets off on the wrong floor)

import random

test_data = {}

def create_test_data():
    number_of_people = random.randint(10, 60)
    print(number_of_people)
    for x in range(number_of_people):
        arrival_time = str(random.randint(0, 30))
        coming_or_going = random.randint(1, 2)
        if coming_or_going == 1:
            get_on = 1
            get_off = random.randint(2, 10)
        elif coming_or_going == 2:
            get_on = random.randint(2, 10)
            get_off = 1
        test_data.update({arrival_time: (get_on, get_off)})
    return(test_data)



print(create_test_data())


# for x in range(10):
#   print random.randint(1,101)
