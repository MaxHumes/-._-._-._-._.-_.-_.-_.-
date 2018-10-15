import re

def translateText(text):
	wordList = re.sub("[^\w]", " ",  text).split()

	output = ''
	for word in wordList:
		output += translateWord(word) + ' '

	return output

def translateWord(word):
	vowels = 'aeiou'

	if word[0] in vowels:
		return word + 'yay'

	ending = ''
	i = 0
	while word[i] not in vowels  + 'y':
		ending += word[i]
		i += 1

	return word[i:] + ending + 'ay'