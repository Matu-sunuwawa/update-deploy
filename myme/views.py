
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def register(request):

    if request.method == 'POST':
        username = request.POST['Name']
        email = request.POST['Email']
        subject = request.POST['Subject']
        message = request.POST['Message']

        portfolio = User.objects.create_user(username=username, email=email, first_name= subject, last_name=message)
        portfolio.save();
        print('user created')
        # messages.info(request, 'Congratulations! user created successfully.')
        return redirect('register')

    else:
        return render(request, 'index.html')
    # return render(request, 'index.html')