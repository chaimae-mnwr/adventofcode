fichier = open('/home/menouar/Documents/dir5/boarding.txt', 'r')
LN = []


for line in fichier:
    line_split = (line.rstrip('\n')).split(" ")
    LN.extend(line_split)

fichier.close()

def get_row(num):
    rows = [i for i in range(0,128)]
    for i in range(0,len(num)):
        index = int(len(rows)/2)
        if num[i] == "B":

            rows = rows[index:]
        else :
            rows = rows[:index]
    return rows.pop()

def get_column(num):
    rows = [i for i in range(0,8)]
    for i in range(0,len(num)):
        index = int(len(rows)/2)
        if num[i] == "R":
            rows = rows[index:]
        else :
            rows = rows[:index]

    return rows.pop()

#Part 1:

"""ids = []
for b_pass in LN :

    row = get_row(b_pass[:7])

    column = get_column(b_pass[7:])

    id_pass = row*8 + column
    ids.append(id_pass)
print(max(ids))
"""


#Part 2:
ids = []
missing = []
for b_pass in LN :

    row = get_row(b_pass[:7])

    column = get_column(b_pass[7:])

    id_pass = row*8 + column
    ids.append(id_pass)
ids.sort()
for index, truc in enumerate(ids) :
    if ids[index-1] == truc -2 :
        missing.append(truc-1)
print(missing)
