from pydub import AudioSegment
from matplotlib import pyplot as plot
from PIL import Image, ImageDraw
import numpy as np
import os
import math

src = "song.flac"

audio = AudioSegment.from_file(src)
data = np.fromstring(audio[:30000]._data, np.int16)
fs = audio.frame_rate

BARS = 1000
BAR_HEIGHT = 60
BAR_WIDTH = 2
BARS_PER_LINE = 100
LINES = int(math.ceil(float(BARS) / float(BARS_PER_LINE)))
VERTICAL_SPACING = 5
HORIZONTAL_SPACING = 5

IMAGE_WIDTH = HORIZONTAL_SPACING * BAR_WIDTH * BARS_PER_LINE
IMAGE_HEIGHT = VERTICAL_SPACING * BAR_HEIGHT * LINES

highest_line = 0
for d in data:
	if abs(d) > highest_line:
		highest_line = d

line_ratio = highest_line/BAR_HEIGHT

im = Image.new('RGBA', (IMAGE_WIDTH, IMAGE_HEIGHT), (255, 255, 255, 1))
draw = ImageDraw.Draw(im)

current_x = 0
line_count = 0
current_line = 1
for item in data:
	if line_count > BARS_PER_LINE:
		current_line += 1
		current_x = 0
		line_count = 0

	item_height = float(item)/float(line_ratio)

	current_y = ((BAR_HEIGHT - item_height)/2) + (current_line*(HORIZONTAL_SPACING + BAR_HEIGHT))
	draw.line((current_x, current_y, current_x, current_y + item_height), fill=(169, 171, 172), width=BAR_WIDTH)

	current_x = current_x + HORIZONTAL_SPACING
	line_count += 1

im.show()
