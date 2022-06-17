from django.shortcuts import render,redirect
from .models import Intern,HR
from .forms import InternForm
from django.http import HttpResponseRedirect


# Create your views here.
def delete_intern(request,intern_id):
    intern = Intern.objects.get(pk=intern_id)
    intern.delete()
    return redirect('intern-list')


def edit_intern(request,intern_id):
    intern = Intern.objects.get(pk=intern_id)
    form = InternForm(request.POST or None, instance=intern)
    if form.is_valid():
        form.save()
        return redirect('intern-list')

    return render(request,'intern_register/edit_intern.html',{
        'intern': intern,
        'form' : form
        })


def add_intern(request):
    submitted = False
    if request.method == "POST":
        form = InternForm(request.POST)
        hr_list = HR.objects.all()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_intern?submitted=True')
    else:
        hr_list = HR.objects.all()
        form = InternForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request,'intern_register/add_intern.html',{'form':form,'submitted': submitted, 'hr_list': hr_list})

    # context = {
    #     'hr_list' : hr_list
    # }

    # if request.method == "POST":
    #     name = request.POST.get('i_name')
    #     email = request.POST.get('i_email')
    #     mob_num = request.POST.get('i_phone')
    #     address = request.POST.get('i_address')
    #     job_position = request.POST.get('i_job_position')
    #     stipend = request.POST.get('i_stipend')
    #     join_date = request.POST.get('i_join_date')
    #     description = request.POST.get('i_description')
    #     hr_name = request.POST.get('hr_name')
    #     hr_email = request.POST.get('hr_email')

    #     intern = Intern(
    #         i_name = name,
    #         i_email_address = email,
    #         i_mob_num = mob_num,
    #         i_address = address,
    #         i_job_position = job_position,
    #         i_stipend = stipend,
    #         i_join_date = join_date,
    #         i_description = description,
    #         hr_name = hr_name,
    #         hr_email = hr_email
    #     )
    #     intern.save()
    #     redirect ('intern_list')
    # return render(request,'intern_register/intern_list.html',context)

def home(request):
    return render(request,'intern_register/home.html',{})


def intern_list(request):
    intern = Intern.objects.all()
    context = {
        'intern' : intern,
    }
    return render(request,'intern_register/intern_list.html',context)