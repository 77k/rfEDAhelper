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

	filename = sys.argv[5]
	depth = int(sys.argv[4])
	stroke = float(sys.argv[3])
	h = float(sys.argv[2])
	lamb = float(sys.argv[1])
	r = 0.75 * lamb/PI
	ccw = numpy.array([[cos(PI/2), -sin(PI/2)], [sin(PI/2), cos(PI/2)]])
	cw = numpy.array([[cos(-PI/2), -sin(-PI/2)], [sin(-PI/2), cos(-PI/2)]])
	axiom = 'LFL+F+LFL+F'
	production = { 'L' : '-RF+LFL+FR-',
		       'R' : '+LF-RFR-FL+'}
	print axiom
	for x in range(0, depth) :
		tmp = ''
		for s in axiom:
			if s in production.keys():
				tmp += production[s]
			else:
				tmp += s
		axiom = tmp
	print axiom		
	n = depth
	h = lamb * (PI/4.0) /(4 ** ((n + 0) * .5))
	d = Svg(height = str(h) + 'mm', width = str(h) + 'mm')
	a = lamb * 1.5 / (4.0 ** (depth + 1))
		
	sb = pysvg.builders.ShapeBuilder()
	v = numpy.array([0, a])
	p0 = numpy.array([h/2 - a/2, 1 * a])
	seg_num = 0
	def F():
			t = numpy.add(p0, v)
			t2 = numpy.add(p0, v * (1.0 + 0.5 * stroke/numpy.linalg.norm(v)))
			scolor = 'black'
			d.addElement(sb.createLine(str(p0[0]) + 'mm', str(p0[1]) + 'mm', str(t2[0]) + 'mm', str(t2[1]) + 'mm', strokewidth = str(stroke) + 'mm', stroke = scolor))
			return (t, v, seg_num + 1)
	def CCW():
			return (p0, v.dot(ccw), seg_num)
	def CW():
			return (p0, v.dot(cw), seg_num)


	evaluation = { 'F' : F, '+' : CCW, '-' : CW} 
	for c in axiom:
		if c in evaluation.keys():
			(p0, v, seg_num) = evaluation[c]()
			if seg_num == int(round((4 ** (n + 1)) * 1.0/4.0) - 1):
				port1 = (p0, v, seg_num)
			if seg_num == int(round((4 ** (n + 1)) * (1.0/4.0 - 1.0/6.0)) - 1):
				port2 = (p0, v, seg_num)
			if seg_num == int(round((4 ** (n + 1)) * (3.0/4.0 + 1.0/6.0)) - 1):
				port3 = (p0, v, seg_num)
			if seg_num == int(round((4 ** (n + 1)) * 3.0/4.0) - 1):
				port4 = (p0, v, seg_num)
	q = port1[0] + port1[1] * 0.5
	r = numpy.add(q, numpy.array([-h/2, 0.0]));
        d.addElement(sb.createLine(str(q[0]) + 'mm', str(q[1]) + 'mm', str(r[0]) + 'mm', str(r[1]) + 'mm', strokewidth = str(stroke) + 'mm', stroke = 'black'))
	corr = (((4 ** (n + 1)) * 1.0/4.0 - 1.0/6.0) * a)/(lamb * 1.5) - (float(port2[2])/( 4 ** ( n + 1))) 
	q = port2[0] + port2[1] * corr
	r = numpy.add(q, numpy.array([0.0, -h/2]));
        d.addElement(sb.createLine(str(q[0]) + 'mm', str(q[1]) + 'mm', str(r[0]) + 'mm', str(r[1]) + 'mm', strokewidth = str(stroke) + 'mm', stroke = 'black'))
	corr = (((4 ** (n + 1)) * 3.0/4.0 + 1.0/6.0) * a)/(lamb * 1.5) - (float(port2[2])/( 4 ** ( n + 1))) 
	q = port3[0] + port3[1] * corr
	r = numpy.add(q, numpy.array([0.0, -h/2]));
        d.addElement(sb.createLine(str(q[0]) + 'mm', str(q[1]) + 'mm', str(r[0]) + 'mm', str(r[1]) + 'mm', strokewidth = str(stroke) + 'mm', stroke = 'black'))
	q = port4[0] + port4[1] * 0.5
	r = numpy.add(q, numpy.array([h/2, 0.0]));
        d.addElement(sb.createLine(str(q[0]) + 'mm', str(q[1]) + 'mm', str(r[0]) + 'mm', str(r[1]) + 'mm', strokewidth = str(stroke) + 'mm', stroke = 'black'))
	d.save(filename)

if __name__ == "__main__":
    main()

