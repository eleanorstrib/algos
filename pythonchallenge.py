#############################
##  Question 2             ##
##                         ##
#############################

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


print question2(dict_lett, phrase)

#############################
##  Question 3             ##
##                         ##
#############################

import python_challenge_q3 as pcq3

def count_chars(char_list):
	dict_count_chars = {}
	for char in char_list:
		if char in dict_count_chars:
			dict_count_chars[char] = dict_count_chars[char] + 1
		else:
			dict_count_chars[char] = 1
	return dict_count_chars

print count_chars(pcq3.chars)


