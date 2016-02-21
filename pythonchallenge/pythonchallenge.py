BASE_URL = "http://www.pythonchallenge.com/pc/def/"

####################################################
##  Question 1             						  ##
##  http://www.pythonchallenge.com/pc/def/0.html  ##
####################################################

def question1():
	add_to_url = str(2**38)
	url = BASE_URL + add_to_url + ".html"
	return url


print "*******QUESTION 1*******"
print "URL for next page replaces the '0' with the value on the TV screen", question1()
print

#######################################################
##  Question 2                                       ##
##  http://www.pythonchallenge.com/pc/def/map.html   ##
#######################################################

# this phrase and the letter translations as marked below were given
phrase = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

dict_lett = {
	'a' : 'c',
	'b' : 'd',
	'c' : 'e',
	'd' : 'f',
	'e': 'g', # given
	'f' : 'h',
	'g' : 'i',
	'h' : 'j',
	'i' : 'k',
	'j' : 'l',
	'k' : 'm', # given
	'l' : 'n',
	'm' : 'o',
	'n' : 'p',
	'o': 'q', # given
	'p' : 'r',
	'q': 's',
	'r' : 't',
	's' : 'u',
	't' : 'v',
	'u' : 'w',
	'v' : 'x',
	'w' : 'y',
	'x' : 'z',
	'y' : 'a',
	'z' : 'b',
}



def question2(dict_lett, phrase):
	new_phrase = list(phrase)

	for i in range (0, len(new_phrase)):
		if new_phrase[i] in dict_lett:
			new_phrase[i] = dict_lett[new_phrase[i]]

	return ''.join(new_phrase)

print "*******QUESTION 2*******"
print "This is the translation of the code:"
print question2(dict_lett, phrase)
print "To get to the next url, I encoded the last three letters in the current url:"
print " m -> o, a -> c, p -> r, which gives us: http://www.pythonchallenge.com/pc/def/ocr.html"
print

#########################################################
##  Question 3                                         ##
##  http://www.pythonchallenge.com/pc/def/ocr.html     ##
#########################################################

# stored the large number of characters in a seperate file to reduce clutter
import python_challenge_q3 as pcq3

def count_chars(char_list):
	# Using a dictionary for this initially because I need a mutable value
	# for the count (value) attached to a unique character (key)
	dict_count_chars = {}
	for char in char_list:
		if char in dict_count_chars:
			dict_count_chars[char] = dict_count_chars[char] + 1
		else:
			dict_count_chars[char] = 1

	# Changing this into a list of tuples so I can sort by the dict value
	sorted_list_tuples = sorted(dict_count_chars.items(), key=lambda x:x[1])
	
	# As there's not a definition of 'rare values' in the question
	# decided to use average; this is better than median because it will reflect
	# much lower or higher instances of a number.  I can see that the letters are 
	# the rarest characters visually, but wanted to derive them programmatically.

	average_count = sum(dict_count_chars.values())/len(dict_count_chars)

	rare_characters = []

	for tuples in sorted_list_tuples:
		if tuples[1] < average_count:
			rare_characters.append(tuples[0])

	# This includes a '/n' which is an escape character, showing up because I put 
	# the original characters into triple quotes -- I think that added the '\n'

	# I observed that all of the rare characters are alpha characters, tried a few  
	# combinations and anagrams I could think up myself, but didn't work.
	# Wrote this loop finds to find the original order

	alpha_in_order = []

	for char in char_list:
		if char.isalpha():
			alpha_in_order.append(char)

	return alpha_in_order

print "*******QUESTION 3*******"
print "The 'rare characters' in this collection are all letters (one instance each)."
print 
print "When you arrange them in order, you get '", ''.join(count_chars(pcq3.chars)), "'."
print "The next url is:", BASE_URL + ''.join(count_chars(pcq3.chars)) + ".html"

print "*******QUESTION 3*******"
