from PIL import Image, ImageDraw

img = Image.open('pil_text.png')

d = ImageDraw.Draw(img)
d.text((5, 5), "Hello World", fill=(255, 0, 0))

img.save('pil_text.png')
