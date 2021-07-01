path = 'C:/Users/hp/Desktop/coding/python/assests'

fileref = open('assests/grades.txt', 'r+')

# lines = fileref.read()

# print(len(lines))
# print(lines[0])

# for i in range(10):
#   fileref.write(str(i) + '\n')

for line in fileref:
    print(line.strip())
fileref.close()