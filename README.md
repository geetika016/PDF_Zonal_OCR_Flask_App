# PROJECT DESCRIPTION

## What is in this Repository?
This repository contains the code for a Flask App that takes a pdf document in, finds the page of interest (in our case it was a certificate in the document) and then does OCR on this page and extracts the values of field of interest and displays it on the screen. The app can be modified to accept a zip folder containing more than one document and extract and display the extracted certificates, aggregate the data in a csv that can be downloaded and also click on each certificate individually to view the fields-values and also validate a few values against a database.

## What are the features of this Flask App?

* Take a single document or a zip folder containing .pdf documents of interest
* Extract the page of Interest from these documents (if the document contains that page)
* Do Zonal OCR on this Page of Interest ( a page with a form-like structure containing fields and their value)
* In case of a single document the fields of interest are displayed, can be downloaded as a .csv
![image]()
* In case of multiple documents, the app displays the results of for all the documents, a View All option to view each documents extracted page of interest and on clicking the page, the extracted results are displayed for that particular document.
![image]()



## Prerequisites 
Python : 3.6 or above
[Flask](https://flask.palletsprojects.com/en/1.1.x/installation/)
		

## Steps to run this :
1. Open the directory that contains the code, I would recommend creating a virtual environment before installing the dependencies using the command:
	
		pip install -r requirements.txt

2. You can specify the constraints required to search for the page in the file : pdf_classification.py.

3. go to app folder and run:

		python app.py

4. Web app Home can be viewed on localhost, port 5000.

5. Upload a single pdf document( a complete document that contains page of interest as one of the pages), or a .zip folder containing more than one .pdf documents. 
