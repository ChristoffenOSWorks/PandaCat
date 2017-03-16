from filename import *
from variables import *

def toCairo():
	print new + space3 + subHeading * length6
	print convertR 
	print space3 + subHeading * length6
	r_one = float(raw_input(space3 + bell));

	print new + space3 + subHeading * length7
	print convertG
	print space3 + subHeading * length7
	g_one = float(raw_input(space3 + bell));

	print new + space3 + subHeading * length8
	print convertB 
	print space3 + subHeading * length8
	b_one = float(raw_input(space3 + bell));

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

	strOutputRGB = space3 + setSourceRGBAStart + stringR + end + stringG + end + stringB + toCairoEnd
	length9 = len(strOutputRGB) - 4
	print new + space3 + subHeading * length9
	print strOutputRGB
	print space3 + subHeading * length9

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
