import random as rnd
import sys

#===========DEFINE ALL THE NECCESARY COMMANDS============
#these must appear in this order
order = [
r"co='from math ';",
r"exec('import os  ');",
r"exec(co+'import sqrt ');",
r"w='me=';"
r"x='os.path.';",
r"y='realpath';",
r"z='(__file__)';",
r"exec(w+x+y+z);",
r"f=open(me);",
r"s=f.read();"]

#these can be interspersed in 'order' in any order
anys = [\
r'spa=0.0;',
r'i=0;',
r'fll=0.0;',
r"o='Pi~%f';",
r"a='while(i<len(s)):\n\t';",
r"newL='\n';",
"b='if(s[i]==\\'\"\\' ';",
r"c='or s[i]==newL):';",
r"d='elif(s[i]==\'|\'):';",
r"e='spa+=1\n\t';",
r"f='else:fll+=1\n\t';",
r"g='i+=1';",
r"h='pass\n\t';"]

#these must appear in this order, after everything above
lasts = [\
"d1=a+b+c+h;",
"d2=d+e+f+g;",
"exec(d1+d2);",
"fll+=2;"
"spa-=1;",
"squ=spa+fll;",
"rad=sqrt(squ/4)-.5;",
"pi=fll/(rad)**2;",
"re=o%pi;",
"print(re);"]


#==========PROGRAM WRITER HELPERS======================
def nl(f):
	f.write("\n")

#=========GENERATE TEST PROGRAM========================
def writeTestProgram():
	f=open("test.py","w")
	for line in inits:
		f.write(line)
		nl(f)
	for line in anys:
		f.write(line)
		nl(f)
	for line in finals:
		f.write(line)
		nl(f)

#=======FORMAT THE GENERATION OF PROGRAM LINES=========
def addTo(line,string):
	if line == "":
		line += ";"+string
	else:
		line += string
	return line

#=======RETRIEVE PROGRAM COMMANDS AS PER RULES========
def getLine(length):
	global order
	global anys
	global lasts
	line = ""
	if len(anys)>0:
		#no spaces for initializations
		if len(order)==0 or length < len(order[0]):	
			i = 0
			#fill with anys 
			while len(line)<=length and i<len(anys):
				if len(line)+len(anys[i])+1<=length:
					line = addTo(line,anys[i])
					anys.remove(anys[i])
				i+=1
		#just space for one initialization
		elif length == len(order[0]):
			line = addTo(line,order[0])
			order = order[1:]
		#space for initializations + anys
		else:
			#fill with as many inits as possible
			while len(line)<=length and len(order)>0:
				if len(line)+len(order[0])+1<=length: 
					line = addTo(line,order[0])
					order = order[1:]
				else:
					break
			#fill the rest with anys	
			i = 0
			while len(line)<=length and i<len(anys):
				if len(line)+len(anys[i])+1<=length:
					line = addTo(line,anys[i])
					anys.remove(anys[i])
				i+=1
	#no anys or inits left
	else:
		#no space for lasts
		if len(lasts)==0 or length < len(lasts[0]):
			pass
		else:
			#fill line with lasts 
			while len(line)<=length and len(lasts)>0:
				if len(line)+len(lasts[0])+1<=length:
					line = addTo(line,lasts[0])
					lasts = lasts[1:]
				else:
					break	

	#find out the leftover space
	toFill = length - len(line)
	if toFill > 0:
		#fill leftover space with valid,pythonic gibberish
		filler = "#"
		for iterator in range(0,toFill - 1):
			filler += "{}".format(rnd.randint(0,9))
	else:
		filler = ""
	return line + filler

#======GENERATE QUINE CIRCLE PROGRAM FROM ABOVE LINES====
def makeCircle(radius):
	f=open("quinePi.py","w")

	#iterate through circle
	for y_pos in range(-radius,radius+1):
		content,empties = 0,0
		for x_pos in range(-radius,radius+1):
			#if coordinate in circle, allocate line space
			if x_pos**2+y_pos**2 <= radius**2:
				content += 1
			else:
				empties += 1

		#get the Python contents of line
		program = getLine(content)

		#generate the beginning and ending separator strings
		numSeps = empties/2
		seps = "|"*numSeps
		seps = '"""'+seps+'"""'
		
		#format and write program line
		toWrite = "{}{}{}".format(seps,program,seps)
		print toWrite
		f.write(toWrite)
		if y_pos!=radius+1:
			f.write("\n")
	f.close()

#=======PROGRAM MAIN FUNCTION=============================
def estimate(radius):
	makeCircle(radius)
	import quinePi

#======INTERPRET COMMAND LINE ARGS========================
if __name__ == '__main__':
	desiredRad = int(sys.argv[1])
	if desiredRad < 14:
		print "Sorry! I haven't been able to make them that small yet!"
		sys.exit()
	estimate(desiredRad)