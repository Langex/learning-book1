import random
import time

def displayIntro():
	print('''Вы находитесь в землях, заселенных драконами.
		Перед собой вы видете две пещеры. В одной из них - дружелюбный дракон,
		который готов поделится с вами своими сокровищами. Во второй - 
		жадний и голодный дракон, который мигом вас сьест''')
	print()

def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print ('В какую пещеру вы войдете? (нажмите клавишу 1 или 2)')
		cave = input()

	return cave

def checkCave(chosenCave):
        print('Вы приближаетесь к пещере...')
        time.sleep(2)
        print('Ее темнота заставляет вас дрожать от страха...')
        time.sleep(2)
        print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...')
        print()
        time.sleep(2)

        friendlyCave = random.randint(1, 2)
        if chosenCave == str(friendlyCave):
                print('...делиться с вами своими сокровищами!')
        else:
                print('...моментально вас сьедает!')

def main():
        playAgain = 'да'
        while playAgain == 'да' or playAgain == 'д':
                displayIntro()
                caveNumder = chooseCave()
                checkCave(caveNumder)

                print('Попытаете еще раз? (да или нет)')
                playAgain = input()

main()
