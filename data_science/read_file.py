import re

path = 'C:/Users/hp/Desktop/coding/python/assests'

def grades():
    with open ('../assests/grades.txt' , 'r') as file:
        grades = file.read()

    pattern = re.compile(r': B')

    matches = pattern.finditer(grades)

    matches_list = []
    for match in matches:
        matches_list.append(match)

    return matches_list


def read_file(): 
    file = open(f'{path}/grades.txt', 'r')
    grades = file.readlines()
    file.close()
    return grades

def logs():
    with open (f'{path}/logdata.txt', 'r') as file:
        logs = file.readlines()
    
    print(type(logs[0]))

# print('Found B grade:', len(grades()))
print('File Array', read_file()[0])
print(logs())