def max_sequence(arr):
    if len(arr) == 0: return 0
    positive_numbers = [x for x in arr if x >= 0]
    negative_numbers = [x for x in arr if x < 0]
    if len(positive_numbers) == len(arr): return sum(positive_numbers)
    if len(negative_numbers) == len(arr): return 0   

    result_list = []
    # for i in range(len(arr) + 1):
    #     for j in range(i + 1, len(arr) + 1):
    #         result_list.append(sum(arr[i:j]))

    return max([sum(arr[i:j]) for i in range(len(arr) + 1) for j in range(i + 1, len(arr) + 1)])

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))