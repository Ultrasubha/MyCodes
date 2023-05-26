from PIL import Image
import os

def compress(image_file):
    
    filepath = os.path.join(os.getcwd(), image_file)

    image = Image.open(filepath).convert('RGB')

    image.save("image-file-compressed.JPEG", 
                 "JPEG", 
                 optimize = True, 
                 quality = 90)
    return

compress("a.png")