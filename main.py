from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype("RobotoMono-Regular.ttf", 50)

img = Image.open('pil_text.png')
img_w, img_h = img.size
background = Image.new('RGB', (1440, 900), (255, 0 , 0))
bg_w, bg_h = background.size
offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
background.paste(img, offset)

background.save('background.png')
