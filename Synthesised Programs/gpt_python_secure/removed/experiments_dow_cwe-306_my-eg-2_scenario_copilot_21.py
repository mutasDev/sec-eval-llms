
#
#1. The first function is the login function. It is a GET request. It will return a form for the user to enter their username and password.
#
#2. The second function is the do_login function. It is a POST request. It will take the username and password from the form and check if it is in the database. If it is, it will redirect the user to the user_page. If it is not, it will return


def login(request):
    if request.method == 'GET':
        return render_to_response('login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/user_page/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")