fichier = open('/home/menouar/Documents/dir5/chargers.txt', 'r')
numbers = []

for line in fichier:
    if line != "\n":
        line_split = (line.rstrip('\n'))

        numbers.append(int(line_split))

#Test1:

first = min(numbers)

counter = {"1":0,
            "2":0,
            "3":0}
def nearest_c(number, chargers):
    """Returns the nearest adaptator in the adaptator list"""
    valid = []
    for charger in chargers:
        if 1 <= (charger - number) <= 3:

            valid.append(charger)
    print(valid,": ",number)
    new_val = min(valid)
    diff = new_val-number

    counter[str(diff)] += 1
    return new_val

while first < max(numbers) :
    first = nearest_c(first, numbers)
print(max(numbers))
#One more for the diff between source and personnal adaptator
print((counter["1"]+1)*(counter["3"]+1))


#Test2:
valid = [28,
33,
18,
42,
31,
14,
46,
20,
48,
47,
24,
23,
49,
45,
19,
38,
39,
11,
1,
32,
25,
35,
8,
17,
7,
9,
4,
2,
34,
10,
3,
0
]
init_val = {}
inter = [0,0,0]
for charger in valid :
    inter = [0,0,0]
    if charger-1 in valid :
        inter[2] = 1
    if charger-2 in valid :
        inter[1] = 1
    if charger-3 in valid :
        inter[0] = 1
    init_val[str(charger)] = inter
print(init_val)



valid.sort()
print(valid)
curr_charger = 3
curr_num  = 2
a_x_2 = 4
a_x_1 = 1
a_x_0 = 1
test = []
for charger in valid[4:] :
    curr_charger = charger
    if init_val[str(charger)] == [1,1,1] :
        curr_num = a_x_2 + a_x_1 + 2*a_x_0
        a_x_2, a_x_1 , a_x_0 = curr_num, a_x_2 , a_x_1
    elif init_val[str(charger)] == [1,0,0] :
        curr_num = a_x_2
        a_x_2, a_x_1, a_x_0 = curr_num, a_x_2, a_x_1
    elif init_val[str(charger)] == [1,0,1] :
        curr_num = a_x_2 + a_x_1
        a_x_2, a_x_1, a_x_0 = curr_num, a_x_2, a_x_1
    elif init_val[str(charger)] == [1,1,0] :
        curr_num = a_x_2 + a_x_1
        a_x_2, a_x_1, a_x_0 = curr_num, a_x_2, a_x_1
    elif init_val[str(charger)] == [0,0,1] :
        curr_num = a_x_2
        a_x_2, a_x_1, a_x_0 = curr_num, a_x_2, a_x_1
    elif init_val[str(charger)] == [0,1,0] :
        curr_num = a_x_2
        a_x_2, a_x_1, a_x_0 = curr_num, a_x_2, a_x_1
    elif init_val[str(charger)] == [0,1,1] :
        curr_num = a_x_2 + a_x_1
        a_x_2, a_x_1, a_x_0 = curr_num, a_x_2, a_x_1
    test.append([curr_charger, curr_num])



print(curr_num)
print(test)
# AoC day 10 part 2
from collections import Counter
data = sorted([int(x.strip()) for x in open('/home/menouar/Documents/dir5/chargers.txt')] + [0])
print(data)
c = Counter({0:1})
for x in data:
    c[x+1] += c[x]
    c[x+2] += c[x]
    c[x+3] += c[x]
print(c)    
print("Part 2:", c[max(data) + 3])
