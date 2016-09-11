import time
import sys
import os

print "STARTING Your Custom Counter - Down"


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


#Test arguments
count = sys.argv[1]



if is_number(count):
	count = int(float(count))
	print "STARTING Your Custom Counter"
	print ""
else: 
	print "You did not enter a number"
	sys.exit()

while count !=0:
	print count
	time.sleep(1)     #Sleep for 1 second
	count = count - 1
	if count%30 == 0:
		print "Almost there"
		os.system("tree ~/code")






