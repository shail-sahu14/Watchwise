from django.shortcuts import render,redirect
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .recommender.utils import get_recommendations
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('emailid')
        password = request.POST.get('password')
        
        user = User.objects.create_user(username,email,password)
        user.save()
        
        return redirect('loginPage')
    return render(request,'base/signup.html')

def loginPage(request):
    if request.method == 'POST':
        usm = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request,username=usm,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('loginPage')
    return render(request,'base/loginPage.html')

def home(request):
    if request.method == 'POST':
        watchlist_name = request.POST.get('watchlist_name')
        obj = models.Watchlist(name=watchlist_name,user=request.user)
        obj.save()
        return redirect('home')
    watchlists = models.Watchlist.objects.filter(user=request.user)
    context = {'watchlists' : watchlists}
    return render(request,'base/home.html',context)

def editwatchlist(request,pk):
    if request.method == 'POST':
        watchlist_name = request.POST.get('watchlist_name')
        obj = models.Watchlist.objects.get(id=pk)
        obj.name = watchlist_name
        obj.save()
        return redirect('home')
    return render(request,'base/editwatch.html')

def deletewatchlist(request,pk):
    obj = models.Watchlist.objects.get(id=pk)
    obj.delete()
    return redirect('home')

def movies(request,pk):
    watchlist = models.Watchlist.objects.get(id=pk)
    request.session['watchlist'] = pk
    if request.method == 'POST':
        title = request.POST.get('title')
        obj = models.Movie(watchlist=watchlist,title=title)
        obj.save()
        return redirect('movies',obj.watchlist.id)
    movis = watchlist.movies.all()
    name = models.Watchlist.objects.get(id=pk).name
    context = {'movis':movis , 'name':name}
    return render(request,'base/movies.html',context)

def status(request,pk):
    obj = models.Movie.objects.get(id=pk)
    obj.status = not obj.status
    obj.save()
    return redirect('movies',obj.watchlist.id)

def deletemovie(request,pk):
    obj = models.Movie.objects.get(id=pk)
    obj.delete()
    return redirect('movies',obj.watchlist.id)

def editmovie(request,pk):
    if request.method == 'POST':
        title = request.POST.get('title')
        obj = models.Movie.objects.get(id=pk)
        obj.title = title
        obj.save()
        return redirect('movies',obj.watchlist.id)
    return render(request,'base/editmovie.html')

def recommend(request,pk):
    obj = models.Movie.objects.get(id=pk)
    movie = obj.title
    recommendations = get_recommendations(movie)
    context = {'recommendations':recommendations,'movie':movie}
    return render(request,'base/recommend.html',context)

def add(request, movie):
    pk = request.session.get('watchlist')
    watchlist = models.Watchlist.objects.get(id=pk)
    obj = models.Movie(title=movie,watchlist=watchlist)
    obj.save()
    return redirect('movies',pk)

def signout(request):
    logout(request)
    return redirect('loginPage')