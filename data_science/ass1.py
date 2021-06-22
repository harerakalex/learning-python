import re

path = 'C:/Users/hp/Desktop/coding/python/assests'

def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    # YOUR CODE HERE
    name = re.findall('[A-Z][\w]{1,4}',simple_string)
    print(name)
    return name

def grades():
    with open ("assets/grades.txt", "r") as file:
        grades = file.read()

    # YOUR CODE HERE
    names = []
    for item in re.finditer("([A-Z][\w]* [A-Z][\w]*)[\w]*: B", grades):
        names.append(item.groups(2)[0])
    return names

def logs():
    with open("assets/logdata.txt", "r") as file:
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