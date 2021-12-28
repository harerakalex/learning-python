import random


def play(predicted_num: int) -> str:
    random_list = []
    for i in range(0, 5):
        n = random.randint(1, 90)
        random_list.append(n)

    print('Generated numbers:', random_list)

    if predicted_num in random_list:
        return 'You win'

    return 'You lost'


if __name__ == '__main__':
    input_num = input('Enter your Number: ')
    predicted_num = int(input_num)

    ans = play(predicted_num)

    print(ans)
