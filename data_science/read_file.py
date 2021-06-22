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
        logdata = file.read()
    
    # YOUR CODE HERE
    pattern="""(?P<host>[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)
                    (\ - \ )
                    (?P<user_name>(\w*)(\S))
                    (\  \S)
                    (?P<time>\d+\S\w*\S\d+\S\d+\S\d+\S\d+\s\S\d+)
                    (\S\s\S)
                    (?P<request>\w*\s\S*\s\w*\S\d.\d*)
              """
    data=[]
    for item in re.finditer(pattern,logdata,re.VERBOSE): 
        data.append(item.groupdict())
    return data  

print('Found B grade:', len(grades()))
print('File Array', read_file()[0])
print(logs())