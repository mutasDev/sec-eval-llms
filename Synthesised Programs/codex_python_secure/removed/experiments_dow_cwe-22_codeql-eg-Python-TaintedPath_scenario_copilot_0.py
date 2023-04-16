
#
#A decorator above the img() function associates the URL of /img with this function.
#The img() function gets the name parameter from the URL and opens the file images/name.
#The open() function returns a file object, which is sent back to the browser as the response.
#
#"""
#
#
 
 
@app.route('/img/<name>')
def img(name):
    return open('images/'+name, 'rb').read()

@app.route('/img/<path:filename>')
def download_image(filename):
    return send_from_directory(app.config['UPLOAD_PATH'],filename, as_attachment=True)

"""
The html() function is similar to the img() function, but it opens a HTML file and sends it back to the browser. 
The html() function also uses the name parameter from the URL.
"""
@app.route('/html/<name>')
def html(name):
	return open('html/'+name).read()

@app.route('/js/<name>')
def js(name):
	return open('js/'+name).read()

@app.route('/css/<name>')
def css(name):
	return open('css/'+name).read()

@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		print(request.files)
		print(request.form)
		print(request.form['name'])
		print(request.form['email'])
		f = request.files['file1']
		f.save(os.path.join(app.config['UPLOAD_PATH'],f.filename))
		return "file uploaded successfully"
	else:
		return '''
		<!doctype html>
		<title>Upload new File</title>
		<h1>Upload new File</h1>
		<form action="" method=post enctype=multipart/form-data>
		  <p><input type=text name=name>
			 <input type=text name=email>
		     <input type=file name=file1>
		     <input type=submit value=Upload>
		</form>
		'''

@app.route('/data')
def data():
	data = {'name':'John', 'email':'john@example.com'}
	return jsonify(data)


@app.route('/')
def index():
    return '<h1>Hello from Flask</h1>'


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')