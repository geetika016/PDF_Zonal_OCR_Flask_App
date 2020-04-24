import pdf_classification
#import re
#import os
"""
for foldername,subfolders,files in os.walk(r"/Users/geetikasharma/Downloads/20200219123803"):
	for file in files:
    	pdfFile = os.path.join(foldername,file)
    	outPdfFile = pdfFile.replace(".pdf","_searched_extracted.pdf")
    	stringList = ["PHYTOSANITARY CERTIFICATE"]
    	pdf_classification.extractPage(pdfFile, outPdfFile, findText(pdfFile, stringList))
print("DONE")

"""

from os import listdir
from os.path import isfile, join
import re
import glob, os

def multi_classification(pdf_folder_path,pdf_folder_name):
	onlyfiles = [f for f in listdir(pdf_folder_path) if isfile(join(pdf_folder_path, f))]

	for file in onlyfiles:
		pdfFile = os.path.join(pdf_folder_path,file)
		outPdfFile = os.path.join('./temp',file)
		stringList = ["Phytosanitary Certificate"]
		pdf_classification.extractPage(pdfFile, outPdfFile, pdf_classification.findText(pdfFile, stringList))	
	print("DONE")