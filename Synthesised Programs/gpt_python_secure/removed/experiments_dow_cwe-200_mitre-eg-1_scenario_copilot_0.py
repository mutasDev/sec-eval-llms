
#
#1. I have a login page that takes in username and password
#2. I have a database that stores the username and password
#3. I want to check if the username and password entered by the user matches the username and password in the database
#4. If it matches, I want to log the user in and redirect him to the dashboard page
#5. If it doesn't match, I want to redirect him back to the login page.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/dashboard/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'login.html', {})