#!/usr/bin/python
import sys
import pysvg
from pysvg.filter import *
from pysvg.gradient import *
from pysvg.linking import *
from pysvg.script import *
from pysvg.shape import *
from pysvg.structure import *
from pysvg.style import *
from pysvg.text import *
from pysvg.builders import *
from pysvg.builders import *
from math import pi as PI
from math import sin, cos, sqrt

def main():

	filename = sys.argv[3]
	h = float(sys.argv[2])
	lamb = float(sys.argv[1])
	r = 0.75 * lamb/PI
	if r >= h/2 :
		print "does not fit" 
	d = Svg(height = str(h) + 'mm', width = str(h) + 'mm')
	
	sb = pysvg.builders.ShapeBuilder()
	d.addElement(sb.createCircle(str(h/2) + 'mm', str(h/2) + 'mm' , str(r) + 'mm', strokewidth = '3mm', stroke = 'black', fill = 'none'))
	
	d.addElement(sb.createLine('0mm', str(h/2) + 'mm', str(h/2 - r) + 'mm', str(h/2) + 'mm', strokewidth = '3mm', stroke = 'black'))
	d.addElement(sb.createLine(str(h/2 + r) + 'mm' , str(h/2) + 'mm', str(h) + 'mm',
					str(h/2) + 'mm', strokewidth = '3mm', stroke = 'black'))
	d.addElement(sb.createLine(str(h/2 - r * cos(PI/3)) + 'mm' , str(h/2 - r * sin(PI/3)) + 'mm'
					, str(h/2 - 2 * h * cos(PI/3)) + 'mm',
					str(h/2 - 2 * h * sin(PI/3)) + 'mm', strokewidth = '3mm', stroke = 'black'))
	d.addElement(sb.createLine(str(h/2 - r * cos(2 * PI/3)) + 'mm' , str(h/2 -  r * sin(2 * PI/3)) + 'mm'
					, str(h/2 - 2 * h * cos(2 * PI/3)) + 'mm',
					str(h/2 - 2 * h * sin(2 * PI/3)) + 'mm', strokewidth = '3mm', stroke = 'black'))
	d.save(filename)

if __name__ == "__main__":
    main()

