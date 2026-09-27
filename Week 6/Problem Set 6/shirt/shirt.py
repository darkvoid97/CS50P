import sys, os
from PIL import Image, ImageOps

if error:=("Too few command-line arguments" if len(args:=sys.argv) <= 2
           else "Too many command-line arguments" if len(args) > 3
           else "Input does not exist" if not os.path.isfile(args[1])
           else "Invalid input" if (in_ext := os.path.splitext(args[1])[1].lower()) not in ('.png','.jpg','.jpeg')
           else "Invalid output" if (out_ext := os.path.splitext(args[2])[1].lower()) not in ('.png','.jpg','.jpeg')
           else "Input and output have different extensions" if in_ext != out_ext
           else None):
        sys.exit(error)

with Image.open(args[1]) as im:
       with Image.open("shirt.png") as shirt:
            after = ImageOps.fit(im, shirt.size)
            after.paste(shirt, shirt)
            after.save(args[2])
