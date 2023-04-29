from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import StudentRegistration
from .models import user
from django.contrib import messages
# Create your views here.
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']

            reg=user(name=nm, email=em, password=pw)
            reg.save()
            messages.add_message(request,messages.SUCCESS,"Your Details is Added")
            fm=StudentRegistration()
            
            



    else:
        fm=StudentRegistration()


    details=user.objects.all()
    
    
    return render(request,'addandshow.html',{'form':fm,'details':details})



# deletefunction

def deleteData(request,id):

    if request.method=='POST':
        pi=user.objects.get(pk=id)
        pi.delete()
        messages.add_message(request,messages.INFO," Deleted Successfully")
        return redirect('/')

# updatefunctionGETID

def updateData(request,id):
    if request.method=='POST':
        pi=user.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS," Updated Successfully")
            return redirect('/')

            

    else:
        pi=user.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    
    return render(request,'update.html',{'form':fm})

    