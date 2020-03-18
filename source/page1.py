from PIL import Image, ImageDraw, ImageFont
from constants import *

img = Image.open('res/img/page_1.png')
img_w, img_h = img.size


def _render_post_number(pos_no):
    font = ImageFont.truetype("res/font/RobotoMono-Regular.ttf", 80)
    text = "#" + str(pos_no)
    text_x = img_w - (font.getsize(text)[0] + margin_horizontal)
    print(font.getsize(text)[1])
    text_y = margin_top
    draw = ImageDraw.Draw(img)
    draw.text((text_x, text_y), text, (67, 222, 164), font=font)


def _render_project_image(url):
    img_new = Image.open('res/img/abc.png', 'r')
    img_w, img_h = img_new.size
    img_new.thumbnail((200, 100), Image.ANTIALIAS)
    img_new.save('generated/abc_new.png')
    im = Image.open('generated/abc_new.png', 'r')
    img.paste(im, (300, 300), im)


def create_page_1(post_number):
    _render_post_number(post_number)
    _render_project_image("postwoman", None)
    img.save('generated/page_1_gen.png')


def _remove_aplha(image):
    alpha1 = 0  # Original value
    r2, g2, b2, alpha2 = 0, 0, 0, 255  # Value that we want to replace it with

    red, green, blue, alpha = data[:, :, 0], data[:,
                                                  :, 1], data[:, :, 2], data[:, :, 3]
    mask = (alpha == alpha1)
    data[:, :, :3][mask] = [r2, g2, b2, alpha2]

    data = np.array(image)
    return Image.fromarray(data)
