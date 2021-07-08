from string import ascii_lowercase

def vowel_back(st: str):
    new_str = ''
    for i in range(len(st)):
        if st[i] == 'c' or st[i] == 'o':
            new_str = new_str + get_movable_char(st[i], -1)
        elif st[i] == 'd':
            new_str = new_str + get_movable_char(st[i], -3)
        elif st[i] == 'e':
            new_str = new_str + get_movable_char(st[i], -4)
        elif st[i] not in 'aeiou':
            new_str = new_str + get_movable_char(st[i], 9)
        elif st[i] in 'aeiou':
            new_str = new_str + get_movable_char(st[i], -5)

    return new_str

def get_char_position(char: str) -> int:
    return ascii_lowercase.index(char)

def get_movable_char(char, move):
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    if get_char_position(char) in range(17, 26) and char not in 'code':
        movable_char = alpha[(get_char_position(char) - len(alpha)) + move]
    elif char in 'aeiou' and get_char_position(char) in range(0, 5) and char not in 'code':
        movable_char = alpha[(get_char_position(char) + len(alpha)) + move]
    else:
        movable_char = alpha[get_char_position(char) + move]

    if movable_char in 'code':
        movable_char = char
    print(char, '|',  get_char_position(char) , '|' , movable_char)

    return movable_char


print(vowel_back('bringonthebootcamp'))