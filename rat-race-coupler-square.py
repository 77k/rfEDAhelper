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
import numpy

def main():

	filename = sys.argv[4]
	depth = int(sys.argv[3])
	h = float(sys.argv[2])
	lamb = float(sys.argv[1])
	r = 0.75 * lamb/PI
	ccw = numpy.matrix([[cos(PI/2), sin(PI/2)], [-sin(PI/2), cos(PI/2)]])
	cw = numpy.matrix([[cos(-PI/2), sin(-PI/2)], [-sin(-PI/2), cos(-PI/2)]])
	axiom = 'LFL+F+LFL+F'
	production = { 'L' : '-RF+LFL+FR-',
		       'R' : '+LF-RFR-FL+'}	
	if r >= h/2 :
		print "does not fit" 
	d = Svg(height = str(h) + 'mm', width = str(h) + 'mm')

	a = lamb * 1.5 / (4.0 ** (depth + 1))
		
	sb = pysvg.builders.ShapeBuilder()
	
	d.addElement(sb.createLine('0mm', str(h/2) + 'mm', str(h/2 - r) + 'mm', str(h/2) + 'mm', strokewidth = '3mm', stroke = 'black'))
	d.save(filename)

if __name__ == "__main__":
    main()

