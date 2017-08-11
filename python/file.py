import os

print os.getcwd()

# more file methods: https://www.tutorialspoint.com/python/file_methods.htm
fo = open ("testfile.txt","w+")
fo.write("test1.20170701.log\ntest2.20170601.log");
fo.seek(0,0)
names = fo.read()
print names
fo.close()
os.rename("testfile.txt","testfile1.txt")
os.rename("testfile1.txt","testfile.txt")
#list all files in current directory
print os.listdir("/Users/psharma/workspace/python files/")
print os.listdir(".")

try: 
	fo1 = open ("testfile1","r")
	content = fo1.read()
	print content 
	fo.close()
except IOError:
	print "no such file exist"
except Exception:
	print "error"
