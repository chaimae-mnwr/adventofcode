file ='/home/menouar/passwords.txt'

fichier = open(file, 'r')
LN = []
for line in fichier:
    line_split = (line.rstrip('\n')).split(" ")
    LN.extend(line_split)
fichier.close()

n1, n2 = 0, 0
let_test =""
mot_test =""
true_pass = 0
for i in range(0, len(LN)-3, 3):
    ind = LN[i].find('-')
    n1 = LN[i][:ind]
    print(n1)
    n2 = LN[i][ind + 1:]
    print(n2)
    let_test = LN[i+1][0]
    print(let_test)
    mot_test = LN[i+2]
    print(mot_test)
    compteur_t = 0
    if mot_test[int(n1)-1]== let_test:
        compteur_t+=1
    if mot_test[int(n2)-1]== let_test:
        compteur_t+=1
    print(compteur_t == 1)    
    if compteur_t == 1:
        true_pass+=1


print(true_pass)
