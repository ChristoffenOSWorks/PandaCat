# PandaCat
Python tools to help Designers draw their own Pandas without knowing anything about Cairo. 

## Introduction
This is a tool created by @mgagemorgan, co-founder, for the design staff. Due to other projects, it would be a waste of time to let designers have an actual programmer programming their experiments.

Instead of automatically implementing everything in the Assets API, Christoffen is building a testing tool that crunches info into Cairo function calls and spits them out into a file or into the CLI for quick debugging. 

## The Story
@mgagemorgan realized this when doing gradients with @dackean. @dackean wanted to use them a certain way, and then subsequently decided he didn't like it. @mgagemorgan didn't have time to work on Cairo scripting. 

Then comes coloring the logo. Again, @dackean made boneheaded mistakes that caused lost time. That was it, the final straw. 

## Implementation
Here are the files in this repo:

### cairo_colors.py
This is the response to the logo coloring failure. @dackean can use this tool to go to and from RGB colors without @mgagemorgan's intervention. 

### cairo_coordinates.py
Allows designers to use PIXLR or GIMP to draw lines. 
