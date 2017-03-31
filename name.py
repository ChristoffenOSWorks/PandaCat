from filename import *
from variables import *
spaces = Spaces()

def name():
	name = raw_input(spaces.space3 + bell)
	
	pngFun = spaces.space3 + "cairo_surface_write_to_png (surface," + quote + name + quote + ");"
	length15 = len(pngFun) - 4

	print new + spaces.space3 + subHeading * length15
	print pngFun
	print spaces.space3 + subHeading * length15

	with open(filename, 'a') as f:
		print >> f, "        cairo_surface_write_to_png (surface," + quote + name + quote + ");"
	f.close()



