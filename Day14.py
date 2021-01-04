#Test 1:
fichier = open('/home/menouar/Documents/dir5/bits.txt', 'r')

masks = []
vals = []
i = -1
for line in fichier:
    line_split = line.rstrip('\n').split()
    if line_split[0] == 'mask':
        masks.append(line_split[2])
        i += 1
        vals.append([])
    else :
        a = line_split[0].index("[")
        b = line_split[0].index("]")
        adress = line_split[0][a+1:b]
        print(line_split)
        vals[i].append((int(adress), int(line_split[2])))
print(masks)
print(vals)

pass
pass
