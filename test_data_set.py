# test data has an entry per 'person' (arrival time by minute, starting floor, destination floor)


import random

test_data = []

def create_test_data():
    number_of_people = random.randint(5, 120)
    print(number_of_people, "people arrived during this 60 minute stretch")
    for x in range(number_of_people):
        arrival_time = random.randint(0, 60)
        coming_or_going = random.randint(1, 2)
        if coming_or_going == 1:
            get_on = 1
            get_off = random.randint(2, 10)
        elif coming_or_going == 2:
            get_on = random.randint(2, 10)
            get_off = 1
        test_data.append((arrival_time, get_on, get_off))
        test_data.sort(key=lambda tup: tup[0])
    return(test_data)


print(create_test_data())
