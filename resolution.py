wText = "Enter image height: "
hText = "Enter image length: "
bell = "    >> "
new = "\n"
resolutionStart = "cairo_image_surface_create (CAIRO_FORMAT_ARGB32, "
resolutionEnd = ");"
end = ", "
cairoRes = "Your resolution in cairo is: "

def resolution():
	print wText + new
	width = int(raw_input(bell))

	print hText + new
	height = int(raw_input(bell))

	stringW = str(width)
	stringH = str(height)

	print cairoRes + new
	
	with open('out.txt', 'a') as f:
		print >> f, resolutionStart + stringW + end + stringH + resolutionEnd
	f.close()

