from variables import *

print new + space4 + heading * length16
print starter1 
print space4 + subHeading * length16
print starter2 
print space4 + heading * length16

print new + space3 + heading * length2
print fnameHead
print space3 + heading * length2

inpt = raw_input(space3 + bell)
filename = inpt + ".c"
first = gcc + inpt + gcc1
length18 = len(first) - 12

def elfin():
	print new + space4 + heading * length18
	print first
	print space4 + subHeading * length18
	print gcc2 
	print space4 + subHeading * length18
	print gcc3 + inpt + gcc4 + inpt + ".c" + gcc5
	print space4 + heading * length18 + new


