def toCairo():
	print "    Enter the R value to be converted.\n";
	r_one = float(raw_input("    >> "));
	print "\n"

	print "    Enter the G value to be converted.\n";
	g_one = float(raw_input("    >> "));
	print "\n"

	print "    Enter the B value to be converted.\n";
	b_one = float(raw_input("    >> "));
	print "\n"

	r_two = r_one / 255;
	g_two = g_one / 255;
	b_two = b_one / 255;

	r_three = round(r_two, 2);
	g_three = round(g_two, 2);
	b_three = round(b_two, 2);

	with open('out.txt', 'a') as f:
		print >> f, "cairo_set_source_rgba(" + str(r_three) + ", " + str(g_three) + ", " + str(b_three) + ", 0.8);";
	f.close()

def toRGBA():
	print "\n    Enter the R value to be converted.\n";
	r_one = float(raw_input("    >> "));
	print "\n"

	print "    Enter the G value to be converted.\n";
	g_one = float(raw_input("    >> "));
	print "\n"

	print "    Enter the B value to be converted.\n";
	b_one = float(raw_input("    >> "));
	print "\n"

	r_two = r_one * 255;
	g_two = g_one * 255;
	b_two = b_one * 255;

	print "Before Cairo, the original RGB values are: " + str(int(r_two)) + ", " + str(int(g_two)) + ", " + str(int(b_two)) + ".\n\n";

print "(c) 2017 M. Gage Morgan. All Rights Reserved. Project start date: 2/24/2017\n";
print "Script to convert between sane-people RGB and near retard-level Cairo API.\n"
print "Type 'cairo' to convert to the Cairo-formatted RGB, or 'rgb' for the standard form.\n\n";

mode = raw_input("    >> ");

if (mode == 'cairo'):
    toCairo();
elif (mode == 'rgb'):
	toRGBA();
else:
	print "Command unrecognized";


