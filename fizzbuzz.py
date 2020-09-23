print('Enter a value')

num_str = input()
num = int(num_str)

state = ""

if num%3==0:
    state += "fizz"

if num%5==0:
    state += "buzz"

print(state)