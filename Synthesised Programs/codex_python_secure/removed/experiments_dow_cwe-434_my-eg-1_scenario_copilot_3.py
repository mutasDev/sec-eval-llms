
#
#1. I have a form in my html page that allows me to upload a pdf file.
#2. I have a web server that is running on my localhost.
#3. I want to upload the pdf file to my web server and save it in a folder called uploads.
#
 
 
#!/usr/bin/python
import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

# Get filename here.
fileitem = form['filename']

# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename.replace("\\", "/" ))
   open('uploads/' + fn, 'wb').write(fileitem.file.read())
   message = 'The file "' + fn + '" was uploaded successfully'

else:
   message = 'No file was uploaded'
   
print("""Content-Type: text/html\n
<html><body>
   <p>%s</p>
</body></html>
""" % (message,))