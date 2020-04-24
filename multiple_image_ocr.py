import os
import phyto_ocr

def ocr_multiple_image():
    for filename in os.listdir('./ocr_images'):
        print(os.path.join('./ocr_images',filename))
        phyto_ocr.ocr_function(os.path.join('./ocr_images',filename))
        

    print("multi_image_ocr_done")