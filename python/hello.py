import random

#numbers
x = 5
y = 10L
print (x+y)

#char
c = "p"
x = str(x) + "-men"
print x

#string : https://www.tutorialspoint.com/python/python_strings.htm
s = "Pathik Sharma"
print s
print s[3:5]
print s[5:]
print s + "'s"
print s * 2
str="pathik sharma is my name"
print "number of times 'a' comes is:",str.count('a')
stra = str.split(" ", 2)
print stra

#list
list = ['pat', 7 , 'shar', 9.98, 'true', 'false']
print list
#list[start:end:jump]
print list[::-1] # reverse order by 1
print list[3::2] # start from 3 and print alternate
print list[:4]
list [1] = 1000 # updating values
print list
random.shuffle(list)
print "random list -->",list
list1 = ['a','z','c']
list2 = ['a','z','c']
#if first element is greater -> 1
#if first element is smaller -> -1
#if perfect math -> 0
print "comparing list1 and 2 -->",cmp(list1,list2)
print len(list1)
print list1[1] #get value at index
print list1.index('z') #get indes for a value
list1.append('last val')
list1.insert(1, 'insertedat1')
print list1
list1.pop() #opposite of append
print list1
list1.remove('z')
list1.reverse()
print "list 1 reversed -->",list1
list1.sort()
print "list 1 sorted -->",list1
list1.extend(list2)
print list1
print "number of a in list -->",list1.count('a')

#same as list but () instead of [] and its values cannot be updated. Its RO
tuple = ('pat', 7 , 'shar', 9.98) 

#dictionary
dict = {1:"one",2:"two"}
print dict[2]
print dict.keys()
print dict.values()
del dict[2]
dict[3] = "three"
print dict
dictcopy = dict.copy()
print dictcopy
keylist = ["file1","file2","file3","file4"]
#create a new dic from list as key and assign 0 as default val
dict2 = dict.fromkeys(keylist,0)
print dict2
print "get value from index", dict2.get("file1"), dict2["file1"]
print "has key", dict2.has_key("file5")
dict.update(dict2)
print dict

print ("Hello world")
#raw_input("\n\npress enter to exit the code")

var = 7 
if var==1:
	print "False"
elif var==7:
	print "the value is 7"
else:
	print "O or null constitute as false"

num = 7
while num != 10:
	num += 1
	print "Enter 10 to exit. num entered",num


for num in range(10,20,2):
	for i in range(2, num):
		if num%i == 0:
			j=num/i
			print "%d * %d = %d"%(i,j,num) 
			break
	else :
		print  "%s is prime"%(num)

x = int (random.random()*100)
print x

def sum(var1, var2=9):
	"this function sums 2 variable"
	sum = var1 + var2
	return sum

print sum(1,2)
print sum(1)


