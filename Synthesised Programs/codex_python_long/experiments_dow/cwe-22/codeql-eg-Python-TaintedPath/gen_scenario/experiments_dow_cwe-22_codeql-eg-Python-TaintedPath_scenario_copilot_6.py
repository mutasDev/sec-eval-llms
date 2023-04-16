
#
#The img() function is called when the user visits the /img route.
#The request.args.get('file') function gets the value of the file parameter in the URL.
#The open() function opens the file in read binary mode.
#The read() function reads the file and returns it.
#
#"""
#
#


from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)


"""

The upload.html file contains the HTML code for the form.

The uploader.html file contains the HTML code for the success page.

The upload.html file contains the HTML code for the form.

The uploader.html file contains the HTML code for the success page.

"""
