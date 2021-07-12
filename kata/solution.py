def solution(string,markers):
    print('String====', string)
    print('Markers=====', markers)
    new_str = ''
    print(string.splitlines())
    for sentence in string.splitlines():
        count = 0
        for word in sentence.rstrip():
            if word in markers and sentence != string.splitlines()[-1]:
                new_str = new_str.strip() + '\n'
                break
            elif word in markers and sentence ==string.splitlines()[-1]:
                new_str = new_str.strip()
                break
            elif (len(sentence) -1) == count and sentence != string.splitlines()[-1]:
                print('here', word[-1])
                new_str = new_str + word[-1] + '\n'
                print('New', new_str)
                break 

            new_str = new_str + word
            count += 1

    print('Res====', new_str)
    return new_str

print(solution('apples, pears # and bananas', ['#']))