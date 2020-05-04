from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from LoginScreen import classes
from dashboard import views as DashboardViews

# Create your views here.

def UserLogin(request):
    if request.user.is_authenticated:
        return DashboardViews.home(request)
    if request.method == 'GET':
        form = classes.OverrideAuthenticationForm()
        return render(request, 'loginscreen/login.html', {'form': form, 'title':'Login'})
    if request.method == 'POST':
        form = classes.OverrideAuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return DashboardViews.home(request)
            else:
                return render(request, 'loginscreen/login.html', {form: form, 'title':'Login'})
        else:
            # If there were errors, we render the form with these
            # errors
            return render(request, 'loginscreen/login.html', {'form': form, 'title':'Login'}) 