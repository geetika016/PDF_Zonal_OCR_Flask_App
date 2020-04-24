from pdf2image import convert_from_path

def convert_and_save(filename):
	pages = convert_from_path(filename, 300)
	for i, page in enumerate(pages):
		page.save("./ocr_image/phyto_image.jpg", 'JPEG')
		if i>0:
			break