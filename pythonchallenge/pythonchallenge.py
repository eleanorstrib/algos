BASE_URL = "http://www.pythonchallenge.com/pc/def/"

####################################################
##  Question 0            						  ##
##  http://www.pythonchallenge.com/pc/def/0.html  ##
####################################################

def power():
	add_to_url = str(2**38)
	url = BASE_URL + add_to_url + ".html"
	return url


print "*******QUESTION 0*******"
print "URL for next page replaces the '0' with the value on the TV screen", power()
print
print "***********************"
print

#######################################################
##  Question 1                                       ##
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



def mapping(dict_lett, phrase):
	new_phrase = list(phrase)

	for i in range (0, len(new_phrase)):
		if new_phrase[i] in dict_lett:
			new_phrase[i] = dict_lett[new_phrase[i]]

	return ''.join(new_phrase)

print "*******QUESTION 1*******"
print "This is the translation of the code:"
print mapping(dict_lett, phrase)
print "To get to the next url, I encoded the last three letters in the current url:"
print " m -> o, a -> c, p -> r, which gives us: http://www.pythonchallenge.com/pc/def/ocr.html"
print
print "***********************"
print

#########################################################
##  Question 2                                         ##
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

print "*******QUESTION 2*******"
print "The 'rare characters' in this collection are all letters (one instance each)."
print 
print "When you arrange them in order, you get '", ''.join(count_chars(pcq3.chars)), "'."
print "The next url is:", BASE_URL + ''.join(count_chars(pcq3.chars)) + ".html"
print
print "***********************"
print

############################################################
##  Question 3                                            ##
##  http://www.pythonchallenge.com/pc/def/equality.html   ##
############################################################
import python_challenge_q4 as pcq4

def candles(big_string):
	# paired on this one with github.com/kb0rg!
	# interpreting small as lower case and bodyguards and uppercase
	# looking for this sequence lUUUlUUUl (exactly 3 bodyguards on each side, 9 characters)
	candidates = []

	# remove escape characters
	big_string = big_string.replace('\n', '')
	ind=0
	for char in big_string:
		if char.islower():
			if big_string[ind+1:ind+4].isupper():
				if big_string[ind+4].islower():
					if big_string[ind+5:ind+8].isupper():
						if big_string[ind+8].islower():
							candidates.append(ind+4)
				
		ind = ind+1
	return candidates

print "*******QUESTION 3*******"
print "Looked for a pattern: one lowercase letter, followed by 3 uppercase, followed by 1 lowercase,"
print "followed by 3 uppercase."
print "When this was run, it provided an array of letters following this pattern."
print "The middle, lowercase letters from each chunk spelt:", candles(pcq4.chars4)
print
print "Adding this string to the url got us to a page that simply said 'linkedlist.php'."
print "This url led to the next step:", BASE_URL + "linkedlist.php."
print
print "***********************"
print


############################################################
##  Question 4                                            ##
##  http://www.pythonchallenge.com/pc/def/linkedlist.php  ##
############################################################

import urllib2

def chainsaw():
	#number shown when moused over or clicked on picture
	num="12345"
	# dict to hold responses and values for number
	num_dict={}
	# clue said that 400 times was more than enough
	# this loop uses the "num" value to get the response for each page 
	# extract the digit, which becomes the new 'num' and put it into a dict
	# observed that each value occurred one or two times first, then looked at responses
	for x in range(401):
		response = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + num)
		html = response.read()
		num = ''.join([str(i) for i in html.split() if i.isdigit()])
		num_dict[num] = num_dict.get(num, "") + html
	return num_dict['']

print "*******QUESTION 4*******"
print "The picture was the key here -- if you moused over or clicked, you went to the url:"
print "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345."
print "Following it was fruitless, but there was a comment in the html file saying 400x was more than enough"
print "and urllib would be helpful.  Discovered that the responses held the key -- for the value '' message was:  "
print chainsaw()
print 
print "Trying", BASE_URL + "peak.html was the correct answer."
print
print "***********************"
print

############################################################
##  Question 5                                            ##
##  http://www.pythonchallenge.com/pc/def/equality.html   ##
############################################################
import pickle

def pickle():
	file = open('ptext.txt', 'r')
	decoded = pickle.load(file)
	return decoded

print pickle()

