import random

print('Welcome to the rolling dice game!')
print('Enter Yes to start the game!')

wanna_play = 'yes'
while wanna_play == 'yes' or wanna_play == 'y':
    dice_num = random.randint(1, 6)
    print("your rolled dice number is {}".format(dice_num))
    wanna_play = input("wanna play more? if yes enter 'yes' or 'y' : ")
