import os
import zipfile
from flask import Flask, request, redirect, url_for, flash, render_template
from werkzeug.utils import secure_filename
import processor
import pandas as pd

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            global pdf_folder_path, pdf_filename
            pdf_filename = filename[:-4]
            pdf_folder_path = "./uploads"
            print(filename)
            print(pdf_filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            #zip_ref = zipfile.ZipFile(os.path.join(UPLOAD_FOLDER, filename), 'r')
            #zip_ref.extractall(os.path.join(pdf_folder_path))
            #zip_ref.close()
            #return 'file uploaded successfully'
            #return render_template('processing.html')
            return redirect(url_for('processing'))
    return render_template('home.html')

@app.route('/processing')
def processing():
    retval =""
    retval = processor.start_processing(pdf_folder_path,pdf_filename)
    if (retval == "hello"):
        data = pd.read_csv("./data/result.csv")
        #data.set_index(['File_ID'], inplace=True)
        return render_template('results.html',tables=[data.to_html()],titles = ['na', 'OCR Results'])
    return render_template('no_phyto.html')


    
'''
***** to do add app route to  display results ****
**** also add app route when authentication is done : should be / ****
*** change / to home then 
'''

if __name__ == "__main__":
    app.run(debug=True)