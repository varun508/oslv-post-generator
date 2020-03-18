from PIL import Image, ImageDraw, ImageFont

def create_page_1():
    font = ImageFont.truetype("res/font/RobotoMono-Bold.ttf", 56)
    img = Image.open('res/img/page_1.png')
    draw = ImageDraw.Draw(img)
    draw.text((60, 180), "postwoman", (255, 255, 255), font=font)
    img_w, img_h = img.size
    img.save('generated/page_1_gen.png')
    print(img_w, img_h)
