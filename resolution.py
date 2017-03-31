from filename import *
from variables import *
spaces = Spaces()

def resolution():
	print new + spaces.space3 + subHeading * length3
	print spaces.space3 + wText 
	print spaces.space3 + subHeading * length3
	width = int(raw_input(spaces.space3 + bell))

	print new + spaces.space3 + subHeading * length4
	print spaces.space3 + hText 
	print spaces.space3 + subHeading * length3
	height = int(raw_input(spaces.space3 + bell))

	stringW = str(width)
	stringH = str(height)
	
	with open(filename, 'a') as f:
		print >> f, spaces.space1 + resolutionStart + stringW + end + stringH + resolutionEnd
	f.close()

