
file ='/home/menouar/expense.txt'

fichier = open(file, 'r')
LN = []
for line in fichier:
    line_split = (line.rstrip('\n')).split(" ")
    if "" in line_split:
        line_split.remove("")
    LN.extend(line_split)
fichier.close()

def soluce(liste_sl):
    """SOlution"""
    for i in range(0, len(liste_sl)):
        for j in range(0, len(liste_sl)):
            for a in range(0, len(liste_sl)):
                if int(LN[i])+int(LN[j])+int(LN[a])==2020:
                    return int(LN[i])*int(LN[j])*int(LN[a])
    return "Wola c'est fo ce machin"


print(LN)
print(soluce(LN))
