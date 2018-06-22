#!/usr/bin/env python3

from PIL import Image, ImageDraw
from math import *

STEPS = 64 * 6
HEIGHT = 256

im = Image.new('RGB', (STEPS, HEIGHT))
draw = ImageDraw.Draw(im)

COLORS = [
	(0xFF, 0x00, 0x00),
	(0xFF, 0x66, 0x00),
	(0xFF, 0xEE, 0x00),
	(0x00, 0xFF, 0x00),
	(0x00, 0x99, 0xFF),
	(0x44, 0x00, 0xFF),
	(0x99, 0x00, 0xFF)
]

COLOR_STEPS = 25
def sin_soften(x):
	return 0.5 - cos(x * pi) / 2

colorIdx = 0
colorStep = 0
for x in range(0, STEPS+1):
	c1 = COLORS[colorIdx]
	c2 = COLORS[(colorIdx + 1) % len(COLORS)]

	ratio = sin_soften(colorStep / (COLOR_STEPS - 1))
	color = (
		int((c1[0] * (1 - ratio) + c2[0] * ratio)),
		int((c1[1] * (1 - ratio) + c2[1] * ratio)),
		int((c1[2] * (1 - ratio) + c2[2] * ratio))
	)
	print("%d %03d %s" % (colorIdx, colorStep, color))

	colorStep += 1
	if colorStep == COLOR_STEPS:
		colorStep = 0
		colorIdx += 1
		if colorIdx == len(COLORS):
			colorIdx = 0

	draw.line((x, 0, x, HEIGHT), fill=color)

del draw
im.save('sinbow.png')
