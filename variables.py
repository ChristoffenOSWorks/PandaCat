class Spaces():
	def __init__(init):
		init.space1 = "        "
		init.space2 = "            "
		init.space3 = "    "
		init.space4 = init.space3 * 4

spaces = Spaces()

new = "\n"
setSourceRGBAStart = "cairo_set_source_rgba(cr, "
before = "Before Cairo, the original RGB values are: " 
bell = ">> "
end = ", "
cmd = "Command not recognized"
toCairoEnd = ", 0.8);"
quote = "\""
wText = "Enter image height: "
hText = "Enter image length: "
rgb = spaces.space3 + "Please enter the R, G, and B values for the outline of the image to be generated." 
convertR = spaces.space3 + "Enter the R value to be converted."
convertG = spaces.space3 + "Enter the G value to be converted."
convertB = spaces.space3 + "Enter the B value to be converted."
resolutionStart = "cairo_image_surface_create (CAIRO_FORMAT_ARGB32, "
resolutionEnd = ");"
lineToEnd = ");"
lineToStart = "cairo_line_to(cr, "
widthHead = spaces.space3 + "Please enter the width and height of the image to be generated." 
fnameHead = spaces.space3 + "Please enter the name of the file to be generated."
points1 = spaces.space3 + "Please enter the number of points to plot determined from static image using the GIMP or something similar" 
points2 = spaces.space3 + "Please remember to close by making the last plot same as first." 
line1 = spaces.space3 + "Please enter the number of pairs you want drawn."
overlaid = spaces.space3 + "Please enter the number of images to be drawn over top of each other."
xvalue1 = spaces.space3 + "Please enter the X value of the current pair."
yvalue1 = spaces.space3 + "Please enter the Y value of the current pair."
nameGen = spaces.space3 + "Please give the name of the image to be generated."
starter1 = spaces.space4 + "(c) 2017 Christoffen OSWorks, LLC. Some rights reserved. Code handwritten by M. Gage Morgan."
starter2 = spaces.space4 + "This is the PandaCat vector graphics code generator tool, which plugs into the Cairo API for testing purposes."
gcc = spaces.space4 + "The generator has finished. You can find the outputted file, "
gcc1 = ".c, in the directory you ran this script from."
gcc2 = spaces.space4 + "Compile the generated file with: " 
gcc3 = spaces.space4 + "gcc -o " 
gcc4 = " `pkg-config --cflags cairo` "
gcc5 = " `pkg-config --libs cairo`" 
crtOne = spaces.space4 + "(c) 2017 M. Gage Morgan. All Rights Reserved. Project start date: 2/24/2017"
crtTwo = spaces.space4 + "Script to convert between sane-people RGB and near retard-level Cairo API."
crtThree = spaces.space3 + "Type 'cairo' to convert to the Cairo-formatted RGB, or 'rgb' for the standard form."
heading = "="
subHeading = "-"
class Length():
	
	def __init__(variables):
		return None
	def __len__(variables): 
		return len(variables.vals) - 4
	

length1 = len(widthHead) - 4
length2 = len(fnameHead) - 4
length3 = len(wText) 
length4 = len(hText)
length5 = len(rgb) - 4
length6 = len(convertR) - 4
length7 = len(convertG) - 4
length8 = len(convertB) - 4
length10 = len(points1) - 4
length11 = len(line1) - 4
length12 = len(xvalue1) - 4
length13 = len(yvalue1) - 4
length14 = len(nameGen) - 4
length16 = len(starter2) - 12 
length19 = len(crtThree) - 4
