from filename import *
from variables import * 
from resolution import resolution

def part1():
	with open(filename, 'a') as f:
		print >> f, "#include " + quote + "/usr/include/cairo/cairo.h" + quote

		print >> f, "int"
		print >> f, "main (int argc, char *argv[])"
		print >> f, "{"
		print >> f, space1 + "cairo_surface_t *surface = "
	f.close()

def part2():
	with open(filename, 'a') as f:
		print >> f, space1 + "cairo_t *cr = "
		print >> f, space2 + "cairo_create (surface);" + new
	f.close()

def joinImages1():
	part1()
	resolution()
	part2()

	print new + space3 + subHeading * length11
	print overlaid
	print space3 + subHeading * length11
	number_of_times = int(raw_input(space3 + bell))
	pointer_dec = 0

	while (pointer_dec < number_of_times):
		print new + space3 + subHeading * length12
		print "Enter image nickname"
		print space3 + subHeading * length12
		imgNames = raw_input(space3 + bell)

		name = imgNames
	
		with open(filename, 'a') as f:
			print >> f, space1 + "cairo_surface_t *" + str(name) + ";\n"
		f.close()
		pointer_dec += 1

		if (pointer_dec == number_of_times):
			break

	print "Enter values the same you entered them above"
	number_of_times2 = int(raw_input(space3 + bell))
	pointer_dec2 = 0

	while (pointer_dec2 < number_of_times2):
		print new + space3 + subHeading * length12
		print "Enter image nickname"
		print space3 + subHeading * length12
		imgNames2 = raw_input(space3 + bell)

		print new + space3 + subHeading * length12
		print "Enter name of image png file"
		print space3 + subHeading * length12
		pngTitle = raw_input(space3 + bell)

		name2 = imgNames2
		title = pngTitle
		with open(filename, 'a') as f:
			print >> f, space1 + "\ncairo_push_group (cr);"
			print >> f, space1 + str(name2) + " " + heading + " " + "cairo_image_surface_create_from_png (" + quote + str(title) + quote + ");"
			print >> f, space1 + "cairo_pop_group_to_source (cr);"
		f.close()
		pointer_dec2 += 1

	print "More nicknames, same order"
	number_of_times3 = int(raw_input(space3 + bell))
	pointer_dec3 = 0

	while (pointer_dec3 < number_of_times3):
		pngTitle3 = raw_input(space3 + bell);
		title3 = pngTitle3
		with open(filename, 'a') as f:
			print >> f, "cairo_set_source_surface (cr, " + str(title) + ", 0, 0);"
			print >> f, "cairo_paint (cr); "
		f.close()
		pointer_dec3 += 1

		if (pointer_dec3 == number_of_times3):
			with open('filename', 'a') as f:
				print >> f, space1 + "cairo_close_path (cr);"
				print >> f, space1 + "cairo_close_path(cr);" + new
			f.close()

joinImages1()



















	



