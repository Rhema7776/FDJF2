from tkinter import dialog
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ApplicantForm
from .models import Applicant

# Create your views here.
# def update_applicant(request, applicant_id):
#     applicant = Applicant.objects.get(pk=applicant_id)
#     return render(request, 'update_applicant.html',
#      {'applicant': applicant})

# def list_applicants(request, applicant_id):
#     applicant = Applicant.objects.get(pk=applicant_id)
#     return render(request, 'list_applicants.html',
#      {'applicant_list': applicant_list})
def home(request):
    return render(request, 'base.html')



def register(request):
    submitted=False
    if request.method=="POST":
        form=ApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register?submitted=True')
        else:
            if 'submitted' in request.GET:
                raise form.validationError("This is a duplicate")
    else:
        form=ApplicantForm
        if 'submitted' in request.GET:
            submitted=True

    form=ApplicantForm
    return render(request, 'register.html',{'form':form, 'submitted':submitted})



def about(request):
    return render(request, 'about.html')


