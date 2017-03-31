from filename import *
from variables import * 
spaces = Spaces()

def lineTo():
	print new + spaces.space3 + subHeading * length11
	print line1
	print spaces.space3 + subHeading * length11
	number_of_times = int(raw_input(spaces.space3 + bell))
	time_current = 0

	while (time_current < number_of_times):
		print new + spaces.space3 + subHeading * length12
		print xvalue1
		print spaces.space3 + subHeading * length12
		point_x1 = float(raw_input(spaces.space3 + bell))

		print new + spaces.space3 + subHeading * length13
		print yvalue1
		print spaces.space3 + subHeading * length13
		point_y1 = float(raw_input(spaces.space3 + bell))

		x1 = str(point_x1)
		y1 = str(point_y1)
	
		with open(filename, 'a') as f:
			print >> f, spaces.space1 + lineToStart + x1 + end + y1 + lineToEnd
		f.close()
		time_current += 1

	if (time_current == number_of_times):
		with open('out.txt', 'a') as f:
			print >> f, spaces.space1 + "cairo_close_path (cr);"
			print >> f, spaces.space1 + "cairo_close_path(cr);" + new
		f.close()



















	



