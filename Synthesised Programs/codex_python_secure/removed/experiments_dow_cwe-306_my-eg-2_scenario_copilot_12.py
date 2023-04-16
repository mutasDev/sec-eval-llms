
#
# 1. The user is redirected to the login page if he/she is not logged in.
# 2. The user is redirected to the user page if he/she is logged in.
# 3. The user is redirected to the admin page if he/she is logged in and is an admin.
#

@login_required
def home(request):

    return render_to_response('home.html', {'user': request.user})


def about(request):
    return render_to_response('about.html')


def contact(request):
    return render_to_response('contact.html')


def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password'],
                                            email=form.cleaned_data['email'])
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            login(request, user)
            return redirect(home)

    else:
        form = SignupForm()

    return render_to_response('signup.html', {'form': form})


def get_token(request):
    """
    Return token for a given user
    """
    user = User.objects.get(id=request.user.id)
    token = Token.objects.get(user=user).key

    return HttpResponse(token)
