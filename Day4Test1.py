fichier = open('/home/menouar/Documents/dir5/passeports.txt', 'r')
LN = []
passeport = []
champs = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
for line in fichier:
    if line != "\n":
        line_split = (line.rstrip('\n')).split(" ")
        passeport.extend(line_split)
    else :
        LN.append(passeport)
        passeport =[]
LN.append(passeport)
passeport = []
valid_char = ["0","1","2","3","4","5",'6','7','8','9','a',
               'b','c','d','e','f' ]

eye_valid =["amb","blu","brn","gry","grn","hzl","oth"]
valid_num = ["0","1","2","3","4","5",'6','7','8','9']
def byr_valid(data):
    """checks valid year"""
    return len(data) == 4 and 1920 <=int(data) <= 2002

def iyr_valid(data):
    """checks valid year"""
    return len(data) == 4 and 2010 <=int(data) <= 2020

def exp_valid(data):
    """checks valid year"""
    return len(data) == 4 and 2020 <=int(data) <= 2030

def hgt_valid(data):
    """checks valid height"""
    if len(data) <4:
        return False
    if len(data) == 4:
        return (59<=int(data[:2])<=76 and data[2:] == "in")
    else :
        return (150<=int(data[:3])<=193 and data[3:] == "cm")
def hcl_valid(data):
    """checks valid height"""
    if data[0] != "#" or len(data)!= 7:
        return False
    else :
        for a in range(1,7):
            if data[a] not in valid_char:
                return False
        return True

def ecl_valid(data):
    return data in eye_valid

def pid_valid(data):
    """checks valid height"""
    if len(data)!= 9:
        return False
    else :
        for a in range(0,9):
            if data[a] not in valid_num:
                return False
        return True


def valid_element(machin, data):
    if machin == "byr":
        return byr_valid(data)
    elif machin == "iyr":
        return iyr_valid(data)
    elif machin == "eyr":
        return exp_valid(data)
    elif machin == "hgt":
        return hgt_valid(data)
    elif machin == "hcl":
        return hcl_valid(data)
    elif machin == "ecl":
        return ecl_valid(data)
    elif machin == "pid":
        return pid_valid(data)
    else :
        return False

fichier.close()

nbr_pass = 0
for element in LN:
    valid_data = []
    compteur = 0
    for truc in element:

        i = truc.index(':')

        if valid_element(truc[:i],truc[i+1:] ) :
            compteur+=1
            valid_data.append(truc)

    print(element, compteur,'\n',valid_data)
    if compteur == 7 :
        nbr_pass +=1


print(nbr_pass)
