import random

# Character names
wizard = 'Wizard'
warrior = 'Warrior'
elf ='Elf'
archer = 'Archer'

#oppenent name
jadin = 'Jadin'
dragon = 'Dragon'
goblin = 'Goblin'
troll = 'Troll'

# Opponent health points
jadin_health = 1000
dragon_health = 800
goblin_health = 600
troll_health = 700

# Opponent attack points
jadin_attack = 100
dragon_attack = 80
goblin_attack = 60
troll_attack = 70


# Character health points
wizard_health = 120
warrior_health = 150
elf_health = 115
archer_health = 105

# Character attack points
jadin_attack = 100
wizard_attack = 50
warrior_attack = 70
elf_attack = 60
archer_attack = 40

# choose you role
print(wizard, ':press 1')
print(warrior, ':press 2')
print(elf, ':press 3')
print(archer, ':press 4')

opponents = [jadin,dragon,goblin,troll]
opponent = random.choice(opponents)

role = int(input('\nChoose your role:'))


while True:
    if role == 1:
        print('\nYou chose', wizard, 'with', wizard_health, 'health points and', wizard_attack, 'attack points.')
    elif role == 2:
        print('\nYou chose', warrior, 'with', warrior_health, 'health points and', warrior_attack, 'attack points.')
    elif role == 3:
        print('\nYou chose', elf, 'with', elf_health, 'health points and', elf_attack, 'attack points.')
    elif role == 4:
        print('\nYou chose', archer, ' with', archer_health, 'health points and', archer_attack, 'attack points.')
    else:
        print('\nInvalid option. Please choose a different role.')
        break

    if opponent == jadin:
        opponent_health = jadin_health
        opponent_attack = jadin_attack
        print('\nYou are facing', opponent, 'with', jadin_health, 'health points and', jadin_attack, 'attack points.')
    elif opponent == dragon:
        opponent_health = dragon_health
        opponent_attack = dragon_attack
        print('\nYou are facing', opponent, 'with', dragon_health, 'health points and', dragon_attack, 'attack points.')
    elif opponent == goblin:
        opponent_health = goblin_health
        opponent_attack = goblin_attack
        print('\nYou are facing', opponent, 'with', goblin_health, 'health points and', goblin_attack, 'attack points.')
    elif opponent == troll:
        opponent_health = troll_health
        opponent_attack = troll_attack
        print('\nYou are facing', opponent, 'with', troll_health, 'health points and', troll_attack, 'attack points.')

    print('\nThe battle begins!')

    special_attacks = {'Lightning': 1000, 'Fireball': 800, 'Arrow': 200, 'swordSlash': 170}
    special_attackk = random.choice(list(special_attacks.keys()))
    special_damage = special_attacks[special_attackk]
    while True:
        if role == 1:
            opponent_health -= wizard_attack
            print('\nYou attacked', opponent, 'for', wizard_attack, 'damage.')
            print('\n', opponent, 'now has', opponent_health, 'health points.')
            wizard_health -= opponent_attack
            print('\n', opponent, 'attacked you for', opponent_attack, 'damage.')
            print('\nYou now have', wizard_health, 'health points.')
            if wizard_health < 62 and wizard_health > 0:
                print('Do you want to use a special attack?')
                yes_no = input('y or n: ')
                if yes_no.lower() == 'y':
                    opponent_health -= special_damage
                    print('\nYou used', special_attackk, 'on', opponent, 'for', special_damage, 'damage.')
                    print('\n', opponent, 'now has', opponent_health, 'health points.')
            if wizard_health <= 0:
                print('\nYou have been defeated by', opponent, '!')
                break
            elif opponent_health <= 0:
                print('\nYou have defeated', opponent, '!')
                break
        elif role == 2:
            opponent_health -= warrior_attack
            print('\nYou attacked', opponent, 'for', warrior_attack, 'damage.')
            print('\n', opponent, 'now has', opponent_health, 'health points.')
            warrior_health -= opponent_attack
            print('\n', opponent, 'attacked you for', opponent_attack, 'damage.')
            print('\nYou now have', warrior_health, 'health points.')
            if warrior_health < 62 and warrior_health > 0:
                print('Do you want to use a special attack?')
                yes_no = input('y or n: ')
                if yes_no.lower() == 'y':
                    opponent_health -= special_damage
                    print('\nYou used', special_attackk, 'on', opponent, 'for', special_damage, 'damage.')
                    print('\n', opponent, 'now has', opponent_health, 'health points.')
            if warrior_health <= 0:
                print('\nYou have been defeated by', opponent, '!')
                break
            elif opponent_health <= 0:
                print('\nYou have defeated', opponent, '!')
                break
        elif role == 3:
            opponent_health -= warrior_attack
            print('\nYou attacked', opponent, 'for', warrior_attack, 'damage.')
            print('\n', opponent, 'now has', opponent_health, 'health points.')
            warrior_health -= opponent_attack
            print('\n', opponent, 'attacked you for', opponent_attack, 'damage.')
            print('\nYou now have', warrior_health, 'health points.')
            if warrior_health < 62 and warrior_health > 0:
                print('Do you want to use a special attack?')
                yes_no = input('y or n: ')
                if yes_no.lower() == 'y':
                    opponent_health -= special_damage
                    print('\nYou used', special_attackk, 'on', opponent, 'for', special_damage, 'damage.')
                    print('\n', opponent, 'now has', opponent_health, 'health points.')
            if warrior_health <= 0:
                print('\nYou have been defeated by', opponent, '!')
                break
            elif opponent_health <= 0:
                print('\nYou have defeated', opponent, '!')
                break
        elif role == 4:
            opponent_health -= warrior_attack
            print('\nYou attacked', opponent, 'for', warrior_attack, 'damage.')
            print('\n', opponent, 'now has', opponent_health, 'health points.')
            warrior_health -= opponent_attack
            print('\n', opponent, 'attacked you for', opponent_attack, 'damage.')
            print('\nYou now have', warrior_health, 'health points.')
            if warrior_health < 62 and warrior_health > 0:
                print('Do you want to use a special attack?')
                yes_no = input('y or n: ')
                if yes_no.lower() == 'y':
                    opponent_health -= special_damage
                    print('\nYou used', special_attackk, 'on', opponent, 'for', special_damage, 'damage.')
                    print('\n', opponent, 'now has', opponent_health, 'health points.')
            if warrior_health <= 0:
                print('\nYou have been defeated by', opponent, '!')
                break
            elif opponent_health <= 0:
                print('\nYou have defeated', opponent, '!')
                break

    if wizard_health <= 0 or opponent_health <= 0:
        break
    elif warrior_health <= 0 or opponent_health <= 0:
        break
    elif elf_health <= 0 or opponent_health <= 0:
        break
    elif archer_health <= 0 or opponent_health <= 0:
        break




