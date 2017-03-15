from resolution import resolution
from cairo_colors import toCairo
from cairo_line import lineTo
from name import name
from filename import *
from variables import *

def part1():
	with open(filename, 'a') as f:
		print >> f, "#include " + quote + "/usr/include/cairo/cairo.h" + quote

		print >> f, "int"
		print >> f, "main (int argc, char *argv[])"
		print >> f, "{"
		print >> f, space1 + "cairo_surface_t *surface = "
	f.close()
part1()

print new + space3 + heading * length1 
print widthHead
print space3 + heading * length1 

resolution()

def part2():
	with open(filename, 'a') as f:
		print >> f, space1 + "cairo_t *cr = "
		print >> f, space2 + "cairo_create (surface);" + new
	f.close()

part2()

print space3 + "Please enter the R, G, and B values for the outline of the image to be generated." + new
toCairo()

def part2_5():
	with open(filename, 'a') as f:
		print >> f, space1 + "cairo_scale (cr, 1.0, 1.0);"
	f.close()

part2_5()

print space3 + "Please enter the number of points to plot determined from static image using the GIMP or something similar" 
print space3 + "Please remember to close by making the last plot same as first." + new
lineTo()

def part3():
	with open(filename, 'a') as f:
		print >> f, space1 + "cairo_fill_preserve (cr);"
	f.close()

part3()

print space3 + "Please enter the R, G, and B values for the area of the image outline to be generated." + new
toCairo()

def part4():
	with open(filename, 'a') as f:
		print >> f, space1 + "cairo_stroke (cr);" + new
	f.close()

part4()

print space3 + "Please give the name of the image to be generated." + new
name()

def part5():
	with open(filename, 'a') as f:
		print >> f, space1 + "cairo_destroy (cr);"
		print >> f, space1 + "cairo_surface_destroy (surface);" 
		print >> f, space1 + "return 0;"
		print >> f, "}"
	f.close()
part5()





