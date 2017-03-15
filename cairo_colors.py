from filename import *

new = "\n"
setSourceRGBAStart = "cairo_set_source_rgba(cr, "
before = "Before Cairo, the original RGB values are: " 
convertR = "    Enter the R value to be converted."
convertG = "    Enter the G value to be converted."
convertB = "    Enter the B value to be converted."
bell = "//    >> "
end = ", "
crtOne = "(c) 2017 M. Gage Morgan. All Rights Reserved. Project start date: 2/24/2017"
crtTwo = "Script to convert between sane-people RGB and near retard-level Cairo API."
crtThree = "Type 'cairo' to convert to the Cairo-formatted RGB, or 'rgb' for the standard form."
cmd = "Command not recognized"
toCairoEnd = ", 0.8);"
space1 = "        "

def toCairo():
	print convertR + new
	r_one = float(raw_input(bell));
	print new

	print convertG + new
	g_one = float(raw_input(bell));
	print new

	print convertB + new
	b_one = float(raw_input(bell));
	print new

	r_two = r_one / 255;
	g_two = g_one / 255;
	b_two = b_one / 255;

	r_three = round(r_two, 2);
	g_three = round(g_two, 2);
	b_three = round(b_two, 2);

	stringR = str(r_three)
	stringG = str(g_three)
	stringB = str(b_three)

	with open(filename, 'a') as f:
		print >> f, space1 + setSourceRGBAStart + stringR + end + stringG + end + stringB + toCairoEnd
	f.close()

	print space1 + setSourceRGBAStart + stringR + end + stringG + end + stringB + toCairoEnd

def toRGBA():
	print convertR + new
	r_one = float(raw_input(bell));
	print new

	print convertG + new
	g_one = float(raw_input(bell));
	print new

	print convertB + new
	b_one = float(raw_input(bell));
	print new

	r_two = r_one * 255;
	g_two = g_one * 255;
	b_two = b_one * 255;

	stringR = str(int(r_two))
	stringG = str(int(g_two))
	stringB = str(int(b_two))

	print before + stringR + end + stringG + end + stringB + new + new

"""
print crtOne + new
print crtTwo + new
print crtThree + new + new

mode = raw_input(bell);

if (mode == 'cairo'):
	toCairo();
elif (mode == 'rgb'):
	toRGBA();
else:
	print cmd

if (mode == 'cairo'):
	toCairo();
elif (mode == 'rgb'):
	toRGBA();
else:
	print cmd 
"""
