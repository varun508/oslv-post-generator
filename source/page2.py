from PIL import Image, ImageDraw, ImageFont
from common import *


img = Image.open('res/img/page_2.png')
img_w, img_h = img.size


def create_page_2():
    render_footer(None, 'liyasthomas', img)
    _render_project_name('liyasthomas', 'postwoman')
    _render_info()
    img.save('generated/page_2_gen.png')


def _render_project_name(author, project_name):
    text = author + '/' + project_name
    fontsize = int(900 / len(text))
    if fontsize > 60:
        fontsize = 60
    font = ImageFont.truetype("res/font/RobotoMono-Bold.ttf", fontsize)
    draw = ImageDraw.Draw(img)
    draw.text((60, 265), text, (255, 255, 255), font=font)


def _render_info():
    fontsize = 30
    font = ImageFont.truetype("res/font/RobotoMono-Regular.ttf", fontsize)
    draw = ImageDraw.Draw(img)
    draw.text((115, 492), '1627', (255, 255, 255), font=font)  # commits
    draw.text((115, 643), '62', (255, 255, 255), font=font)  # contributors
    draw.text((115, 787), '15', (255, 255, 255), font=font)  # issues
    draw.text((738, 492), '17.3K', (255, 255, 255), font=font)  # stars
    draw.text((738, 643), '1K', (255, 255, 255), font=font)  # forks
    draw.text((738, 787), '5', (255, 255, 255), font=font)  # releases
