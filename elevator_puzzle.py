# Assiuming this is one of the fancy elevators where you don't just press up/down but you have to enter your destination to summon the car and you are assigned which elevator to get in.

# - there are 10 floors
# - there are 3 elevators
# - let's assume each elevator takes at least 2 minutes to deliver a single passenger
# - let's assume one additional minute per passenger


# Data set generator:
# - half the time the start/destination number should be 1 because that's where the exit is
# - the other half of the time the number should be randomly selected from 2-10
# - we can generate a set of between 5 and 60 people for each 30 min segment (assumes this particular elevator usually has at least 10 people per hour and at most 120)
# - "people" here means social units of people traveling together (two people together only press the buttons once)
# - each of the 60 people should be assigned an arrival time
# - for simplicity's sake we will assume that everyone gets either on or off at the 1st floor and that there is no reason to travel between floors (and nobody ever gets off on the wrong floor)

# beginning of a test run all elevators are waiting at the 1st floor.


test_data =[(0, 1, 2), (0, 8, 1), (1, 1, 6), (2, 1, 6), (2, 2, 1), (2, 7, 1), (3, 1, 8), (3, 5, 1), (6, 2, 1), (8, 3, 1), (8, 10, 1), (8, 1, 3), (9, 10, 1), (11, 4, 1), (11, 10, 1), (11, 2, 1), (12, 9, 1), (13, 2, 1), (15, 10, 1), (15, 9, 1), (17, 6, 1), (20, 6, 1), (20, 1, 4), (22, 1, 9), (22, 5, 1), (22, 6, 1), (23, 5, 1), (23, 10, 1), (23, 2, 1), (26, 8, 1), (26, 10, 1), (27, 10, 1), (27, 1, 10), (27, 1, 2), (28, 8, 1), (29, 1, 8), (31, 4, 1), (31, 1, 4), (31, 1, 10), (32, 1, 8), (34, 1, 3), (35, 1, 6), (36, 1, 3), (38, 1, 8), (39, 4, 1), (40, 6, 1), (40, 1, 8), (40, 4, 1), (43, 4, 1), (44, 1, 3), (44, 2, 1), (45, 3, 1), (46, 1, 5), (48, 5, 1), (49, 10, 1), (50, 10, 1), (50, 3, 1), (52, 1, 5), (53, 3, 1), (54, 2, 1), (57, 1, 5), (58, 8, 1), (58, 1, 10), (58, 1, 7), (59, 4, 1), (59, 9, 1)]
time = 0
up_queue = []
down_queue = []

class Elevator:
    def __init__(self, name, location, direction):
        self.name = name
        self.location = location
        self.direction = direction
        self.queue = []
        self.arrival_time = 0

    def pick_up_passengers(self):
        global up_queue
        global down_queue
        if self.location == 1:
            self.queue = up_queue
            up_queue = []
        elif self.location == 10:
            self.queue = down_queue
            down_queue = []


    def make_run(self):
        self.arrival_time = time + len(self.queue) + 1 # assumes each run takes 2 minutes for 1 passenger, each additional passenger takes one extra minute
        print("Elevator", self.name, "left from", self.location, "at the minute of", time, "to transport", self.queue, "on its way", self.direction, ".")
        if self.direction  == "down":
            self.location = 1
            self.direction ="up"
        else:
            self.location = 10 # while not necessary, for simplicity I'm sending each elevator all the way to the top
            self.direction = "down"
        print('Elevator', self.name, "will arrive on floor", self.location, "at", self.arrival_time)
        self.queue = []


A = Elevator('A', 1, 'up')
B = Elevator('B', 1, 'up')
C = Elevator('C', 1, 'up')
elevators = [A, B, C]


def queue_per_minute():
    global time
    print("future passengers:", test_data)
    while 0 < len(test_data):
        x = test_data[0]
        if x[0] == time:
            if x[1] > x[2]:
                down_queue.append(x)
            else:
                up_queue.append(x)
            test_data.remove(x)
        else:
            break


    for elevator in elevators:
        if elevator.location == 1 and len(up_queue) > 0 and elevator.arrival_time <= time:
            elevator.pick_up_passengers()
            elevator.make_run()
        elif elevator.location == 10 and len(down_queue) >0 and elevator.arrival_time <= time:
            elevator.pick_up_passengers()
            elevator.make_run()
    time += 1
    print("time is now", time)


while len(test_data) > 0 or len(up_queue) > 0 or len(down_queue) > 0:
    queue_per_minute()




# all three elevators start the hour


print("up queue:", up_queue)
print("down queue:", down_queue)






# [(0, 1, 7),
# (1, 1, 9),
# (1, 9, 1),
# (1, 1, 10),
# (1, 2, 1),
# (4, 1, 9),
# (4, 1, 7),
# (4, 1, 4),
# (5, 4, 1),
# (5, 4, 1),
# (6, 1, 7),
# (6, 3, 1),
# (6, 2, 1),
# (6, 1, 6),
# (7, 8, 1),
# (7, 7, 1),
# (7, 1, 3),
# (8, 1, 6),
# (8, 4, 1),
# (8, 6, 1),
# (9, 5, 1),
# (10, 1, 4),
# (10, 1, 2),
# (10, 1, 8),
# (10, 6, 1),
# (11, 5, 1),
# (12, 6, 1),
# (13, 2, 1),
# (13, 6, 1),
# (15, 4, 1),
# (15, 10, 1),
# (15, 1, 3),
# (17, 4, 1),
# (17, 1, 2),
# (17, 9, 1),
# (17, 1, 2),
# (18, 8, 1),
# (18, 1, 8),
# (20, 1, 2),
# (20, 9, 1),
# (21, 7, 1),
# (22, 3, 1),
# (24, 1, 2),
# (24, 1, 2),
# (26, 1, 8),
# (26, 1, 4),
# (26, 1, 6),
# (27, 8, 1),
# (27, 1, 5),
# (27, 9, 1),
# (28, 1, 10),
# (28, 1, 6),
# (29, 9, 1),
# (29, 9, 1)]
