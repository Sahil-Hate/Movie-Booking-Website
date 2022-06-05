from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')


def page(request):
    movies = Movie.objects.all()    #fetches all objects of class Movie
    return render(request,'page.html',{"movies":movies})


def detail_page(request,id):
    mov = Movie.objects.all()
    m = Movie.objects.get(id=id)    #get se ek he cheez fetch hoga
    movies = []   
    for i in mov:
        if i!=m:
            movies.append(i)
    movie_cast = MovieCast.objects.filter(movie = m)    #filter se query set aayega and its similar to list
    return render(request,'detail_page.html',{"movie_id":m, "cast":movie_cast,"movies":movies})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    
    else:
        return render(request,'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken!')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.info(request,'User Created!')
                return render(request,'confirmation.html')
        else:
            messages.info(request,'Passwords do not match')
            return render(request,'signup.html')

    else:  
        return render(request,'signup.html')



def confirmation(request):
    return render(request,'confirmation.html')


def logout(request):
    auth.logout(request)
    return redirect("/")


def prebooking(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            movies = Movie.objects.all()
            return render(request,'prebooking.html',{"movies":movies})

        if request.method == 'POST':
            movie = request.POST["movies"]
            date = request.POST["date"]
            return redirect("booking/" + movie + "/" + date + "/")
    else:
        return redirect('/login')


def booking(request,movie,date):
    if request.user.is_authenticated:
        seats = Seat.objects.all().order_by("seat_identity")
        booked_seats = []
        m = Movie.objects.get(name = movie)
        if request.method=="POST":
            selected_seats=request.POST.get("abc").split(";")
            selected_seats.pop()
            print(selected_seats)
            for i in selected_seats:
                seat = Seat.objects.get(seat_identity=i)
                Booking.objects.create(customer=request.user,seat=seat,movie=m,date=date)
        X = Booking.objects.filter(movie=m,date=date)
        for i in X:
            booked_seats.append(i.seat.seat_identity)
        return render(request,'booking.html',{"movie":movie,"date":date,"seats":seats,"booked_seats":booked_seats})
    else:
        return redirect('/login')
    