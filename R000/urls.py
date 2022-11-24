
from django.urls import include, path   
from .import views

app_name='registration'

urlpatterns = [    


    # path('home/', views.home, name="home"),
    # path('about/university', views.about_uni, name="about-uni"),
    # path('about/system', views.about_sys, name="about-sys"),

    path('', views.college, name="college"),
    # path('admin/', views.college, name="college"),
    # path('college', views.college, name="college"),
    path('department/<int:college_id>', views.department, name="department"),
    path('program/<int:department_id>', views.program, name="program"),
    path('batch/<int:program_id>', views.batch, name="batch"),

    path('studant/<int:batch_id>', views.studant, name="studant"),

    path('studant/<int:studant_id>/<int:batch_id>', views.edit_studant, name="edit-studant"),
    path('update/<int:studant_id>/studant/<int:batch_id>', views.update_studant, name="update-studant"),

    path('add/studant/<int:batch_id>', views.add_studant, name="add-studant"),
    path('insert/studant/<int:batch_id>', views.insert_studant, name="insert-studant"),

    path('studant/details/<int:studant_id>', views.details, name="details"),
]
