def solution(area):
    # Your code here
    ans = []

    while area > 0:
        biggest_side = int(area ** 0.5)
        biggest_square = biggest_side ** 2
        area -= biggest_square
        ans.append(biggest_square)

    return ans
