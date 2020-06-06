import random
winning = random.randint(1,1000)
guess = 1
number = int(input("enter a number : "))
game_over = False
while not game_over:
    if number == winning:
        print(f"you win and you guessed this number in {guess} times")
        game_over = True
    else:
        if number < winning:
            print("too low")
        else:
            print("too high")
        guess += 1
        number = int(input("try again : "))