#Test 1:
fichier = open('/home/menouar/Documents/dir5/bits.txt', 'r')
adresses = {}
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

        vals[i].append((int(adress), int(line_split[2])))


for i in range(0, len(masks)):
    for value in vals[i]:
        adress = value[0]
        binary = "{:036b}".format(value[1])
        result = binary
        result = list(result)
        print(result)
        for j in range(0, len(masks[i])):
            if masks[i][j] == '1' or masks[i][j] == '0':
                result[j] = masks[i][j]
        result = ''.join(result)
        adresses[adress] = int(result, 2)

print(sum(adresses.values()))
