from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):

    if request.method == "POST":
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')

        else:
            return redirect('login')

    else:
        return render(request, 'userpages/login.html')

def logout(request):
    # if request.method == 'POST':
    auth.logout(request)

    return redirect('home')

def signup(request):
    if request.method == "GET":
        return render(request, 'userpages/signup.html')

    else:
        inData = request.POST
        try:
            user = User.objects.create_user(username=inData['username'], first_name = inData['firstname'], last_name = inData['lastname'], email = inData['email'], password = inData['password'])
            user.save()

            u_stat = UserStat()
            u_stat.user = user
            u_stat.shipping_address = inData['address']
            u_stat.country = inData['country']

            auth.login(request, user)
        except:
            pass

        return redirect('home')
