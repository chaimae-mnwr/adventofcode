fichier = open('/home/menouar/Documents/dir5/ship.txt', 'r')
directions = []

for line in fichier:
    if line != "\n":
        line_split = (line.rstrip('\n'))
        directions.append([line_split[0],int(line_split[1:])])
fichier = open('/home/menouar/Documents/dir5/ship.txt', 'r')
directions = []

for line in fichier:
    if line != "\n":
        line_split = (line.rstrip('\n'))
        directions.append([line_split[0],int(line_split[1:])])
