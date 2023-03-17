import sys
from PIL import Image, ImageOps

inp = sys.argv[1]
outp = sys.argv[2]
exts = [".jpg", ".jpeg", ".png"]

if not len(sys.argv) == 3:
    sys.exit("Example usage: python shirt.py input.jpg output.jpg")
for ext in exts:
    if inp.endswith(ext) and outp.endswith(ext):
        break
    else:
        sys.exit("Files must have the same extenstion (.jpg, .jpeg, .png)")

shirt = Image.open("shirt.png")
shirt_size = shirt.size

try:
    input_image = Image.open(inp)
    input_size = input_image.size
except FileNotFoundError:
    sys.exit(f"{inp} not found.")

resized_input = ImageOps.fit(input_image, shirt_size)

resized_input.paste(shirt, (0, 0), shirt)

resized_input.save(outp)
