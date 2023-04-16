
#empty


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/info')
def info():
    user = request.args.get('user')
    email = request.args.get('email')
    ssn = request.args.get('ssn')
    
    if user and email and ssn:
        return render_template('info.html', user=user, email=email, ssn=ssn[-4:])
    else:
        return render_template('error.html')

if __name__ == '__main__':
    app.run()
