from pydub import AudioSegment
from matplotlib import pyplot as plot
from PIL import Image, ImageDraw
import numpy as np
import os

src = "song.flac"

audio = AudioSegment.from_file(src, format='flac', frame_rate=44100, sample_width=2, channels=2)
segment = audio[:30000]

data = np.fromstring(segment._data, np.int16)
fs = audio.frame_rate

IMAGE_HEIGHT = 1000
IMAGE_WIDTH = 1000

BAR_WIDTH = 60




BAR_HEIGHT = 60
LINE_WIDTH = 3
highest_line = 0
WIDTH_SPACING = 1
HEIGHT_SPACING = BAR_HEIGHT + 5
IMAGE_WIDTH = 500 * LINE_WIDTH + (WIDTH_SPACING * LINE_WIDTH)
IMAGE_HEIGHT = 500 * BAR_HEIGHT + (SPACING * BAR_HEIGHT)

for d in xrange(length):
  if abs(d) > highest_line:
      highest_line = abs(d)

line_ratio = highest_line/BAR_HEIGHT


im = Image.new('RGBA', (IMAGE_WIDTH, IMAGE_HEIGHT), (255, 255, 255, 1))
draw = ImageDraw.Draw(im)

current_x = 1
for item in data:
    if (current_x > IMAGE_WIDTH):
        current_x = 1
        current_y = (BAR_HEIGHT - item_height)/2 + highest_line +


    item_height = item/line_ratio

    current_y = (BAR_HEIGHT - item_height)/2
    draw.line((current_x, current_y, current_x, current_y + item_height), fill=(169, 171, 172), width=LINE_WIDTH)

    current_x = current_x + LINE_WIDTH + SPACING

im.show()
