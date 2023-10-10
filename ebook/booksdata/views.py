from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404
from . models import Books
from . forms import AddBooksForm,ReviewForm, RegisterForm
from user.models import UserOrder


# Create your views here.



# Create a custom decorator to check if the user has both staff and superuser status
def is_staff_and_superuser(user):
    return user.is_staff and user.is_superuser

# Apply the custom decorator to your view

def loginProfile(request):

    if is_staff_and_superuser(request.user):
        return redirect('books')

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
            if is_staff_and_superuser(user):
                login(request, user)
                return redirect('books')
            else:
                messages.error(request,'you are not superuser')

        else:
            messages.error(request,'username or password is incorrect..')

    

    return render(request, 'booksdata/login-register.html')

def logoutProfile(request):
    logout(request)
    messages.error(request,'user was loged out..')
    return redirect('login')




def registerProfile(request):
    page = 'register'
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # WE PUT HOLED THE SAVE METHOD TO MAKE SOME CHANGES IN FORM DATA(USERNAME TO LOWER)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created')

            login(request,user)
            return redirect('books')
        else:
            messages.error(request,'An error has occurred during registration..')
    context = {'page':page, 'form':form}

    return render(request, 'booksdata/login-register.html',context)



@user_passes_test(is_staff_and_superuser, login_url='login')
def displayBooks(request):
    name = request.user.username
    books = Books.objects.all()
    context = {'books':books,'name':name}
    return render(request,'booksdata/display_books.html',context)



@user_passes_test(is_staff_and_superuser, login_url='login')
def viewBook(request,pk):
    book = Books.objects.get(id = pk)
    reviews = book.review_set.all()
    context = {'book':book,'reviews':reviews}

    return render(request, 'booksdata/view_book.html',context)



@user_passes_test(is_staff_and_superuser, login_url='login')
def addBook(request):
    form = AddBooksForm()
    if request.method == 'POST':
        form = AddBooksForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books')
        
    context = {'form':form}

    return render(request, 'booksdata/add_books.html',context)




@user_passes_test(is_staff_and_superuser, login_url='login')
def editBook(request,pk):
    book = Books.objects.get(id = pk)
    form = AddBooksForm(instance=book)
    if request.method == 'POST':
        form = AddBooksForm(request.POST,request.FILES,instance=book)
        if form.is_valid():
            form.save()
            return redirect('view-book',int(pk))
        
    context = {'form':form}

    return render(request, 'booksdata/edit_book.html',context)



@user_passes_test(is_staff_and_superuser, login_url='login')
def deleteBook(request,pk):
    book = Books.objects.get(id=pk)
    book.delete()
    return redirect('books')  # Redirect to a course list view
    # return render(request, 'booksdata/delete_book.html', {'book': book})





@user_passes_test(is_staff_and_superuser, login_url='login')
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
            return redirect('view-book',int(pk))  # Redirect to a course list view
    else:
        form = ReviewForm()
    return render(request, 'booksdata/add_review.html', {'form': form})




@user_passes_test(is_staff_and_superuser, login_url='login')
def editReview(request, pk, review_id):
    book = Books.objects.get(id=pk)
    review = book.review_set.get(id=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST,instance=review)
        if form.is_valid():
            form.save()
            return redirect('view-book',int(pk))  # Redirect to a course list view
    else:
        form = ReviewForm(instance=review)
    return render(request, 'booksdata/edit_review.html', {'form': form})



@user_passes_test(is_staff_and_superuser, login_url='login')
def deleteReview(request, pk, review_id):
    book = Books.objects.get(id=pk)
    review = book.review_set.get(id=review_id)
    review.delete()
    return redirect('view-book',int(pk))  # Redirect to a course list view
    # return render(request, 'booksdata/delete_review.html', {'review': review})


# views.py

@user_passes_test(is_staff_and_superuser, login_url='login')
def admin_messages(request):
    messages = UserOrder.objects.all()
    
    # if request.method == 'POST':
    #     message_id = request.POST.get('message_id')
    #     action = request.POST.get('action')
    #     if message_id and action in ['approve', 'reject']:
    #         message = UserOrder.objects.get(id=message_id)
    #         if action == 'approve':
    #             message.is_approved = True


    #         elif action == 'reject':
    #             message.is_approved = False
    #         # else:
    #         #     message.delete
    #         #     return redirect('admin_messages')
                
    #         message.save()

    return render(request, 'booksdata/inbox.html', {'messages': messages})


# views.py
@user_passes_test(is_staff_and_superuser, login_url='login')
def approve_message(request, message_id):
    message = get_object_or_404(UserOrder, id=message_id)
    message.is_approved = True
    message.save()
    return redirect('admin_messages')


@user_passes_test(is_staff_and_superuser, login_url='login')
def reject_message(request, message_id):
    message = get_object_or_404(UserOrder, id=message_id)
    message.is_approved = False
    message.save()
    return redirect('admin_messages')


@user_passes_test(is_staff_and_superuser, login_url='login')
def delete_message(request, message_id):
    message = get_object_or_404(UserOrder, id=message_id)
    message.delete()
    return redirect('admin_messages')