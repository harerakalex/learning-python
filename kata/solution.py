def solution(string,markers):
    n_list = []
    for sentence in string.split("\n"):
        s = ""
        for word in sentence:
            if word in markers:
                break
            else:
                s = s + word
        n_list.append(s.strip())
    return "\n".join(n_list)

print(solution('apples, pears # and bananas', ['#']))