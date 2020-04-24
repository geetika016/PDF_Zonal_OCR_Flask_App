from pdf2image import convert_from_path

def convert_and_save(filename):
	pages = convert_from_path(filename, 300)
	for i, page in enumerate(pages):
		filename = filename.replace("./temp/","")
		page_name = "./ocr_images/phyto_image.jpg"
		page.save(page_name, 'JPEG')
		if i>0:
			break