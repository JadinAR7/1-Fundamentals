""" import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []


while diamonds:
    selection = input('Press enter to pick a card or Q to quit ')
    if selection == 'Q' or selection == 'q':
        print('Goodbye!')
        break
    elif selection == 'Enter':
        random_card = random.choice(diamonds)
        hand.append(random_card)
        diamonds.pop(random_card)
        print('this is your hand: ' + str(hand))
        print('remaining cards:' + str(diamonds))
        if not diamonds:
            print('There are no more cards to pick') """

""" myString = 'Giraffe'
print(myString[2:-2]) """