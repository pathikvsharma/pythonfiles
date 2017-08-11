import re
from datetime import date
import random

def when100(name, age):
	"when will you reach 100?"
	print "Your name is %s and your age is %d" % (name,age)
	rem_years = 100 - age
	curr_year = date.today().year
	print "you will be 100 years in", rem_years + curr_year

def lessThanNum(alist, num = 5):
	"Number less than 5 are"
	blist = []
	for r in alist:
		if r < num:
			blist.append(r)
	return blist
			
def printCommon(a,b):
	"print common from both lists"
	common = []
	for num in a:
		if num in b and num not in common:
				common.append(num)

	return common

def randomlist(a):
	listlength = random.randint(1,10)
	listresult = []

	for i in range(0,listlength):
		listresult.append(random.randrange(0,100))
	return listresult

def palindrome(s):
	"To check if its a palindrome or not"
	s = s.replace(" ","") #strip all spaces
	length = len(s)
	print s,length
	for i in range(0,length/2):
		if (s[i] == s[length - i - 1]):
			continue
		else:
			return "false"
	return "true"

def evenlist(b):
	"To pring just even numbers from list"
	even = [i for i in b if i%2==0]
	return even

def rockPaperScissor():
	"Rock Paper Scissor game r>s s>p p>r"
	humancnt = computercnt = 0
	while (True):
		human = ''
		game = ['r','p','s']
		invalid = True
		while (invalid):
			human = raw_input("your pick: (r,p,s)")
			if human == "zz":
				return
			elif human not in game:
				print "invalid input"
				continue
			else: invalid = False
		
		computer = random.choice(game)
		print "computer picked:", computer
	
		if (human == 'r' and computer == 's') or \
			(human == 's' and computer == 'p') or \
		     (human == 'p' and computer == 'r'):
			print "You won!!"
			humancnt +=1
		elif human == computer:
			print "This game is a tie :/"
		else:
			print "You lost :("
			computercnt+=1
		print "Scores: \n Human : %d \n Computer : %d \n To exit press zz anytime"%(humancnt,computercnt)

def rockPaperScissorComputer():
	"Rock Paper Scissor game r>s s>p p>r"
	humancnt = computercnt = 0
	i = 0
	while (i<1000):
		game = ['r','p','s']
		invalid = True
		
		human = random.choice(game)
		computer = random.choice(game)
		print "computer picked:", computer
	
		if (human == 'r' and computer == 's') or \
			(human == 's' and computer == 'p') or \
		     (human == 'p' and computer == 'r'):
			print "You won!!"
			humancnt +=1
		elif human == computer:
			print "This game is a tie :/"
		else:
			print "You lost :("
			computercnt+=1
		try:
			print "Scores: \n Human : %d (%f) \n Computer : %d (%f) \n To exit press zz anytime"%(humancnt, (float (humancnt)*100)/(float (humancnt) + float (computercnt)),computercnt,(float (computercnt)*100)/(float (humancnt) + float (computercnt)))
		except Exception:
			print "First game was tie :/ run the program again!"
		i+=1


def fibonacci(n = 10):
	"Print fibonacci list"
	fiboList = []
	first = 1
	second = 1
	if n < 1: print "nothing in fiboList"
	fiboList.append(first) 
	if n < 2: 
		return fiboList
	fiboList.append(second) 
	if n < 3:
		return fiboList
	i = 3
	while (i<=n):
		third = first + second
		fiboList.append(third)
		first = second
		second = third
		i+=1
	return fiboList

def reverseWords(s):
	words = s.split(" ")
	length = len(words)
	print length
	revWords = []
	for i in range(length-1,-1,-1):
		revWords.append(words[i])
	return revWords

def randomPasswordGenerator(n = 12):
	lower = 'abcdefghijklmnopqrstuvwxyz'
	upper = lower.upper()
	digits = '1234567890'
	punctuation = '@#$!*'
	u = lower + upper + digits + punctuation
	print u

	password = ''

	password = password + (str(random.sample(lower,1)))+ \
	                       str(random.sample(upper,1)) + \
	                       str(random.sample(digits,1)) + \
	                      str(random.sample(punctuation,1))
	
	length = len(password)
	password = password + str(random.sample(u,8))
	print str(password)
	return

def cowsAndBulls():
	'''To print how many cows and bulls are there 
	currect number at correct position = cow
	currect number at incorrect position = bull
	user guesses and program matches with computer generated'''
	cows = bulls = tries = 0
	
	comp = str (random.randint(1000,9999))
	comp = list (comp)
	while (True):
		human = list (raw_input("write a 4 digit number\n"))
		if (len(human)!=4): 
			print ("invalid number") 
			return
		humantemp = human
		comptemp = comp
		print humantemp, comptemp
		for i in range(0,4,1):
			if humantemp[i] == comptemp[i]:
				cows+=1
				humantemp[i] = 'm'
				comptemp[i] = 'n'
		print humantemp, comptemp
	
		for i in range(0,4,1):
			for j in range(0,4,1):
				if humantemp[i] == comptemp[j]:
					bulls+=1
					humantemp[i] = 'm'
					comp[j] = 'n'
		print humantemp,comptemp
		print "cows, bulls" , cows,bulls
		tries += 1
		cows = bulls = 0
		humantemp = comptemp = []
		if cows + bulls == 4: 
			print "number of tries", tries
			return
	


#to print numbers less than 5
alist = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#to print common
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
l = []

	
def main():
	#print "name is pathik"
	when100("Pathik", 27)
	print lessThanNum(alist, 9)
	print printCommon(a,b)
	print randomlist(l)
	print palindrome("race car")
	print evenlist(randomlist(l))
	print fibonacci()
	#rockPaperScissor()
	print reverseWords("my name is apthil")
	randomPasswordGenerator()
	#rockPaperScissorComputer()
	cowsAndBulls()

if __name__ == "__main__":
	main()