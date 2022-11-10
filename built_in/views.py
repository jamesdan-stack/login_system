from django.shortcuts import render
from .forms import Loginform
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = Loginform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('done')

                else:
                    return HttpResponse('disabled account')

            else:
                return HttpResponse('invalid login')

    else:
        form = Loginform
        return render (request, 'registration/second_login.html', {'form':form})
