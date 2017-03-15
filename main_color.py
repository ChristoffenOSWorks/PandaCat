from resolution import resolution
from cairo_colors import toCairo
from cairo_line import lineTo
from name import name
from filename import *

space1 = "        "
space2 = "            "
end = "\n"
quote = "\""

def part1():
	with open(filename, 'a') as f:
		print >> f, "#include " + quote + "/usr/include/cairo/cairo.h" + quote

		print >> f, "int"
		print >> f, "main (int argc, char *argv[])"
		print >> f, "{"
		print >> f, space1 + "cairo_surface_t *surface = "
	f.close()
part1()

print "Please enter the width and height of the image to be generated."
resolution()

def part2():
	with open(filename, 'a') as f:
		print >> f, space1 + "cairo_t *cr = "
		print >> f, space2 + "cairo_create (surface);" + end
	f.close()

part2()

print "Please enter the R, G, and B values for the outline of the image to be generated."
toCairo()

def part2_5():
	with open(filename, 'a') as f:
		print >> f, space1 + "cairo_scale (cr, 1.0, 1.0);"
	f.close()

part2_5()

print "Please enter the number of points to plot determined from static image using the GIMP or something similar"
print "Please remember to close by making the last plot same as first."
lineTo()

def part3():
	with open(filename, 'a') as f:
		print >> f, space1 + "cairo_fill_preserve (cr);"
	f.close()

part3()

print "Please enter the R, G, and B values for the area of the image outline to be generated."
toCairo()

def part4():
	with open(filename, 'a') as f:
		print >> f, space1 + "cairo_stroke (cr);" + end
	f.close()

part4()

print "Please give the name of the image to be generated."
name()

def part5():
	with open(filename, 'a') as f:
		print >> f, space1 + "cairo_destroy (cr);"
		print >> f, space1 + "cairo_surface_destroy (surface);" 
		print >> f, space1 + "return 0;"
		print >> f, "}"
	f.close()
part5()





