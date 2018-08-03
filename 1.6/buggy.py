import random
nuber1 = random.randint(1, 10)
nuber2 = random.randint(1, 10)
print('Сколько будет: ' + str(nuber1) + '+' + str(nuber2) + '?')
answer = input()
if answer == nuber1 + nuber2:
	print('Верно')
else:
	print('Нет! Правильный ответ - ' + str(nuber1 + nuber2))