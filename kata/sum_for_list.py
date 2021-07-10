# def sum_for_list(lst):
#     result = []
#     for p in sorted(get_prime_factors(lst)):
#         sum = 0
#         for num in lst:
#             if num % p == 0:
#                 sum += num
#         result.append([p, sum])

#     return result

# def sum_for_list(lst):
#     kvdict = {}
#     for num in lst:
#         if num < 0:num=-num
#         for item in range(1,num+1):
#             if num%item == 0 and isprime(item):
#                 if item in kvdict.keys():
#                     kvdict[item].append(num)
#                 else:
#                     kvdict[item] = [num]
#     res = []
    
#     for key in kvdict.keys():
#         vsum = 0
#         for num in kvdict[key]:
#             if key == 5:
#                 vsum = 0
#             else:
#                 vsum += num
#         res.append([key,vsum])

#     return sorted(res)

def sum_for_list(lst):
    factors = {i for k in lst for i in range(2, abs(k)+1) if not k % i}
    print(factors)
    prime_factors = {i for i in factors if not [j for j in factors-{i} if not i % j]}
    print(prime_factors)
    return [[p, sum(e for e in lst if not e % p)] for p in sorted(prime_factors)]
 

def get_prime_factors(lst):
    prime_factor = []
    for num in lst:
        if num < 0: num=-num
        prime_factor += [item for item in range(2,num+1) if(num%item == 0 and isprime(item) and item not in prime_factor)]

    return prime_factor

# def isprime(num: int):
#     flag = False
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 flag = True
#                 break
#     if flag:
#         return False

#     return True

def isprime(n): 
    if n <= 1: return False
    for i in range(2, n): 
        if n % i == 0: return False
    return True


print(sum_for_list([15, 21, 24, 30, -45]))