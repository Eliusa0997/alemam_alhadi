from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import College, Department, Batch, Semster, Studant
from .forms import StudantForm, CollegeForm, DepartmentForm, BatchForm, SemsterForm

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
    context = {'departments':department, 'college':college}
    return render(request, 'department/show.html', context)

def batch(request ,department_id):
    department = Department.objects.get(id=department_id)
    batch = Batch.objects.filter(department=department)
    context = {'batchs':batch,'department':department}
    return render(request, 'batch/show.html', context)

def semster(request ,batch_id):
    batch = Batch.objects.get(id=batch_id)
    semster = Semster.objects.filter(batch=batch)
    context = {'semsters':semster, 'batch':batch}
    return render(request, 'semster/show.html', context)



def studant(request ,semster_id):
    semster = Semster.objects.get(id=semster_id)
    studant = Studant.objects.filter(semster=semster)
    context = {'studants':studant, 'semster':semster}
    return render(request, 'studant/show.html', context)

def add_studant(request, semster_id):
    semster = Semster.objects.get(id=semster_id)
    context = {
                'semster' : semster,
                'form':StudantForm()
    }
    return render(request, 'studant/add.html', context)

def insert_studant(request, semster_id):
    if request.method == "POST":
        semster = Semster.objects.get(id=semster_id)
        form = StudantForm(request.POST)
        if form.is_valid():  
            Studant.objects.create(
                semster=semster,
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
    return redirect("registration:studant", semster_id=semster_id) 

def details(request, studant_id):
    studant = Studant.objects.get(id=studant_id)
    context = {'studant':studant}
    return render(request, 'studant/details.html', context)

def edit_studant(request, semster_id, studant_id):
    semster = Semster.objects.get(pk=semster_id)
    studant = Studant.objects.get(pk=studant_id)
    context = {
                'semster': semster,
                'studant' : studant,
                'form': StudantForm(instance=studant)
    }
    return render(request, 'studant/edit.html', context)

def update_studant(request, semster_id, studant_id):
    if request.method == "POST":
        form = StudantForm(request.POST, instance=Studant.objects.get(pk=studant_id))
        if form.is_valid():  
            form.save()
        else:
            form = StudantForm()
    return redirect("registration:studant", semster_id=semster_id) 


def add_college(request):
    context = {          
        'form':CollegeForm()
    }
    return render(request, 'college/add.html', context)

def insert_college(request):
    if request.method == "POST":
        form = CollegeForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = CollegeForm()
    return redirect("registration:college") 

def add_department(request, college_id):
    college = College.objects.get(id=college_id)
    context = {          
        'college':college,
        'form':DepartmentForm(),
    }
    return render(request, 'department/add.html', context)

def insert_department(request, college_id):
    college = College.objects.get(id=college_id)    
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            Department.objects.create(
                college=college,
                name=form.cleaned_data['name'], 
            )           
        else:
            form = DepartmentForm()
    return redirect("registration:department", college_id=college_id)

def add_batch(request, department_id):
    department = Department.objects.get(id=department_id)
    context = {          
        'department':department,
        'form':BatchForm(),
    }
    return render(request, 'batch/add.html', context)

def insert_batch(request, department_id):
    department = Department.objects.get(id=department_id)  
    if request.method == "POST":
        form = BatchForm(request.POST)
        if form.is_valid():
            Batch.objects.create(
                department=department,
                name=form.cleaned_data['name'], 
            )           
        else:
            form = BatchForm()
    return redirect("registration:batch", department_id=department_id)

def add_semster(request, batch_id):
    batch = Batch.objects.get(id=batch_id)
    context = {          
        'batch':batch,
        'form':SemsterForm(),
    }
    return render(request, 'semster/add.html', context)

def insert_semster(request, batch_id):
    batch = Batch.objects.get(id=batch_id)
    if request.method == "POST":
        form = SemsterForm(request.POST)
        if form.is_valid():
            Semster.objects.create(
                batch=batch,
                name=form.cleaned_data['name'], 
            )           
        else:
            form = SemsterForm()
    return redirect("registration:semster", batch_id=batch_id)