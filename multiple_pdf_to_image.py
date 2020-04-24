import os
import pdf_to_image_for_ocr

def multiple_pdf_convert():
    for filename in os.listdir('./temp'):
        print(os.path.join('./temp',filename))
        if filename.endswith(".pdf"):
            pdf_to_image_for_ocr.convert_and_save(os.path.join('./temp',filename))
    print("to image : Done!")