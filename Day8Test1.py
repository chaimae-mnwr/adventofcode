import copy

fichier = open('/home/menouar/Documents/dir5/game.txt', 'r')
action = []

for line in fichier:
    if line != "\n":
        line_split = (line.rstrip('\n')).split(" ")
        action.append(line_split)
#Test1:
actions = action
accumulator = 0
print(actions)
index =0
next_ind = 1
for element in actions:
    element.append(0)
print(actions)
element = actions[0]
while element[2] == 0 :
    if actions[index][0] == "nop" :
        index += 1
        element[2]+=1
        element = actions[index]

    elif actions[index][0] == "acc" :
        if actions[index][1][0] == '+':
            val_aj = int(actions[index][1][1:])
            accumulator+=  val_aj
            index += 1
            element[2]+=1
            element = actions[index]
        elif actions[index][1][0] == '-':
            val_aj = int(actions[index][1][1:])
            accumulator -=  val_aj
            index += 1
            element[2]+=1
            element = actions[index]
    elif actions[index][0] == "jmp" :
        if actions[index][1][0] == '+':
            val_aj = int(actions[index][1][1:])
            index +=  val_aj
            element[2]+=1
            element = actions[index]
        elif actions[index][1][0] == '-':
            val_aj = int(actions[index][1][1:])
            index -=  val_aj
            element[2]+=1
            element = actions[index]

print(accumulator)
#Day 2:

print(action)

next_ind = 1
for element in action:
    element.append(0)
def does_run_prog(actions):
    for element in action:
        element[2] = 0

    accumulator = 0
    index =0
    element = actions[0]
    while index < len(actions) :
        element = actions[index]
        if element[2] > 0:

            return False
        if actions[index][0] == "nop" :
            index += 1
            element[2]+=1


        elif actions[index][0] == "acc" :
            if actions[index][1][0] == '+':
                val_aj = int(actions[index][1][1:])
                accumulator+=  val_aj
                index += 1
                element[2]+=1

            elif actions[index][1][0] == '-':
                val_aj = int(actions[index][1][1:])
                accumulator -=  val_aj
                index += 1
                element[2]+=1

        elif actions[index][0] == "jmp" :
            if actions[index][1][0] == '+':
                val_aj = int(actions[index][1][1:])
                index +=  val_aj
                element[2]+=1

            elif actions[index][1][0] == '-':
                val_aj = int(actions[index][1][1:])
                index -=  val_aj
                element[2]+=1

    print(accumulator)
    return True

test_actions = copy.deepcopy(action)
initial = does_run_prog(test_actions)
change_ind = 0
while initial == False  :
    test_actions = copy.deepcopy(action)
    while test_actions[change_ind][0] == "acc":
        change_ind+= 1
    if test_actions[change_ind][0] == "jmp":
        test_actions[change_ind][0] = "nop"
    elif test_actions[change_ind][0] == "nop":
        test_actions[change_ind][0] = "jmp"
    change_ind+= 1
    initial = does_run_prog(test_actions)
