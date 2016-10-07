def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(" ")
	return words
	
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)      
	
def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)  
	return word
	
def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	return word
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	first_word = print_first_word(words)
	last_word = print_last_word(words)
	return  first_word, last_word
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	first_word = print_first_word(words)
	last_word = print_last_word(words)
	return  first_word, last_word
	
sentence = "All good things come to those who wait."
print "the sentence is: " + sentence

break_sentence = break_words(sentence)
print "the break sentence is: " + str(break_sentence)

sort_words_of_sentence = sort_words(break_sentence)
print "the sorted words of sentence is: " + str(sort_words_of_sentence)

print_first_word_of_sentence = print_first_word(break_sentence) 
print "print first word of sentence: " + str(print_first_word_of_sentence)

print_last_word_of_sentence = print_last_word(break_sentence) 
print "print last word of sentence: " + str(print_last_word_of_sentence)


print "print sort sentence: " + str(sort_sentence(sentence))
print "print print first and last word of sentence: " + str(print_first_and_last(sentence))
print "print print first and last sorted word of sentence: " + str(print_first_and_last_sorted(sentence))
