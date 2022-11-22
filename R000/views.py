from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import College, Department, Program, Batch, Studant
from .forms import StudantForm

from django.contrib.auth.decorators import login_required


# def home(request):
#     context = {}
#     return render(request, 'home/home.html', context)

def about_uni(request):
    context = {}
    return render(request, 'home/about_uni.html', context)

def about_sys(request):
    context = {}
    return render(request, 'home/about_sys.html', context)

def college(request):
    colleges = College.objects.all()
    context = {'colleges':colleges}
    return render(request, 'college/show.html', context)

def department(request ,college_id):
    college = College.objects.get(id=college_id)
    department = Department.objects.filter(college=college)
    context = {'departments':department}
    return render(request, 'department/show.html', context)

def program(request ,department_id):
    department = Department.objects.get(id=department_id)
    program = Program.objects.filter(department=department)
    context = {'programs':program,'department':department}
    return render(request, 'program/show.html', context)

def batch(request ,program_id):
    program = Program.objects.get(id=program_id)
    batch = Batch.objects.filter(program=program)
    context = {'batchs':batch, 'program':program}
    return render(request, 'batch/show.html', context)



def studant(request ,batch_id):
    batch = Batch.objects.get(id=batch_id)
    studant = Studant.objects.filter(batch=batch)
    context = {'studants':studant, 'batch':batch}
    return render(request, 'studant/show.html', context)

def add_studant(request, batch_id):
    batch = Batch.objects.get(id=batch_id)
    context = {
                'batch' : batch,
                'form':StudantForm()
    }
    return render(request, 'studant/add.html', context)

def insert_studant(request, batch_id):
    if request.method == "POST":
        batch = Batch.objects.get(id=batch_id)
        form = StudantForm(request.POST,  request.FILES)
        if form.is_valid():  
            Studant.objects.create(
                batch=batch,
				name=form.cleaned_data['name'],
				universitiy_number=form.cleaned_data['universitiy_number'],
				accept_type=form.cleaned_data['accept_type'],
				toll=form.cleaned_data['toll'],
				toll_status=form.cleaned_data['toll_status'],
				born_in=form.cleaned_data['born_in'],
				born_at=form.cleaned_data['born_at'],
				gender=form.cleaned_data['gender'],
				public_number=form.cleaned_data['public_number'],
				nationality=form.cleaned_data['nationality'],
				religion=form.cleaned_data['religion'],
				address=form.cleaned_data['address'],
				state=form.cleaned_data['state'],
				city=form.cleaned_data['city'],
				phone_number=form.cleaned_data['phone_number'],
				email=form.cleaned_data['email'],
				school_name=form.cleaned_data['school_name'],
				certificate_type=form.cleaned_data['certificate_type'],
				accept_degeer=form.cleaned_data['accept_degeer'],
			)
        else:
            form = StudantForm()
    return redirect("registration:studant", batch_id=batch_id) 

def details(request, studant_id):
    studant = Studant.objects.get(id=studant_id)
    context = {'studant':studant}
    return render(request, 'studant/details.html', context)

def edit_studant(request, batch_id, studant_id):
    batch = Batch.objects.get(pk=batch_id)
    studant = Studant.objects.get(pk=studant_id)
    context = {
                'batch': batch,
                'studant' : studant,
                'form': StudantForm(instance=studant)
    }
    return render(request, 'studant/edit.html', context)

def update_studant(request, batch_id, studant_id):
    if request.method == "POST":
        form = StudantForm(request.POST, instance=Studant.objects.get(pk=studant_id))
        if form.is_valid():  
            form.save()
        else:
            form = StudantForm()
    return redirect("registration:studant", batch_id=batch_id) 