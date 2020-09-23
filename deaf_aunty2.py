say = input("Say sometthing to aunty\n")
stay = True

while stay:
    if say == "I love you aunty, I have to go now":
        print('ok. Goodbye')
        blank = 0
        while blank<2:
            say = input("Boy! are you there ?\n")
            if say=="":
                blank+=1
        stay = False
    elif say.islower():
        say = input("WHAT? SPEAK UP!\n")
    elif say.isupper():
        say = input("YOU ARE VERY RUDE!\n")
    else:
        say = input("SHOW SOME RESPECT!\n")
