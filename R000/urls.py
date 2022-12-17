
from django.urls import include, path   
from .import views

app_name='registration'

urlpatterns = [    


    path('', views.college, name="college"),
    path('add/college/', views.add_college, name="add-college"),
    path('insert/college/', views.insert_college, name="insert-college"),

    path('department/<int:college_id>', views.department, name="department"),
    path('add/department/<int:college_id>', views.add_department, name="add-department"),
    path('insert/department/<int:college_id>', views.insert_department, name="insert-department"),

    path('batch/<int:department_id>', views.batch, name="batch"),
    path('add/batch/<int:department_id>', views.add_batch, name="add-batch"),
    path('insert/batch/<int:department_id>', views.insert_batch, name="insert-batch"),

    path('semster/<int:batch_id>', views.semster, name="semster"),
    path('add/semster/<int:batch_id>', views.add_semster, name="add-semster"),
    path('insert/semster/<int:batch_id>', views.insert_semster, name="insert-semster"),

    path('studant/<int:semster_id>', views.studant, name="studant"),

    path('studant/<int:studant_id>/<int:semster_id>', views.edit_studant, name="edit-studant"),
    path('update/<int:studant_id>/studant/<int:semster_id>', views.update_studant, name="update-studant"),

    path('add/studant/<int:semster_id>', views.add_studant, name="add-studant"),
    path('insert/studant/<int:semster_id>', views.insert_studant, name="insert-studant"),

    path('studant/details/<int:studant_id>', views.details, name="details"),
]
