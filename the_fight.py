# made by Alexander Vasilkov, IKT-13
# inspired by the "Fight Club" movie
# Adults only. No one under 17 admitted
# Street Fighting v.0.2b

# greeting, rules and some info about the game
print('Hello! Welcome to the game called \'Street Fighting\' v.0.2a')
print('It is about to help you to decide who will go for the beer: you or your partner')
print('\nHere are some rules:\n* Only two fighters\n* Do not hit below the belt\n* Do not bite each other\n* No shirts, no shoes\n* Fight will go on as long as it have to\n* If you lose, you have to go for a beer')

# call the needed functions
from random import randint
from time import sleep
from os import system
import platform

# defining the array of names; we're going to use 2
player_names = []

# the array of strikes made
strikes_made = [0, 0]

#defining the list that holds our players's health
player_health = [100, 100]

# making the player to read the rules
raw_input('\nPress enter when you are ready (do not break the rules!)...')

# starting phrase
print('\nSo, let\'s make some preparations before')
sleep(0.5) # pausing the script to make the wow-effect

# time to ask for the names
player_names.append(raw_input('\nEnter the name of the first fighter:\n'))
print('\nGood Job!')
sleep(0.5) # pause. pause. pause...
player_names.append(raw_input('\nNow it\'s time to enter the name of the second fighter:\n'))
print('Now, we are fully prepared!')

# clearing the output window
if platform.system() == 'Windows':
	system('cls')
else:
	system('clear')

# countdown
def countdown():
	sleep(1)
	print('3')
	sleep(1)
	print('2')
	sleep(1)
	print('1')
	sleep(1)
	print('The fight starts!\n')

# returns random damage
def damage():
	return randint(10, 25)

# returns random amount of health restored (while drinking herbal tea)
def healing():
	return randint(10, 20)

# how the fighters think
def artificial_intelligence(myself, enemy):
	hit = damage()
	# maybe it's time for some Red Bull? To make the hit stronger.
	if player_health[enemy] > 0 and randint(0, 4) == 2:
		hit *= 1.5
		print player_names[myself] + ' just drunk Red Bull and his hit damage for now is myltiplied by 1.5!'
	# the hit
	player_health[enemy] -= hit
	print player_names[myself] + ' caused ' + str(hit) + ' damage to ' + player_names[enemy]
	strikes_made[myself] += 1
	# time for healing?
	if player_health[myself] <= 80 and player_health[enemy] > 0 and randint(0, 2) == 1:
		hp_healed = healing()
		player_health[myself] += hp_healed
		print player_names[myself] + ' just drunk some herbal tea and restored ' + str(hp_healed) + ' health!'
	if player_health[0] <= 0:
		print player_names[0] + '\'s current hp is ' + 'zero or less. He is gonna lose the fight'
	else:
		print player_names[0] + '\'s current hp is ' + str(player_health[0])
	if player_health[1] <= 0:
		print player_names[1] + '\'s current hp is ' + 'zero or less. He is gonna lose the fight'
	else:
		print player_names[1] + '\'s current hp is ' + str(player_health[1])

# we remember about the fight, so here it is
def the_fight():
	
	# while somebody can fight, he must do it (yeah, too violently)
	while player_health[0] >= 0 and player_health[1] >= 0:
		sleep(1) # some pause for intrigue
		# it's time to determine who will strike 
		striker = randint(0, 1)
		if striker:
			artificial_intelligence(1, 0)
		else:
			artificial_intelligence(0, 1)
		print '***'
	# who's the winner? and who will go for a beer? ;)
	if player_health[0] > 0:
		winner = 0
	else:
		winner = 1 
	print '\nAfter the great battle, we\'ve got a winner! And his name is ' + player_names[winner] + '.\nHe beated the opponent with ' + str(strikes_made[winner]) + ' strikes.' 
	print player_names[abs(winner - 1)] + ', don\'t forget to bring some beer to your opponent. Rules are rules ;)'

# the main part
countdown()
the_fight()

# just not to quit too early
raw_input('\nPress any key to exit...')

