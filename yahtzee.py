#Player 1
#variables
openSpacesp1 = ['ones', 'twos', 'threes', 'fours', 'fives', 'sixes', 'three of a kind', 'four of a kind', 'full house', 'small straight', 'large straight', 'yahtzee', 'chance']
openSpacesp2 = ['ones', 'twos', 'threes', 'fours', 'fives', 'sixes', 'three of a kind', 'four of a kind', 'full house', 'small straight', 'large straight', 'yahtzee', 'chance']
bonus = 0
bonusp1 = 0
bonusp2 = 0
pointsp1 = 0
pointsp2 = 0
claimedp1 = 'no'
claimedp2 = 'no'
hasYahtzeep1 = 'no'
hasYahtzeep2 = 'no'

#modules
import random
import time

#player names
p1name = input('Player one, what is your name? ')
p2name = input('Player two, what is your name? ')

#player 1 turn
def yahtzeep1(pointsp1 = 0):
    global claimedp1
    global bonusp1
    global hasYahtzeep1

    #roll dice
    rolls = [1]
    while len(rolls) < 5:
        if len(rolls) == 1:
            rolls[0] = random.randrange(1, 7)
            rolls.append(random.randrange(1, 7))
        else:
            rolls.append(random.randrange(1, 7))
    print()
    print('Your rolls:', rolls)
    print('Open spaces: ', openSpacesp1)
    print()

    #Choose which dice to reroll
    for x in [1, 2]:
        reroll = list(input(p1name + ' which dice would you like to reroll from 0-4? '))
        print()
        while len(reroll) > 0:
            rolls[int(reroll[0])] = random.randrange(1, 7)
            reroll.remove(reroll[0])
        print('Your rolls:', rolls)

    #Calc score
    ones = rolls.count(1)
    twos = rolls.count(2)
    threes = rolls.count(3)
    fours = rolls.count(4)
    fives = rolls.count(5)
    sixes = rolls.count(6)
    rollNumbers = [ones, twos, threes, fours, fives, sixes]
    
    print('Open spaces: ', openSpacesp1)
    print()
    chosenSpace = str(input(p1name + ' where would you like to put your points? '))

    if chosenSpace.upper() == 'ONES':
        if 5 in rollNumbers and hasYahtzeep1 == 'yes':
            pointsp1 += (1 * int(ones)) +50
        else:
            pointsp1 += 1 * int(ones)
        bonus = 1 * ones
        bonusp1 += bonus
        openSpacesp1.remove('ones')
        
        
    elif chosenSpace.upper() == 'TWOS':
        if 5 in rollNumbers and hasYahtzeep1 == 'yes':
            pointsp1 += (2 * int(twos)) +50
        else:
            pointsp1 += 2 * int(twos)
        bonus = 2 * twos
        bonusp1 += bonus
        openSpacesp1.remove('twos')

    elif chosenSpace.upper() == 'THREES':
        if 5 in rollNumbers and hasYahtzeep1 == 'yes':
            pointsp1 += (3 * int(threes)) +50
        else:
            pointsp1 += 3 * int(threes)
        bonus = 3 * threes
        bonusp1 += bonus
        openSpacesp1.remove('threes')

    elif chosenSpace.upper() == 'FOURS':
        if 5 in rollNumbers and hasYahtzeep1 == 'yes':
            pointsp1 += (4 * int(fours)) +50
        else:
            pointsp1 += 4 * int(fours)
        bonus = 4 * fours
        bonusp1 += bonus
        openSpacesp1.remove('fours')

    elif chosenSpace.upper() == 'FIVES':
        if 5 in rollNumbers and hasYahtzeep1 == 'yes':
            pointsp1 += (5 * int(fives)) +50
        else:
            pointsp1 += 5 * int(fives)
        bonus = 5 * fives
        bonusp1 += bonus
        openSpacesp1.remove('fives')

    elif chosenSpace.upper() == 'SIXES':
        if 5 in rollNumbers and hasYahtzeep1 == 'yes':
            pointsp1 += (6 * int(sixes)) +50
        else:
            pointsp1 += 6 * int(sixes)
        bonus = 6 * sixes
        bonusp1 += bonus
        openSpacesp1.remove('sixes')

    elif chosenSpace.upper() == 'THREE OF A KIND':
        if 5 in rollNumbers and hasYahtzeep1 == 'yes': 
            pointsp1 += sum(rolls) + 50
        elif 3 in rollNumbers or 4 in rollNumbers or 5 in rollNumbers in rollNumbers:
            pointsp1 += sum(rolls)
        openSpacesp1.remove('three of a kind')

    elif chosenSpace.upper() == 'FOUR OF A KIND':
        if 5 in rollNumbers and hasYahtzeep1 == 'yes': 
            pointsp1 += sum(rolls) + 50
        elif 4 in rollNumbers or 5 in rollNumbers:
            pointsp1 += sum(rolls)
        openSpacesp1.remove('four of a kind')

    elif chosenSpace.upper() == 'FULL HOUSE':
        if 3 in rollNumbers and 2 in rollNumbers:
            pointsp1 += 25
        elif 5 in rollNumbers and hasYahtzeep1 == 'yes':
            pointsp1 += 50
        openSpacesp1.remove('full house')

    elif chosenSpace.upper() == 'SMALL STRAIGHT':
        if (1 in rolls and 2 in rolls and 3 in rolls and 4 in rolls) or (2 in rolls and 3 in rolls and 4 in rolls and 5 in rolls) or (3 in rolls and 4 in rolls and 5 in rolls and 6 in rolls):
            pointsp1 += 30
        elif 5 in rollNumbers and hasYahtzeep1 == 'yes':
            pointsp1 += 50
        openSpacesp1.remove('small straight')

    elif chosenSpace.upper() == 'LARGE STRAIGHT':
        if (1 in rolls and 2 in rolls and 3 in rolls and 4 in rolls and 5 in rolls) or (2 in rolls and 3 in rolls and 4 in rolls and 5 in rolls and 6 in rolls):
            pointsp1 += 40
        elif 5 in rollNumbers and hasYahtzeep1 == 'yes':
            pointsp1 += 50
        openSpacesp1.remove('large straight')

    elif chosenSpace.upper() == 'YAHTZEE':
        if 5 in rollNumbers:
            pointsp1 += 50
            hasYahtzeep1 = 'yes'
        openSpacesp1.remove('yahtzee')

    elif chosenSpace.upper() == 'CHANCE':
        if hasYahtzeep1 == 'yes' and 5 in rollNumbers:
            pointsp1 += sum(rolls) + 50
        else:
            pointsp1 += sum(rolls)
        openSpacesp1.remove('chance')

    else:
        print('Input an available space')

    #bonus points
    if bonusp1 >= 63 and claimedp1 != 'yes':
        pointsp1 += 35
        claimedp1 = 'yes'

    if bonusp1 < 63:
        print(p1name, 'your current points is:', pointsp1, 'you have', bonusp1, '/ 63 for bonus points')
        print('-----------------------------------')
        print()
    else:
        print(p1name, 'your current points is:', pointsp1, 'including bonus points')
        print('-----------------------------------')
        print()

    return(pointsp1)






#player 2 turn
def yahtzeep2(pointsp2 = 0):
    global claimedp2
    global bonusp2
    global hasYahtzeep2

    #roll dice
    rolls = [1]
    while len(rolls) < 5:
        if len(rolls) == 1:
            rolls[0] = random.randrange(1, 7)
            rolls.append(random.randrange(1, 7))
        else:
            rolls.append(random.randrange(1, 7))
    rolls = [1, 1, 1, 1, 1]
    print()
    print('Your rolls:', rolls)
    print('Open spaces: ', openSpacesp2)
    print()

    #Choose which dice to reroll
    for x in [1, 2]:
        reroll = list(input(p2name + ' which dice would you like to reroll from 0-4? '))
        print()
        while len(reroll) > 0:
            rolls[int(reroll[0])] = random.randrange(1, 7)
            reroll.remove(reroll[0])
        print('Your rolls:', rolls)

    #Calc score
    ones = rolls.count(1)
    twos = rolls.count(2)
    threes = rolls.count(3)
    fours = rolls.count(4)
    fives = rolls.count(5)
    sixes = rolls.count(6)
    rollNumbers = [ones, twos, threes, fours, fives, sixes]
    
    print('Open spaces: ', openSpacesp2)
    print()
    chosenSpace = str(input(p2name + ' where would you like to put your points? '))

    if chosenSpace.upper() == 'ONES':
        if 5 in rollNumbers and hasYahtzeep2 == 'yes':
            pointsp2 += (1 * int(ones)) +50
        else:
            pointsp2 += 1 * int(ones)
        bonus = 1 * ones
        bonusp2 += bonus
        openSpacesp2.remove('ones')
        
    elif chosenSpace.upper() == 'TWOS':
        if 5 in rollNumbers and hasYahtzeep2 == 'yes':
            pointsp2 += (2 * int(twos)) +50
        else:
            pointsp2 += 2 * int(twos)
        bonus = 2 * twos
        bonusp2 += bonus
        openSpacesp2.remove('twos')

    elif chosenSpace.upper() == 'THREES':
        if 5 in rollNumbers and hasYahtzeep2 == 'yes':
            pointsp2 += (3 * int(threes)) +50
        else:
            pointsp2 += 3 * int(threes)
        bonus = 3 * threes
        bonusp2 += bonus
        openSpacesp2.remove('threes')

    elif chosenSpace.upper() == 'FOURS':
        if 5 in rollNumbers and hasYahtzeep2 == 'yes':
            pointsp2 += (4 * int(fours)) +50
        else:
            pointsp2 += 4 * int(fours)
        bonus = 4 * fours
        bonusp2 += bonus
        openSpacesp2.remove('fours')

    elif chosenSpace.upper() == 'FIVES':
        if 5 in rollNumbers and hasYahtzeep2 == 'yes':
            pointsp2 += (5 * int(fives)) +50
        else:
            pointsp2 += 5 * int(fives)
        bonus = 5 * fives
        bonusp2 += bonus
        openSpacesp2.remove('fives')

    elif chosenSpace.upper() == 'SIXES':
        if 5 in rollNumbers and hasYahtzeep2 == 'yes':
            pointsp2 += (6 * int(sixes)) +50
        else:
            pointsp2 += 6 * int(sixes)
        bonus = 6 * sixes
        bonusp2 += bonus
        openSpacesp2.remove('sixes')

    elif chosenSpace.upper() == 'THREE OF A KIND':
        if 5 in rollNumbers and hasYahtzeep2 == 'yes':
            pointsp2 += sum(rolls) + 50
        elif 3 in rollNumbers or 4 in rollNumbers or 5 in rollNumbers in rollNumbers: 
            pointsp2 += sum(rolls)
        openSpacesp2.remove('three of a kind')

    elif chosenSpace.upper() == 'FOUR OF A KIND':
        if 5 in rollNumbers and hasYahtzeep2 == 'yes':
            pointsp2 += sum(rolls) + 50
        elif 4 in rollNumbers or 5 in rollNumbers: 
            pointsp2 += sum(rolls)
        openSpacesp2.remove('four of a kind')

    elif chosenSpace.upper() == 'FULL HOUSE':
        if 3 in rollNumbers and 2 in rollNumbers:
            pointsp2 += 25
        elif 5 in rollNumbers and hasYahtzeep2 == 'yes':
            pointsp2 += 50
        openSpacesp2.remove('full house')

    elif chosenSpace.upper() == 'SMALL STRAIGHT':
        if (1 in rolls and 2 in rolls and 3 in rolls and 4 in rolls) or (2 in rolls and 3 in rolls and 4 in rolls and 5 in rolls) or (3 in rolls and 4 in rolls and 5 in rolls and 6 in rolls):
            pointsp2 += 30
        elif 5 in rollNumbers and hasYahtzeep2 == 'yes':
            pointsp2 += 50
        openSpacesp2.remove('small straight')

    elif chosenSpace.upper() == 'LARGE STRAIGHT':
        if (1 in rolls and 2 in rolls and 3 in rolls and 4 in rolls and 5 in rolls) or (2 in rolls and 3 in rolls and 4 in rolls and 5 in rolls and 6 in rolls):
            pointsp2 += 40
        elif 5 in rollNumbers and hasYahtzeep2 == 'yes':
            pointsp2 += 50
        openSpacesp2.remove('large straight')

    elif chosenSpace.upper() == 'YAHTZEE':
        if 5 in rollNumbers:
            pointsp2 += 50
            hasYahtzeep2 = 'yes'
        openSpacesp2.remove('yahtzee')

    elif chosenSpace.upper() == 'CHANCE':
        if 5 in rollNumbers and hasYahtzeep2 == 'yes':
            pointsp2 += sum(rolls) + 50
        else:
            pointsp2 += sum(rolls)
        openSpacesp2.remove('chance')

    else:
        print('Input an available space')

    #bonus points
    if bonusp2 >= 63 and claimedp2 != 'yes':
        pointsp2 += 35
        claimedp2 = 'yes'

    if bonusp2 < 63:
        print(p2name, 'your current points is:', pointsp2, 'you have', bonusp2, '/ 63 for bonus points')
        print('-----------------------------------')
        print()
    else:
        print(p2name, 'your current points is:', pointsp2, 'including bonus points')
        print('-----------------------------------')
        print()

    return(pointsp2)

#execute game
while len(openSpacesp1) > 0 and len(openSpacesp2) > 0:
    pointsp1 = yahtzeep1(pointsp1)
    pointsp2 = yahtzeep2(pointsp2)

else:
    if pointsp1 > pointsp2:
        print(p1name, 'wins!')
    elif pointsp2 > pointsp1:
        print(p2name, 'wins!')
    else:
        print("it's a tie!")

time.sleep(5)
    


            
            
            

    
    
                            





