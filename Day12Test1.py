fichier = open('/home/menouar/Documents/dir5/ship.txt', 'r')
directions = []

for line in fichier:
    if line != "\n":
        line_split = (line.rstrip('\n'))
        directions.append([line_split[0],int(line_split[1:])])

#Test1:
initial = {"1":0,
          "2":0,
          "3":0,
          "0":0}
elements = ["N","E","S","W"]
face = "2"
for direction in directions:
    if direction[0] in elements:
        index = (elements.index(direction[0])+1)%4
        initial[str(index)] += direction[1]
    elif direction[0] == "R":
        face = str(int((int(face)+(direction[1]/90))%4))
    elif direction[0] == "L":
        face = str(int((int(face)-(direction[1]/90))%4))
    elif direction[0] == "F":
        initial[face] += direction[1]

result = abs(initial["1"]-initial["3"])+abs(initial["2"]-initial["0"])
print("Test 1 answer : ",result)

#Test2:
"""initial = {"1":0,
          "2":0,
          "3":0,
          "0":0}
elements = ["N","E","S","W"]
way_point = {"1":1,
            "2":10,
            "3":0,
            "0":0}
for direction in directions:
    if direction[0] in elements:
        index = int((elements.index(direction[0])+1)%4)
        way_point[str(index)] += direction[1]
    elif direction[0] == "R":
        for key, value in way_point.items() :
            new_key = str(int((int(key)+(direction[1]/90))%4))
            way_point["1"] , way_point[new_key] = way_point[new_key], way_point["1"]
    elif direction[0] == "L":
        step = int(direction[1]/90)
        for i in range(0,4):
            way_point["2"] , way_point[str((i-step)%4)] = way_point[str((i-step)%4)], way_point["2"]
            print((i-step-1)%4)
    elif direction[0] == "F":
        for i in range(0,4):
            initial[str(i)] += direction[1]*way_point[str(i)]
    print(way_point)
result = abs(initial["1"]-initial["3"])+abs(initial["2"]-initial["0"])
print("Test 2 answer : ",result)
"""

with open('/home/menouar/Documents/dir5/ship.txt') as f:
    instructions = [[x[0], int(x[1:])] for x in f.read().splitlines()]

# Class for both parts.
class Ship():
    def __init__(self):
        self.facing = 'E'
        self.coord_x = 0
        self.coord_y = 0
        # Relatives to ship coords x y.
        self.wayp_x = 10
        self.wayp_y = 1

    def move(self, direction, number):
        """
        Moves the ship {number} units in {direction}
        """
        if direction == 'N':
            self.coord_y += number
        elif direction == 'S':
            self.coord_y -= number
        elif direction == 'E':
            self.coord_x += number
        elif direction == 'W':
            self.coord_x -= number

    def move_waypoint(self, direction, number):
        """
        Moves the waypoint {number} units in {direction}
        """
        if direction == 'N':
            self.wayp_y += number
        elif direction == 'S':
            self.wayp_y -= number
        elif direction == 'E':
            self.wayp_x += number
        elif direction == 'W':
            self.wayp_x -= number

    def rotate(self, turn, amount):
        """
        Rotates the ship in {turn} direction {amount} degrees
        """
        to_angles = {'N': 90, 'S': 270, 'E': 0, 'W': 180}
        to_facing = {90: 'N', 270: 'S', 0: 'E', 180: 'W'}
        if turn == 'R':
            angle = (to_angles[self.facing] - amount) % 360
            self.facing = to_facing[angle]
        elif turn == 'L':
            angle = (to_angles[self.facing] + amount) % 360
            self.facing = to_facing[angle]

    def rotate_waypoint(self, turn, amount):
        """
        Rotates the waypoint around the ship
        in {turn} direction {amount} degrees
        """
        if turn == 'R':
            angle = 360 - amount
        elif turn == 'L':
            angle = amount

        if angle == 90:
            helper = self.wayp_x
            self.wayp_x = -1 * self.wayp_y
            self.wayp_y = +1 * helper
        elif angle == 180:
            self.wayp_x = -1 * self.wayp_x
            self.wayp_y = -1 * self.wayp_y
        elif angle == 270:
            helper = self.wayp_x
            self.wayp_x = +1 * self.wayp_y
            self.wayp_y = -1 * helper

    def move_ship_to_wayp(self, number):
        self.coord_x += number * self.wayp_x
        self.coord_y += number * self.wayp_y

my_ship_2 = Ship()
for order in instructions:
    action = order[0]
    value = order[1]
    if action == 'F':
        my_ship_2.move_ship_to_wayp(value)
    elif action in ['R', 'L']:
        my_ship_2.rotate_waypoint(action, value)
    elif action in ['N', 'S', 'E', 'W']:
            my_ship_2.move_waypoint(action, value)
answer_2 = abs(my_ship_2.coord_x) + abs(my_ship_2.coord_y)
print(f"Part 2 - Manhattan Dist: {answer_2}")
