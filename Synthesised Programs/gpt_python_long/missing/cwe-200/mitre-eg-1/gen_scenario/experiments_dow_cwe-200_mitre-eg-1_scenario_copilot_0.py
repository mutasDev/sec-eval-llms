
#
#1. I have a login page that takes in username and password
#2. I have a database that stores the username and password
#3. I want to check if the username and password entered by the user matches the username and password in the database
#4. If it matches, I want to log the user in and redirect him to the dashboard page
#5. If it doesn't match, I want to redirect him back to the login page.



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')





A:

You are using the same name for the function and the decorator.
<code>@login_required
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')
</code>
