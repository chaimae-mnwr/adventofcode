fichier = open('/home/menouar/Documents/dir5/numbers.txt', 'r')
numbers = []

for line in fichier:
    if line != "\n":
        line_split = (line.rstrip('\n'))

        numbers.append(int(line_split))

#Test1:
acc_list = numbers[:25]
print(acc_list)
def is_valid(liste, nombre):
    for i in range(0,len(liste)):
        for j in range(i+1, len(liste)):
            if int(nombre) == int(liste[i])+int(liste[j]):
                print(str(nombre)+"="+str(liste[i])+"+"+str(liste[j]))
                return True
    return False

start = is_valid(acc_list, numbers[25])
print(start)
index = 25
while start:
    index += 1
    acc_list = acc_list[1:]
    acc_list.append(numbers[index])
    print(acc_list)
    start = is_valid(acc_list, numbers[index+1])

print(numbers[index+1])


#Test2:
index+= 1
objectif = numbers[index]
somme = []
for i in range(0, index):
    somme.append(numbers[i])
    for j in range(i+1, index):
        somme.append(numbers[j])
        if sum(somme) == objectif:
            print(min(somme)+max(somme))
            break
    somme = []
