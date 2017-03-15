from filename import *

def name():
	name = raw_input("    >> ")
	quote = "\""
	
	print "        cairo_surface_write_to_png (surface," + quote + name + quote + ");"
	with open(filename, 'a') as f:
		print >> f, "        cairo_surface_write_to_png (surface," + quote + name + quote + ");"
	f.close()



