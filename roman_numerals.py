print('key in value')
num = int(input())

num_rn = ""
roman_numerals={
    "M":1000,
    "CM":900,
    "D":500,
    "CD":400,
    "C":100,
    "XC":90,
    "L":50,
    "XL":40,
    "X":10,
    "IX":9,
    "V":5,
    "IV":4,
    "I":1
  }

for k in roman_numerals:
    while num >= roman_numerals[k]:
        num -= roman_numerals[k]
        num_rn += k
        print("log")

print(num_rn)