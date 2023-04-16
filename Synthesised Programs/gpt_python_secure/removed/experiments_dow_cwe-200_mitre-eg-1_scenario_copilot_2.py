
#
#1. I have a login.html page which has a form with username and password fields.
#2. I have a login.py file which has a login function which takes the username and password from the form and checks if the username and password exists in the database.
#3. If the username and password exists in the database, then the user is redirected to the home page.
#4. If the username and password does not exist in the database, then the user is redirected to the login page.

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/home/')
                else:
                    return redirect('/login/')
            else:
                return redirect('/login/')
        else:
            return redirect('/login/')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})