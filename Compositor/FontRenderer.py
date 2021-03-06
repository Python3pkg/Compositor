from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

_ROOT = os.path.abspath(os.path.dirname(__file__))
def get_data_path(path):
        return os.path.join(_ROOT, 'data', path)

def monaco(size):
    return ImageFont.truetype(get_data_path("Monaco.ttf"), size)

def courier(size):
    return ImageFont.truetype(get_data_path("Courier.ttf"), size)

class FontRenderer(object):
    def __init__(self, font, ink=(0, 0, 0, 255), fill=(255, 255, 255, 0)):
        self._font = font
        self._ink = ink
        self._fill = fill

    def render(self, text):
        '''Render a bitmap array of the provided text,
        :text: should be unicode if you want good behaviour'''
        bbox = self.get_bbox(text)
        background = Image.new("RGBA", bbox, self._fill)
        context = ImageDraw.Draw(background)
        context.text((0, 0), text, font=self._font, fill=self._ink)
        return background

    def get_bbox(self, text):
        '''Find the bounding box for the text given the font properties,
        relies on font being monospace'''
        x, y = self._font.getmetrics()
        z = (x + y)
        return len(text) * z / 2, z
