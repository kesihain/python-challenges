def linear_search(target, my_list):
    # your code
    targetfound = False
    for idx, num in enumerate(my_list):
        if num == target:
            print(idx)
            targetfound = True
            break
    if not targetfound:
        print("not found")

random_numbers = [6, 29, 18, 2, 72, 19, 18, 10, 37]

linear_search(18, random_numbers)  # 2 (it returns the position of the number)
linear_search(9, random_numbers)   # not found
