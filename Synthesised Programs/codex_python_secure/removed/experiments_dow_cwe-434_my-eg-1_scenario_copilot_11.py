
#
#1. The upload_pdf() function is called when the user uploads a pdf file.
#2. The pdf file is saved in the uploads folder.
#3. The filepath of the pdf file is saved in the mysql database.
#4. The filepath is then used to download the pdf file.
#


#1. Create a function to upload the pdf file
@app.route('/upload', methods=['GET', 'POST'])
def upload_pdf():
	if request.method=='POST':
		#2. Get the file from the request object
		f = request.files['file']
		#3. Save the file to the uploads folder
		f.save(secure_filename(f.filename))
		#4. Get the filepath of the uploaded pdf file
		filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
		#5. Save the filepath in the database
		#6. Download the pdf file
		return '<h1>'+filepath+'</h1>'
	else:
		return '<h1>Get Method</h1>'

#main function
if __name__ == '__main__':
	app.run(debug=True)