from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import Contacts

# Create your views here.

def hello(request):

    if request.POST:
        contact_obj = Contacts()
        contact_obj.first_name = request.POST.get('f_name')
        contact_obj.last_name = request.POST.get('l_name')
        contact_obj.email = request.POST.get('email')
        contact_obj.phone = request.POST.get('phone')
        contact_obj.save()
        
    return render(request,'home.html')

def listContacts(request):
    contacts = Contacts.objects.all()
    return render(request, 'list_contact.html',{'contacts':contacts})

def updateContacts(request,pk):
    contact = Contacts.objects.get(id=pk)
    if request.POST:
        contact.first_name = request.POST.get('f_name')
        contact.last_name = request.POST.get('l_name')
        contact.email = request.POST.get('email')
        contact.phone = request.POST.get('phone')
        contact.save()
        return redirect('list-contacts')
        
    return render(request, 'update_contact.html',{'contact':contact})

def deleteContacts(request,pk):
    contact = Contacts.objects.get(id=pk)
    if request.POST:
        contact.delete()
        return redirect('list-contacts')
    
    return render(request, 'delete_contact.html',{'contact':contact})