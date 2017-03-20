from cairo_colors import *
from variables import *

def textColor():
	print new + space4 + heading * length16
	print crtOne
	print space4 + subHeading * length16
	print crtTwo 
	print space4 + heading * length16

	print new + space3 + subHeading * length19
	print crtThree 
	print space3 + subHeading * length19

textColor()

mode = raw_input(space3 + bell);
if (mode == "cairo"):
	while mode == "cairo":
		try:
			toCairo()
			break
		except NameError:
			print cmd
			
elif (mode == "rgb"):
	while True:
		try:
			toRGBA();
			break
		except NameError:
			print cmd
else:
	print "Else reached"


