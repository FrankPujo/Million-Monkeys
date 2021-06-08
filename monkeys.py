import random
import os

letters = "abcdefghijklmnopqrstuvwxyz"

def rL():
	return random.choice( letters )

word = [ "h", "e", "l", "l", "o" ]
i = 0
j = 0

while ( True ):
	if ( i == len( word ) ):
		print( "\033[0m", end="")
		print( "\nWord found after:", j, "letters!")
		break
	letter = rL()
	j = j + 1
	if letter == word[i]:
		i = i + 1
		print( "\033[31m", end="" )
	else:
		i = 0
		print( "\033[0m", end="")
	print( letter, end=" ")
