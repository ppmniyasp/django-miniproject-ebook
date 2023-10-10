from django.shortcuts import render, redirect
from booksdata.models import Books
from booksdata. forms import ReviewForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserOrder
from booksdata.models import Books
from .forms import UserMessageForm,UserRegisterForm

# Create your views here.


def loginProfile(request):

    if request.user.is_authenticated:
        return redirect('user-books')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)

        except:
            messages.error(request,'username does not exist..')


        # this will check username match the password if it is it return a instance else none
        user = authenticate(request, username=username, password=password )

        if user is not None:
            login(request, user)
            return redirect('user-books')
        else:
            messages.error(request,'username or password is incorrect..')
    return render(request, 'user/login-register.html')

def logoutProfile(request):
    logout(request)
    messages.error(request,'user was loged out..')
    return redirect('user-login')




def registerProfile(request):
    page = 'register'
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # WE PUT HOLED THE SAVE METHOD TO MAKE SOME CHANGES IN FORM DATA(USERNAME TO LOWER)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created')

            login(request,user)
            return redirect('user-books')
        else:
            messages.error(request,'An error has occurred during registration..')
    context = {'page':page, 'form':form}

    return render(request, 'user/login-register.html',context)




def displayBooks(request):
    name = request.user.username
    books = Books.objects.all()
    context = {'books':books,'name':name}
    return render(request,'user/display_books.html',context)


def viewBook(request,pk):
    book = Books.objects.get(id = pk)
    reviews = book.review_set.all()
    context = {'book':book,'reviews':reviews}

    return render(request, 'user/view_book.html',context)


@login_required(login_url='user-login')
def addReview(request,pk):
    name = request.user.username
    book = Books.objects.get(id=pk)
    # reviw = book.type_set.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Associate the review with the task
            review = form.save(commit=False)
            review.book = book
            review.title = name

            form.save()
            return redirect('user-view-book',int(pk))  # Redirect to a course list view
    else:
        form = ReviewForm()
    return render(request, 'user/add_review.html', {'form': form})



@login_required(login_url='user-login')
def send_message(request, pk):
    book = Books.objects.get(id = pk)
    book_id = pk

    if request.method == 'POST':
        form = UserMessageForm(request.POST)
        if form.is_valid():
            user_message = form.save(commit=False)
            user_message.user = request.user
            user_message.book_name = book
            user_message.save()
            return redirect('message_sent')
    else:
        form = UserMessageForm()

    return render(request, 'user/send_message.html', {'form': form,'book_id':book_id})

@login_required(login_url='user-login')
def message_status(request):
    user_messages = UserOrder.objects.filter(user=request.user)
    return render(request, 'user/message_sent.html', {'user_messages': user_messages,})

@login_required(login_url='user-login')
def delete_order(request, pk):
    order = UserOrder.objects.get(id = pk)
    order.delete()
    return redirect('message_sent')
