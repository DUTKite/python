def break_words(stuff):
	"""This function will break up words for us."""   #帮助文档（文档注解）
	words = stuff.split(" ")
	#python split()方法：通过指定的分隔符对字符中进行切片，
	#split()有两个参数比如，str.split(" ", 2)可以这样理解，
	#把str按空格分隔一次，返回列表格式，
	#代码中没有数字参数，就是分隔到底
	return words
	
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)      #排序（升序）；降序排列方法reverse()
	
def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)  
	#从列表中移除并返回第一个对象（0），参数可以选择对象的索引，
	#第一个对象被返回且被删除
	print word
	
def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	#从列表中移除并返最后一个对象（-1），最后一个对象被返回且被删除
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

break_sentence = break_words(sentence)
sort_words_of_sentence = sort_words(break_sentence)
print_first_word_of_sentence = print_first_word(break_sentence) 
print_last_word_of_sentence = print_last_word(break_sentence) 


print "the sentence is: " + sentence
print "the break sentence is: " + break_sentence
print "the sorted words of sentence is: " + sort_words_of_sentence
print "print first word of sentence: " + print_first_word_of_sentence
print "print last word of sentence: " + print_last_word_of_sentence
print sort_sentence(sentence)
print print_first_and_last(sentence)
print print_first_and_last_sorted(sentence)