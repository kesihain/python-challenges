# Run the code. Read the error message.
# Fix it

# def mean(numbers):
#     print(type(numbers))
#     total = sum(numbers)
#     return total / len(numbers)

# print(mean([5, 3, 6, 10]))

# Define a method called user_details that takes in two arguments

# def user_details(name, occupation):
#     return f"Hi! My name is {name} and I am a {occupation}."

# ######
# # Call the method
# user_name = "Glo"
# user_occupation = "Lecturer"
# print(user_details(user_name, user_occupation))

# # 1. Write the error message here:

# # 2. Fix the code so that it works.

# Define a method called apple_price which takes in one argument
# def apple_price(num_of_apples):
#     return num_of_apples * 1.00


# ###############
# # Call the method
# # What's wrong with the following code?
# print(apple_price(10))

# # 1. Write down the error message here

# # 2. Fix the code so that it works.

# Define a method called "run" that does not take in any arguments
# but prints out "This is the method 'run' and it did not take in any arguments!"
# def run():
#     return f"This is the method 'run' and it did not take in any arguments!"

# ############################
# # Call the method
# print(run())

# Step 1: Determine the number of male adults to determine the number of couples
# couples equal 0.4*pop
# Number of male adults equals to number of couples
def adult_male_population(n):
    return n * 4/10


# Each couples will have 10 babies
def total_babies(n):
    return adult_male_population(n) * 10


# Step 2: Determine the number of adult females and baby females and add them up

def adult_female_population(n):
    return n * 6/10


def total_female(n):
    female_adults = adult_female_population(n)
    female_babies = total_babies(n) * 6/10
    return (female_adults + female_babies)

print(total_female(1600))