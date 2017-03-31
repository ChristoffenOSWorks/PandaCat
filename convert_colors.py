from cairo_colors import *
from variables import *
spaces = Spaces()

def textColor():
	print new + spaces.space4 + heading * length16
	print crtOne
	print spaces.space4 + subHeading * length16
	print crtTwo 
	print spaces.space4 + heading * length16

	print new + spaces.space3 + subHeading * length19
	print crtThree 
	print spaces.space3 + subHeading * length19

textColor()

mode = raw_input(spaces.space3 + bell);
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


