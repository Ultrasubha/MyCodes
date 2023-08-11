#from PIL import Image
#import os
#
#def compress(image_file):
#    
#    filepath = os.path.join(os.getcwd(), image_file)
#
#    image = Image.open(filepath).convert('RGB')
#
#    image.save("image-file-compressed.JPEG", 
#                 "JPEG", 
#                 optimize = True, 
#                 quality = 90)
#    return
#
#compress("a.png")

#import random
#print(random.sample([i for i in range(9999)], 199))
# doubled(obj):
#    return obj[:-2]
#x = list(map(lambda s: s[:-2],["gold 2", "red 1", "green 3", "blue 5"]))
y = ["hi 5", "lo 1", "hello 3", "world 4"]
print(y.find("lo"))