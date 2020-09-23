info = [
    ["name", "age", "pet"],
    ["Amy", "20", "bird"],
    ["John", "21", "cat"],
    ["Ash", "24", "dog"],
]

persons = info[1:]
key =info[0]

class_info = {}

for idx, person in enumerate(persons):
    class_info[idx]={key[0]:person[0],key[1]:person[1],key[2]:person[2]}

print(class_info)