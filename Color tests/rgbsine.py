#!/usr/bin/env python3

from PIL import Image, ImageDraw

STEPS = 64 * 6
HEIGHT = 256

im = Image.new('RGB', (STEPS, HEIGHT))
draw = ImageDraw.Draw(im)

SIN_TBL = [0, 0, 1, 1, 3, 4, 6, 8, 10, 13, 16, 19, 22, 26, 30, 34, 38, 43, 48, 53, 58, 64, 69, 75, 81, 87, 93, 99, 105, 112, 118, 124, 131, 137, 143, 150, 156, 162, 168, 174, 180, 186, 191, 197, 202, 207, 212, 217, 221, 225, 229, 233, 236, 239, 242, 245, 247, 249, 251, 252, 254, 254, 255, 255]
SIN_STEPS = len(SIN_TBL)

hueSector = 0
hue = 0
for x in range(0, STEPS):
	if hueSector == 0:
		r = SIN_TBL[SIN_STEPS - hue - 1]
		g = SIN_TBL[hue]
		b = 0

	elif hueSector == 1:
		r = 0
		g = SIN_TBL[SIN_STEPS - hue - 1]
		b = SIN_TBL[hue]

	else:
		r = SIN_TBL[hue]
		g = 0;
		b = SIN_TBL[SIN_STEPS - hue - 1]

	print((r, g, b))
	hue += 1
	if hue == SIN_STEPS:
		hue = 0
		hueSector += 1
		if hueSector == 3:
			hueSector = 0

	draw.line((x, 0, x, HEIGHT), fill=(r, g, b))

del draw
im.save('rgbsine.png')
