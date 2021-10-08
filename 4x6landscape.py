#landscpe 4x6

from gimpfu import *

def landscape46(image, drawable):
    # Image
    # Scale Image

    new_height = 1200
    new_width = (new_height*image.width)/image.height
    
    pdb.gimp_image_scale(image, new_width, new_height)
    
    
register(
    "python-fu-landscape46",
    "scales image 4x6",
    "Scales images to 1800 high, preserve form factor and save as jpg, png and webp files.",
    "Akeeal", "Akeeal", "2020",
    "Scale to Landscape 4x6",
    "", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None)
    ],
    [],
    landscape46, menu="<Image>/READY PICTURE/STEP 1 = Scaling to 6x4 or 4x6 photo")  # second item is menu location

main()
