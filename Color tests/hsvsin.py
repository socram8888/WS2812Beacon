#!/usr/bin/env python3

from PIL import Image, ImageDraw
from math import *

def sin_soften(x):
	return 0.5 - cos(x * pi) / 2

STEPS = 64 * 6
HEIGHT = 256

im = Image.new('RGB', (STEPS, HEIGHT))
draw = ImageDraw.Draw(im)

hueSector = 0
hue = 0
for x in range(0, STEPS):
	if hueSector == 0:
		r = 255
		g = int(255 * sin_soften(hue / 255))
		b = 0

	elif hueSector == 1:
		r = int(255 * sin_soften(1 - hue / 255))
		g = 255
		b = 0

	elif hueSector == 2:
		r = 0
		g = 255
		b = int(255 * sin_soften(hue / 255))
	
	elif hueSector == 3:
		r = 0
		g = int(255 * sin_soften(1 - hue / 255))
		b = 255

	elif hueSector == 4:
		r = int(255 * sin_soften(hue / 255))
		g = 0
		b = 255

	else:
		r = 255
		g = 0
		b = int(255 * sin_soften(1 - hue / 255))

	print((r, g, b))
	hue += 8
	if hue >= 256:
		hue = 0
		hueSector += 1
		if hueSector == 6:
			hueSector = 0

	draw.line((x, 0, x, HEIGHT), fill=(r, g, b))

del draw
im.save('hsvsin.png')
