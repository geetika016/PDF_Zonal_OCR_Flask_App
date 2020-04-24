import multiple_pdf_classification
import multiple_pdf_to_image
import textract_ocr

def start_processing(pdf_folder_path,pdf_folder_name):
    print(pdf_folder_name)
    multiple_pdf_classification.multi_classification(pdf_folder_path,pdf_folder_name)
    multiple_pdf_to_image.multiple_pdf_convert()
    textract_ocr.ocr_this("./ocr_images/phyto_image.jpg")
    return "hello"