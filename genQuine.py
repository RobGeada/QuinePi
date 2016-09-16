import random as rnd
import sys,os

#===========DEFINE ALL THE NECCESARY COMMANDS============
#these must appear in this order
order = [
r"I='import';",
r"M='from math ';",
r"exec(I+' os');",
r"exec(M+I+' sqrt');",
r"x='M=os.path.realp';",
r"y='ath(__file__)';",
r"exec(x+y);",
r"f=open(M);",
r"s=f.read();"]

#these can be interspersed in 'order' in any order
anys = [\
r'S=-1.;',
r'F=2;',
r"o='%f';",
r"a='for i in s:\n ';",
r"N='\n';",
"b='if(i==\\'\"\\' ';",
r"c='or i==N):pass\n ';",
r"e='elif(i==\'|\'):';",
r"f='S+=1\n else:F+=1';"
]

#these must appear in this order, after everything above
lasts = [\
"m=a+b+c+e+f;",
"exec(m);",
"Q=S+F;",
"H=.5;",
"r=sqrt(Q/4)-H;",
"p=F/r**2;",
"r=o%p;",
"print r;"]

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
	#print order;print anys;print lasts
	line = ""
	if len(anys)>0:
		#no spaces for initializations
		if len(order)==0 or length < len(order[0]):
			i = 0
			#fill with anys 
			while len(line)<length and i<len(anys):
				if len(line)+len(anys[i])+1<=length:
					line = addTo(line,anys[i])
					anys.remove(anys[i])
					i=-1
				i+=1
		#just space for one initialization
		elif length-1 == len(order[0]):
			line = addTo(line,order[0])
			order = order[1:]
		#space for initializations + anys
		else:
			#fill with as many inits as possible
			while len(line)<length and len(order)>0:
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
	if len(order)==0 and len(anys)==0:
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
def makeCircle(radius,verbose):
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
		if verbose:
			print toWrite
		f.write(toWrite)
		if y_pos!=radius+1:
			f.write("\n")
	f.close()

#=======PROGRAM MAIN FUNCTION=============================
def estimate(radius,verbose):
	makeCircle(radius,verbose)
	os.system("python quinePi.py")

#======INTERPRET COMMAND LINE ARGS========================
if __name__ == '__main__':
	desiredRad = int(sys.argv[2])
	verbose = sys.argv[1]
	if verbose=="-v":
		verbose = True
	else:
		verbose = False
	if desiredRad < 12:
		print "Sorry! I haven't been able to make them that small yet!"
		sys.exit()
	estimate(desiredRad,verbose)

