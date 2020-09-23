
def binary_search(target, my_list):
    # your code
    low = 0 
    high = len(my_list)
    while low <= high:
        i = (low+high)//2
        if my_list[i] < target:
            low = i+1
            continue
        if my_list[i] > target:
            high= i-1
            continue
        return i
    return None
print(binary_search(56, list(range(1, 201))))
