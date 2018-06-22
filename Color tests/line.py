#!/usr/bin/env python3

from PIL import Image, ImageDraw

STEPS = 64 * 6
HEIGHT = 256

im = Image.new('RGB', (STEPS, HEIGHT))
draw = ImageDraw.Draw(im)

hueSector = 0
hue = 0
for x in range(0, STEPS):
	if hueSector == 0:
		r = 255
		g = hue
		b = 0

	elif hueSector == 1:
		r = 255 - hue
		g = 255
		b = 0

	elif hueSector == 2:
		r = 0
		g = 255
		b = hue
	
	elif hueSector == 3:
		r = 0
		g = 255 - hue
		b = 255

	elif hueSector == 4:
		r = hue
		g = 0
		b = 255

	else:
		r = 255
		g = 0
		b = 255 - hue

	print((r, g, b))
	hue += 8
	if hue >= 256:
		hue = 0
		hueSector += 1
		if hueSector == 6:
			hueSector = 0

	draw.line((x, 0, x, HEIGHT), fill=(r, g, b))

del draw
im.save('out_lin.png')
