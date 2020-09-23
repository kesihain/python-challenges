def global_linear_search(target, my_list):
    # your code
    pos_arr=[]
    for idx, char in enumerate(my_list):
        if char == target:
            pos_arr.append(idx)
    print(pos_arr)

bananas_arr = list("bananas")   #  ["b", "a", "n", "a", "n", "a", "s"]
global_linear_search("a", bananas_arr)   # [1, 3, 5]