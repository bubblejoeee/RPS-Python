import random

print('ROCK,PAPER,SCISSORS GAME by ben🔥✊✋✌')
print("Type 'rock', 'paper','scissors' to play or 'quit' to exit game")

#VARIABLES
user_score = 0
opponent_score = 0
rounds = 1
max_rounds = 0

#LOGICS FOR PLAY STATE
def play() :
	global rounds,opponent_score,user_score,max_rounds
	rps = ['rock','paper','scissors']

	#PLAY IF THE MAX ROUND ISN'T YET REACHED'
	if rounds <= int(max_rounds) :
		print(f'---📢Round {rounds}📢---')
		
		#END PROGRAM IF THE USER INPUTS 'EXIT'
		user_choice = input('>>> ').lower()		
		if user_choice == 'quit' :
			print('Thanks for playing😘')
		#NOTIFY IF INPUT IS INVALID
		elif user_choice not in rps :
			print('Invalid input. Plase type rock,paper, or scissors or quit')
			play()
		#LOGICS
		else :
			opponent = random.choice(rps)
			print(f"Opponent played '{opponent}'")
			if (user_choice == 'rock' and opponent == 'rock') or (user_choice == 'scissors' and opponent == 'scissors') or (user_choice == 'paper' and opponent == 'paper') :
			    print('--DRAW!😳')
			elif (user_choice == 'rock' and opponent == 'paper') or (user_choice == 'paper' and opponent == 'scissors') or (user_choice == 'scissors' and opponent == 'rock') :
			    print('--You Lose!😞')
			    opponent_score += 1
			elif (user_choice == 'rock' and opponent == 'scissors') or (user_choice == 'paper' and opponent == 'rock') or (user_choice == 'scissors' and opponent == 'paper') :
			    print('--You Win!😍')
			    user_score += 1
			rounds += 1
			print(f'[Your score: {user_score}]')
			print(f"[Opponent's score: {opponent_score}]")
			play()
		
	#PRINTS GAMEOVER IF MAXROUNDS IS REACHED
	else:
		print('_____________________')
		print('----📣Game Over📣----')
		print(f'Your final score: {user_score}')
		print(f"Opponent's final score: {opponent_score}")
		if user_score > opponent_score :
			print('You are the CHAMPION!🏆')
		elif user_score == opponent_score :
			print('Draw!😩')
		else :
			print('Awit, nextgame lods💀')
			
		#TELL IF WANTS TO PLAY MORE
		print('_____________________')
		print('Play again?🎮')
		play_again = input("Any keys for Yes. Otherwise 'No': ").lower()
		if play_again == 'no' :
			print('Thanks for playing☺')
		else :
			print('Yun oh..😎')
			user_score = 0
			opponent_score = 0
			rounds = 1
			define_rounds()
	
#THE FUCTION TO DEFINE MAXROUNDS THAT WILL BE CALLED BELOW
def define_rounds() :
	global max_rounds
	print('_____________________')
	print('How many rounds do you like')
	max_rounds = input('>>> ')
	if max_rounds == 'quit' :
		print('Eh?😶')
	#INVALIDATE IF NOT A NUMBER
	elif max_rounds.isnumeric() == False :
		print('Invalid input. Please type a number only😡')
		define_rounds()
	#INVALIDATE IF LESS THAN 1
	elif int(max_rounds) <= 0 :
		print('Invalid input. Must be greater or equal to 1😑')
		define_rounds()
	else :
		#STARTS THE PLAYSTATE
		play()

#THIS IS TO START THE GAME
define_rounds()