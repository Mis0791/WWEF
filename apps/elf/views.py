from __future__ import unicode_literals
from django.shortcuts import render, redirect
from ..login.models import User
from .models import Elf
from django.contrib.messages import error
from django.contrib import messages

def index(request):
    """
    The queries below set variables equal to not only exclude quotes that are added to the user in sessions favorites but also filter for only the quotes that the user in session has added to their favorites list. These are called in the index.html page where they call on these particular keys from the database and display them on the webpage.
    """
    if "user_id" not in request.session:
        return redirect('/')

    user = User.objects.get(id=request.session['user_id'])
    # allwines = Quote.objects.exclude(quotes__id=request.session['user_id'])
    # otherquotes = Quote.objects.filter(quotes__id=request.session['user_id'])

    context = {
        "users": user,
        # "allwines": allwines,
        # "otherquotes": otherquotes,
    }
    return render(request, 'elf/index.html', context)

def elf(request):
    return render(request, 'elf/elf.html')

# def create(request):
#     """
#     This allows any user that is logged in to create a new quote which then populates up in the quotable quotes list. Newquote is a variable set to create this new wish and post it to the database and newquote.quotes.add(people) is the query that pulls the quotes from the database and displays them under my favorites list on the page. The commented out line below added new quotes to favorites when it needed to go up to the quotable quotes list. If I had an exam that requires new data to immediately go into my list just add the commented line in and add a variable to equal the new created quote. 
#     """
#     result = Quote.objects.validate(request.POST)
#     print result, 'errors'
#     if len(result) > 0:
#         for err in result:   
#             print err
#             messages.error(request, err)
#         return redirect('/quotes') # ends the function and replaces the caller with itself

#     people=User.objects.get(id=request.session['user_id'])
#     Quote.objects.create(
#         quoted_by=request.POST['quoted_by'],
#         message=request.POST['message'],
#         add=people, 
#     )
#     # newquote.quotes.add(people) #  
#     return redirect('/quotes')

# def view(request, number):
#     """
#     This allows the user to click on any users name which will take them to users.html and display that users' number of quotes contributed along with all of their quotes.
#     """
#     if "user_id" not in request.session:
#         return redirect('/')

#     users = User.objects.get(id=request.session['user_id'])

#     context = {
#         "users": users,
#         "user": User.objects.get(id=number),
#         "quote": Quote.objects.filter(add_id=number),
#     }
#     return render(request, 'quotes/user.html', context)

# def add(request, number):
#     """
#     Allows a user to add other users' quotes to their own favorites list.
#     """
#     user = User.objects.get(id=request.session['user_id'])
#     addquote = Quote.objects.get(id=number)
#     addquote.quotes.add(user)
#     return redirect('/quotes')

# def remove(request, number):
#     """
#     Remove is setting up my many to many relationship with removing a particular quote from a users favorites list. 
#     """
#     thisquote = Quote.objects.get(id=number)
#     thisuser = User.objects.get(id=request.session['user_id'])
#     thisquote.quotes.remove(thisuser)
#     return redirect('/quotes')  

def logout(request):
    """
    Flush clears the session once the user logs out preventing from constantly having to refresh the page to clean out the info. Logout redirects the user to the login and reg page.
    """
    request.session.flush()
    return redirect('/elf')

# def dashboard(request):
#     return redirect('/quotes')

