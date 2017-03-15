from resolution import resolution
from cairo_colors import toCairo
from cairo_line import lineTo

def part1():
	with open('out.txt', 'a') as f:
		print >> f, "#include ""/usr/include/cairo/cairo.h\""

		print >> f, "int"
		print >> f, "main (int argc, char *argv[])"
		print >> f, "{"
		print >> f, "        cairo_surface_t *surface = "
	f.close()
part1()
resolution()

def part2():
	with open('out.txt', 'a') as f:
		print >> f, "        cairo_t *cr = "
		print >> f, "            cairo_create (surface);"
	f.close()

part2()
toCairo()
lineTo()

def part3():
	with open('out.txt', 'a') as f:
		print >> f, "		cairo_fill_preserve (cr);"
	f.close()

part3()
toCairo()

def part4():
	with open('out.txt', 'a') as f:
		print >> f, "		cairo_stroke (cr);"

		print >> f, "        cairo_destroy (cr);"
		print >> f, "        cairo_surface_destroy (surface);" 
		print >> f, "        return 0;"
		print >> f, "}"
	f.close()
part4()





