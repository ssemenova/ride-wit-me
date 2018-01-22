from pydub import AudioSegment
from matplotlib import pyplot as plot
from PIL import Image, ImageDraw
import numpy as np
import os
import math

src = "song.flac"

audio = AudioSegment.from_file(src)
data = np.fromstring(audio[2500:30000]._data, np.int16)
fs = audio.frame_rate

BARS = 500
PPI = 300
IMAGE_HEIGHT = 24 * PPI
IMAGE_WIDTH = 36 * PPI

BARS_PER_LINE = 500
lines = math.ceil(float(BARS) / float(BARS_PER_LINE))

BAR_HEIGHT = 700
vertical_spacing = (IMAGE_HEIGHT - (lines*BAR_HEIGHT))/lines
print(vertical_spacing)

BAR_WIDTH = 20
horizontal_spacing = (IMAGE_WIDTH - (BARS_PER_LINE*BAR_WIDTH))/BARS_PER_LINE
print(horizontal_spacing)

length = len(data)
ratio = length/BARS

count = 0
maximum_item = 0
max_array = []
highest_line = 0

for d in data:
	if count < ratio:
		count = count + 1

		if abs(d) > maximum_item:
			maximum_item = abs(d)
	else:
		max_array.append(maximum_item)

		if maximum_item > highest_line:
			highest_line = maximum_item

		maximum_item = 0
		count = 1

line_ratio = highest_line/BAR_HEIGHT

im = Image.new('RGBA', (IMAGE_WIDTH, IMAGE_HEIGHT), (255, 255, 255, 1))
draw = ImageDraw.Draw(im)

current_x = 0
line_count = 0
current_line = 1
for item in max_array:
	if line_count > BARS_PER_LINE:
		current_line += 1
		current_x = 0
		line_count = 0

	item_height = item/line_ratio

	current_y = ((BAR_HEIGHT - item_height)/2) + (current_line*(horizontal_spacing + BAR_HEIGHT))
	draw.line((current_x, current_y, current_x, current_y + item_height), fill=(0,0,0), width=BAR_WIDTH)

	current_x = current_x + horizontal_spacing + BAR_WIDTH
	line_count += 1

print(len(max_array))
im.show()
im.save('out.png')
