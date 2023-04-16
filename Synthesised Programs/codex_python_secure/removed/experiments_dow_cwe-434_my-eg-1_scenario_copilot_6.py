
#
#1. I have a web app that accepts a pdf file and saves it in a folder called uploads.
#
#2. I have a script that converts the pdf file to text and saves it in a folder called text.
#
#3. I have a script that reads the text file and saves it in a database.
#

import os
import sys
import shutil

# Function to upload files to the server

def upload_file(f):
    with open('uploads/' + f.filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# Function to convert pdf to text

def convert_pdf_to_txt(path):
    rsrcmgr = pdfminer.pdfinterp.PDFResourceManager()
    retstr = StringIO()
    layoutmode = pdfminer.layout.LAParams(detect_vertical=True)
    device = pdfminer.converter.TextConverter(rsrcmgr, retstr, laparams=layoutmode)
    fp = open(path, 'rb')
    process_pdf(rsrcmgr, device, fp)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str

# Function to read the text file and save it in the database

def read_text_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
        return text