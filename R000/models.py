from django.db import models

# Create your models here.

class College(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name="department_college")
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Batch(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="batch_department")
    name = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.name

class Semster(models.Model):
    batch = models.ForeignKey(Batch, null=True, blank=True, on_delete=models.CASCADE, related_name="semster_batch")
    name = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.name

class Nationality(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.name

class Studant(models.Model):
    ACCEPT_TYPE= (
        ('قبول عام', 'قبول عم'),
        ('قبول خاص', 'قبول خاص'),
    )
    GENDER= (
        ('زكر', 'زكر'),
        ('انثى', 'انثى'),
    )  
    TOLL_STATUS= (
        ('تم التسديد', 'تم التسديد '),
        ('لم يتم التسديد', 'لم يتم التسديد'),
    )
    CERTIFICATE_TYPE= (
        ('اكاديمي', 'أكاديمي'),
        ('فني', 'فني'),
        ('تجاري', 'تجاري'),
    )  
    RELIGION= (
        ('مسلم', 'مسلم'),
        ('مسيحي', 'مسيحي'),
        ('غير', 'غير'),
    )  
    BLOODTYPE= (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O-', 'O-'),
        ('O+', 'O+'),
        ('AB', 'AB'),
    )  
    semster = models.ForeignKey(Semster, null=True, blank=True, on_delete=models.CASCADE, related_name="studant_semster")
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, related_name="studant_nationality", null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    universitiy_number = models.IntegerField(null=True, blank=True)
    accept_type = models.CharField(max_length=190 , null=True, choices=ACCEPT_TYPE)
    accept_at = models.DateTimeField(auto_now_add=True , null=True)
    toll = models.IntegerField(null=True, blank=True)
    toll_status = models.CharField(max_length=190 , null=True, choices=TOLL_STATUS)

    born_at = models.DateTimeField(null=True, blank=True)
    born_in = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=190 , null=True, choices=GENDER)
    public_number = models.IntegerField(null=True, blank=True)
    religion = models.CharField(max_length=190 , null=True, choices=RELIGION)


    address = models.TextField(max_length=500, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=190 , null=True)

    school_name = models.CharField(max_length=50, null=True, blank=True)
    blood_type = models.CharField(max_length=190 , null=True, choices=BLOODTYPE)
    certificate_type = models.CharField(max_length=190 , null=True, choices=CERTIFICATE_TYPE)
    accept_degeer = models.IntegerField(null=True, blank=True)
    major = models.CharField(max_length=190 , null=True, blank=True)


    def __str__(self):
        return self.name