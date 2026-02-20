from django.shortcuts import render, redirect
from django.contrib.auth.models import User #Import the User model
from django.contrib.auth import authenticate, login, logout #Import the authentication functions
# from django.db.models import Q #Import the Q object for complex queries

# Create your views here.
def home(request):
    users = User.objects.all() #Get all users from the database
    return render(request, 'accounts/accounts.html', {'users': users}) #Render the home template with the users context

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'accounts/login.html') #Render the login template

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        user = User.objects.create_user(
            username=username, 
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
        
        )

    return render(request, 'accounts/register.html') #Render the login template

def user_logout(request):
    logout(request)
    return redirect('home') #Redirect to the home page after logging out

def search_users(request):
    query = request.GET.get('q')
    if query:
    #     users = User.objects.filter(
    #     Q(username__icontains=query) |
    #     Q(email__icontains=query) |
    #     Q(first_name__icontains=query) |
    #     Q(last_name__icontains=query)
    # ) #Search for users whose username contains the query
        users = User.objects.filter(username__icontains=query) | User.objects.filter(email__icontains=query) | User.objects.filter(first_name__icontains=query) | User.objects.filter(last_name__icontains=query)
        print(users)
    else:
        users = User.objects.all() #If no query, return all users
    return render(request, 'accounts/accounts.html', {'users': users}) #Render the home template with the search results