
#
#1. The first function is the login function. It is a GET request. It will return a form for the user to enter their username and password.
#
#2. The second function is the do_login function. It is a POST request. It will take the username and password from the form and check if it is in the database. If it is, it will redirect the user to the user_page. If it is not, it will return
 
 
 #https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Security#Sanitizing_user_input
def login(request):
    '''render login page'''
    return render(request, 'login.html')

def do_login(request):
    '''check username and password'''
    #get values from form
    username = request.POST['username']
    password = request.POST['password']

    #check if values match
    try:
        user = User.objects.get(username=username)
        if user.password == password:
            request.session['username'] = username
            return HttpResponseRedirect(reverse('user_page', args=[user.username]))
        else:
            return HttpResponseRedirect(reverse('login'))

    except User.DoesNotExist:
        return HttpResponseRedirect(reverse('login'))

def logout(request):
    '''Log out of session'''
    try:
        del request.session['username']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('login'))

def user_page(request, username):
    '''render user page'''
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse('login'))

    #check if session exists
    try:
        if request.session['username'] == user.username:
            return render(request, 'user_page.html', {'user':user})
        else:
            return HttpResponseRedirect(reverse('login'))
    except KeyError:
        return HttpResponseRedirect(reverse('login'))

def do_logout(request):
    '''Log out of session'''
    try:
        del request.session['username']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('login'))

def register(request):
    '''render register page'''
    return render(request, 'register.html')

def do_register(request):
    '''register user to database'''
    #get values from form
    username = request.POST['username']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']
    email = request.POST['email']

    #check if passwords match
    if password != confirm_password:
        return HttpResponseRedirect(reverse('register'))

    #check if username exists in database
    try:
        user = User.objects.get(username=username)
        return HttpResponseRedirect(reverse('register'))
    except User.DoesNotExist:
        user = User(username=username, password=password, email=email)
        user.save()
        return HttpResponseRedirect(reverse('login'))