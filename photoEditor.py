from PIL import Image, ImageEnhance, ImageFilter
import os


path = './imgs'
pathout = '/editedImgs'

# # Create output directory
# try:
#     os.mkdir(pathout)
# except OSError as error:
#     print(error)

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    edit = img.filter(ImageFilter.SHARPEN)
    factor = 2
    color_enhancer = ImageEnhance.Color(edit)
    contrast_enhancer = ImageEnhance.Contrast(edit)
    # edit = color_enhancer.enhance(factor)
    edit = contrast_enhancer.enhance(factor)
    clean_name = os.path.splitext(filename)[0]
    edit.save(f".{pathout}/{clean_name}_edited.jpg")
