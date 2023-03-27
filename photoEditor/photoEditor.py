from PIL import Image, ImageFilter, ImageEnhance, ImageColor
import os

path = "./img"                                                  # local folder for unedited images
pathOut = "/editedImgs"                                         # local folder for edited images

for filename in os.listdir(path):                               # for a given image in the first folder
    if filename == '.DS_Store':                                  # skips .DS_Store file, which macOS creates when using finder
        continue
    img = Image.open(f"{path}/{filename}")                      # open the image
    edit = img.filter(ImageFilter.EDGE_ENHANCE).convert("L")    # filter - enhance edges, convert to monochrome
    factor = 1.5                                                # set a factor amount
    enhancer = ImageEnhance.Contrast(edit)                      # create a contrast enhancer
    edit = enhancer.enhance(factor)                             # use the enhancer by preset factor 
    clean_name = os.path.splitext(filename)[0]                  # splts filename and extension, creating tuple
    edit.save(f'.{pathOut}/{clean_name}_edited.png')            # save the edited image to the local folder, using prev tuple to create name