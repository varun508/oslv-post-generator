from PIL import Image, ImageDraw, ImageFont, ImageOps
from constants import *

img = Image.open('res/img/page_1.png')
img_w, img_h = img.size


def _render_post_number(pos_no):
    font = ImageFont.truetype("res/font/RobotoMono-Regular.ttf", 80)
    text = "#" + str(pos_no)
    text_x = img_w - (font.getsize(text)[0] + margin_horizontal)
    text_y = margin_top
    draw = ImageDraw.Draw(img)
    draw.text((text_x, text_y), text, (67, 222, 164), font=font)


def _render_project_image(url):
    img_new = Image.open('res/img/abc.png', 'r')
    img_w, img_h = img_new.size
    img_new.thumbnail((220, 110), Image.ANTIALIAS)
    img_new.save('generated/abc_new.png')
    im = Image.open('generated/abc_new.png', 'r')
    img.paste(im, (800, 240), im)


def _render_project_title(name):
    fontsize = int(700 / len(name))
    if fontsize > 60:
        fontsize = 60
    font = ImageFont.truetype("res/font/RobotoMono-Bold.ttf", fontsize)
    draw = ImageDraw.Draw(img)
    draw.text((60, 225), name, (255, 255, 255), font=font)


def _render_project_subtitle(subtitle):
    fontsize = int(700 / len(subtitle))
    if fontsize > 25:
        fontsize = 25
    font = ImageFont.truetype("res/font/RobotoMono-Regular.ttf", fontsize)
    print(font.getsize("d"))
    draw = ImageDraw.Draw(img)
    draw.text((60, 310), subtitle, (166, 166, 166), font=font)


def _render_dev_avatar(url):
    size = (300, 300)
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    mask = mask.resize((100, 100), Image.ANTIALIAS)
    img_new = Image.open('res/img/avatar.png', 'r')
    img_w, img_h = img_new.size
    img_new.thumbnail((100, 100), Image.ANTIALIAS)
    img_new.save('generated/avatar_new.png')
    img_new = Image.open('generated/avatar_new.png', 'r')
    output = ImageOps.fit(img_new, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    output.save('generated/avatar_new.png')
    img.paste(output, (60, 910), output)


def _render_dev_username(name):
    fontsize = int(660 / len(name))
    if fontsize > 38:
        fontsize = 38
    font = ImageFont.truetype("res/font/RobotoMono-Regular.ttf", fontsize)
    draw = ImageDraw.Draw(img)
    draw.text((200, 910), name, (255, 255, 255), font=font)


def _render_dev_account_url(name):
    name = "github.com/" + name
    fontsize = int(660 / len(name))
    if fontsize > 30:
        fontsize = 30
    font = ImageFont.truetype("res/font/RobotoMono-Regular.ttf", fontsize)
    print(font.getsize("d"))
    draw = ImageDraw.Draw(img)
    draw.text((200, 960), name, (92, 225, 230), font=font)


def create_page_1(post_number):
    _render_post_number(post_number)
    _render_project_image(None)
    _render_project_title("postwoman")
    _render_project_subtitle("liyasthomas/postwoman")
    _render_dev_avatar(None)
    _render_dev_username('liyasthomas')
    _render_dev_account_url('liyasthomas')
    img.save('generated/page_1_gen.png')
