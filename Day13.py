import numpy as np
from functools import reduce
#Test1:

buses = [41,37,379,23,13,17,29,557,19]
our_time = 1004345

nearest_val = [0 for i in range(0,9)]
for i in range(0,len(buses)) :
    initial = 0
    compteur = 0
    while initial < our_time:
        initial += buses[i]
        compteur +=1
    nearest_val[i] = initial

nearest_val  = np.array(nearest_val)
objectif = min(nearest_val - our_time)
new = nearest_val - our_time
index = np.where(new == objectif)[0][0]
print(index)
print("Test 1 answer : ",buses[index]*(nearest_val[index]-our_time))

#Test2:
#Solution exponentielle non valable :
"""fichier = open('/home/menouar/Documents/dir5/buses.txt', 'r')
buses = []
for line in fichier:
    if line != "\n":
        line_split = (line.rstrip('\n'))
        buses.append(line_split)
print(buses)
buses = buses[1]
buses = buses.split(",")
print(buses)
number = 0
intrus = []
distances = []
for bus in buses:
    if bus != 'x':
        distances.append(number)
        number = 0
    else :
        number += 1


while 'x' in buses :
    buses.remove('x')

timestamps = [0 for i in range(0, len(buses))]
print(timestamps)
print(distances)
print(buses)

timestamps[0] = int(buses[0])*10000000000000
result = False
while result == False :
    timestamps[0] += int(buses[0])
    count = 1
    for i in range(1, len(buses)):
        while timestamps[i]-timestamps[i-1] < distances[i] :
            timestamps[i] += int(buses[i])
        if timestamps[i]-timestamps[i-1] == distances[i]:
            count += 1
        else :
            break
    print(timestamps)
    if count == len(buses):
        result = True

print(timestamps[0])
"""
#Utilisation du Chinese theorem , solution d'après Reddit :



RUN_TEST = False
TEST_SOLUTIONS = [3417, 1068781, 754018, 779210, 1261476, 1202161486]
TEST_INPUT_FILE = '/home/menouar/Documents/dir5/buses.txt'
INPUT_FILE = '/home/menouar/Documents/dir5/buses.txt'

ARGS = []


def main_part2(input_file, ):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    if not RUN_TEST:
        inds_and_nums = [(ind, int(elem)) for ind, elem in enumerate(lines[1].split(',')) if elem != 'x']

        rests, divisors = [], []
        for (ind, num) in inds_and_nums:
            rests.append((-ind) % num)
            divisors.append(num)

        solution = chinese_remainder(rests, divisors)
        return solution

    else:
        print(chinese_remainder([2, 1, 3], [3, 4, 5]))

        solutions = []
        for line in lines:
            inds_and_nums = [(ind, int(elem)) for ind, elem in enumerate(line.split(',')) if elem != 'x']

            rests, divisors = [], []
            for (ind, num) in inds_and_nums:
                rests.append((-ind) % num)
                divisors.append(num)

            solution = chinese_remainder(rests, divisors)
            solutions.append(solution)
        return solutions


def chinese_remainder(remainders, divisors):
    M = prod(divisors)
    as_ = list(map(lambda d: int(M / d), divisors))
    eea_results = map(lambda tup: extended_gcd(*tup), zip(as_, divisors))
    is_ = [result[0] % div for result, div in zip(eea_results, divisors)]
    Z = sum(map(prod, zip(is_, remainders, as_)))
    x = Z % M
    return x


def prod(nums):
    return reduce(lambda a, b: a * b, nums, 1)


def extended_gcd(a, b):
    # EEA
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    # return Bezout coefficient 1, 2, and the gcd
    return old_s, old_t, old_r


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTIONS == solution)
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
