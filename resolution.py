from filename import *

wText = "Enter image height: "
hText = "Enter image length: "
bell = "    >> "
new = "\n"
resolutionStart = "cairo_image_surface_create (CAIRO_FORMAT_ARGB32, "
resolutionEnd = ");"
end = ", "
space1 = "            "

def resolution():
	print wText + new
	width = int(raw_input(bell))

	print hText + new
	height = int(raw_input(bell))

	stringW = str(width)
	stringH = str(height)
	
	with open(filename, 'a') as f:
		print >> f, space1 + resolutionStart + stringW + end + stringH + resolutionEnd
	f.close()

