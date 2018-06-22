#!/usr/bin/env python3

from PIL import Image, ImageDraw

STEPS = 64 * 6
HEIGHT = 256

SIN_TBL = [0, 1, 2, 5, 10, 15, 21, 29, 37, 47, 57, 67, 79, 90, 103, 115, 127, 140, 152, 165, 176, 188, 198, 208, 218, 226, 234, 240, 245, 250, 253, 254]
SIN_STEPS = 32

im = Image.new('RGB', (STEPS, HEIGHT))
draw = ImageDraw.Draw(im)

hueSector = 0
hue = 0
for x in range(0, STEPS):
	if hueSector == 0:
		r = 255
		g = SIN_TBL[hue]
		b = 0

	elif hueSector == 1:
		r = SIN_TBL[SIN_STEPS - hue - 1]
		g = 255
		b = 0

	elif hueSector == 2:
		r = 0
		g = 255
		b = SIN_TBL[hue]
	
	elif hueSector == 3:
		r = 0
		g = SIN_TBL[SIN_STEPS - hue - 1]
		b = 255

	elif hueSector == 4:
		r = SIN_TBL[hue]
		g = 0
		b = 255

	else:
		r = 255
		g = 0
		b = SIN_TBL[SIN_STEPS - hue - 1]

	print((r, g, b))
	hue += 1
	if hue >= SIN_STEPS:
		hue = 0
		hueSector += 1
		if hueSector == 6:
			hueSector = 0

	draw.line((x, 0, x, HEIGHT), fill=(r, g, b))

del draw
im.save('hsvsin_disc.png')
