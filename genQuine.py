import random as rnd
import sys

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

def nl(f):
	f.write("\n")

def writeProgram():
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
	f.write("print(do1+do2)")
	nl(f)

def addTo(line,string):
	if line == "":
		line += ";"+string
	else:
		line += string
	return line

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
		#just space for initialization
		elif length == len(order[0]):
			while len(line)<=length and len(order)>0:
				if len(line)+len(order[0])+1<=length: 
					line = addTo(line,order[0])
					order = order[1:]
				else:
					break
		#space for initialization + anys
		else:
			while len(line)<=length and len(order)>0:
				if len(line)+len(order[0])+1<=length: 
					line = addTo(line,order[0])
					order = order[1:]
				else:
					break	
			i = 0
			while len(line)<=length and i<len(anys):
				if len(line)+len(anys[i])+1<=length:
					line = addTo(line,anys[i])
					anys.remove(anys[i])
				i+=1
	#no anys or inits left
	else:
		if len(lasts)==0 or length < len(lasts[0]):
			pass
		else: 
			while len(line)<=length and len(lasts)>0:
				if len(line)+len(lasts[0])+1<=length:
					line = addTo(line,lasts[0])
					lasts = lasts[1:]
				else:
					break	

	toFill = length - len(line)
	if toFill > 0:
		filler = "#"
		for iterator in range(0,toFill - 1):
			filler += "{}".format(rnd.randint(0,9))
	else:
		filler = ""
	return line + filler

def makeCircle(radius):
	f=open("generatedQuine.py","w")
	array=[]
	ohs = 0
	spaces = 0
	for y_pos in range(-radius,radius+1):
		content = 0
		empties = 0
		for x_pos in range(-radius,radius+1):
			if x_pos**2+y_pos**2 <= radius**2:
				content += 1
			else:
				empties += 1

		program = getLine(content)
		numSeps = empties/2
		seps = "|"*numSeps
		seps = '"""'+seps+'"""'
		toWrite = "{}{}{}".format(seps,program,seps)
		print toWrite
		f.write(toWrite)
		if y_pos!=radius+1:
			f.write("\n")
	f.close()

def estimate(radius):
	makeCircle(radius)
	import generatedQuine

if __name__ == '__main__':
	desiredRad = int(sys.argv[1])
	estimate(desiredRad)