from typing import TypeVar

T = TypeVar('T')      # Declare type variabl

def bmi(weight: int, height: float) -> float:
    return weight / (height * height)

def binary_search(array: list[int], x: int) -> bool:
    ''' Binary search to search for order '''

    array.sort()
    left = 0
    right = len(array) - 1

    while left<=right :
        mid = (left + right)//2
        if array[mid] == x :
            return True
        elif(x < array[mid]):
            right = mid -1
        else:
            left = mid +1
    return False

def search_using_in(array: list[T], x: T) -> bool:    # Generic Functiom
    ''' Search if item exists in the list. '''

    if x in array:
        return True
    else: 
        return False