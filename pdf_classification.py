import re
from PyPDF2 import PdfFileReader, PdfFileWriter
import glob, os

# find pages
def  findText(f, slist):
    file = open(f, 'rb')
    pdfDoc = PdfFileReader(file)
    pages = []
    for i in range(pdfDoc.getNumPages()):
        content = pdfDoc.getPage(i).extractText().lower()
        s2 = "USDA"
        for s in slist:
            if re.search(s.lower(), content) is not None:
                if re.search(s2.lower(),content) is not None:
                    if i not in pages:
                        pages.append(i)
                        break
    return pages

#extract pages
def extractPage(f, fOut, pages):
    file = open(f, 'rb')
    output = PdfFileWriter()
    pdfOne = PdfFileReader(file)
    print(pages)
    if not pages:
        return
    for i in pages:
        output.addPage(pdfOne.getPage(i))
    outputStream = open(fOut, "wb")
    output.write(outputStream)
    outputStream.close()
    return