import numpy as np
import copy

fichier = open('/home/menouar/Documents/dir5/questions.txt', 'r')
groups = []
one_grp = []
alphabets = ['a','b','c','d','e','f','g','h','i','j','k',
          'l','m','n','o','p','q','r','s','t','u','v','w',
          'x','y','z']
for line in fichier:
    if line != "\n":
        line_split = (line.rstrip('\n')).split(" ")
        one_grp.extend(line_split)
    else :
        groups.append(one_grp)
        one_grp =[]
groups.append(one_grp)
one_group = []
print(groups)

#Test 1 :
num_qst = []
for group in groups :
    num_inter = 0

    qsts = copy.deepcopy(alphabets)
    for person in group :
        for i in range(0,len(person)):
            if person[i] in qsts :
                num_inter +=1
                qsts.remove(person[i])
    num_qst.append(num_inter)


somme = np.sum(num_qst)
print(somme)

#Test 2:
num_qst = []
somme = 0
for group in groups :
    num_inter = 0

    start = list(group[0])
    liste_inter = start
    for person in group :
        putain = []
        for i in range(0, len(person)):
            if person[i] in liste_inter :
                putain.append(person[i])
        liste_inter = putain
    somme += len(liste_inter)





print(somme)
