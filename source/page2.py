from PIL import Image, ImageDraw, ImageFont
from common import *


img = Image.open('res/img/page_2.png')
img_w, img_h = img.size


def create_page_2():
    render_footer(None, 'liyasthomas', img)
    img.save('generated/page_2_gen.png')
