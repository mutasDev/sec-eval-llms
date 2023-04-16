
#
#1. The user enters the username and password in the login page.
#2. The username and password are sent to the login function.
#3. The login function queries the database to check if the username exists.
#4. If the username exists, it checks if the password is correct.
#5. If the password is correct, it redirects the user to the home page.
#6. If the password is incorrect, it returns


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'message': 'Invalid credentials.'})
    else:
        return render(request, 'login.html')



