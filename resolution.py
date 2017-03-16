from filename import *
from variables import *

def resolution():
	print new + space3 + subHeading * length3
	print space3 + wText 
	print space3 + subHeading * length3
	width = int(raw_input(space3 + bell))

	print new + space3 + subHeading * length4
	print space3 + hText 
	print space3 + subHeading * length3
	height = int(raw_input(space3 + bell))

	stringW = str(width)
	stringH = str(height)
	
	with open(filename, 'a') as f:
		print >> f, space1 + resolutionStart + stringW + end + stringH + resolutionEnd
	f.close()

