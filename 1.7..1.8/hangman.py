import random		
HANGMAN_PICS = ['''		
	  +---+		
	      |		
	      |		
	      |		
	     ===''', '''		
	  +---+		
	  O   |		
	      |		
	      |		
	     ===''', '''		
	  +---+		
	  O   |		
	  |   |		
	      |		
	     ===''', '''		
	  +---+		
	  O   |		
	 /|   |		
	      |		
	     ===''', '''		
	  +---+		
	  O   |		
	 /|\  |		
	      |		
	     ===''', '''		
	  +---+		
	  O   |		
	 /|\  |		
	 /    |		
	     ===''', '''		
	  +---+		
	  O   |		
	 /|\  |		
	 / \  |		
	     ===''']
words = '''аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра
 голубь гусь жаба зебра змея индюк кит кобра коза койот корова кошка кролик крыса
 курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул
 муравей мышь норка носорог обезьяна овца окунь олен орел осел панда паук питон
 попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха
 ястреб ящерица'''.split()