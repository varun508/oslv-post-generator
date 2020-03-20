from PIL import Image, ImageDraw, ImageFont, ImageOps


def render_footer(url, name, image):
    img = image
    _render_dev_avatar(url, img)
    _render_dev_username(name, img)
    _render_dev_account_url(name, img)


def _render_dev_avatar(url, img):
    size = (300, 300)
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    mask = mask.resize((100, 100), Image.ANTIALIAS)
    img_new = Image.open('res/img/avatar.png', 'r')
    img_new.thumbnail((100, 100), Image.ANTIALIAS)
    output = ImageOps.fit(img_new, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    output.save('generated/avatar_new.png')
    img.paste(output, (60, 910), output)


def _render_dev_username(name, img):
    fontsize = int(660 / len(name))
    if fontsize > 38:
        fontsize = 38
    font = ImageFont.truetype("res/font/RobotoMono-Regular.ttf", fontsize)
    draw = ImageDraw.Draw(img)
    draw.text((200, 910), name, (255, 255, 255), font=font)


def _render_dev_account_url(name, img):
    name = "github.com/" + name
    fontsize = int(660 / len(name))
    if fontsize > 30:
        fontsize = 30
    font = ImageFont.truetype("res/font/RobotoMono-Regular.ttf", fontsize)
    draw = ImageDraw.Draw(img)
    draw.text((200, 960), name, (92, 225, 230), font=font)
