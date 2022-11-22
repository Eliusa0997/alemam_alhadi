from django import forms
from .models import Studant

class StudantForm(forms.ModelForm):
  class Meta:
    model = Studant
    fields = ('name', 'universitiy_number', 'toll', 'toll_status', 'accept_type',
              'nationality','born_in', 'born_at', 'gender', 'public_number', 'religion',
              'address', 'state', 'city', 'phone_number', 'email',
              'school_name', 'certificate_type', 'accept_degeer','blood_type',
      )
    widgets = { 
        'name': forms.Textarea(attrs={'rows':1, 'class':'form-control', 'required': 'False', 'placeholder':('')}),
        'universitiy_number': forms.Textarea(attrs={'rows':1, 'class':'form-control', 'placeholder':('')}),
        'blood_type': forms.Select(attrs={'rows':1,'class':'form-control',  'required': 'False'}),        
        'accept_type': forms.Select(attrs={'rows':1,'class':'form-control',  'required': 'False'}),        
        'nationality': forms.Select(attrs={'rows':1,'class':'form-control',  'required': 'False'}),        
        'toll': forms.NumberInput(attrs={'rows':1, 'class':'form-control', 'placeholder':('')}),
        'toll_status': forms.Select(attrs={'rows':1,'class':'form-control',  'required': 'False'}),        
        'born_in': forms.Textarea(attrs={'rows':1, 'class':'form-control', 'placeholder':('')}),
        'born_at': forms.DateInput(attrs={'rows':1, 'class':'form-control', 'placeholder':('')}),
        'gender': forms.Select(attrs={'rows':1,'class':'form-control',  'required': 'False'}),        
        'public_number': forms.NumberInput(attrs={'rows':1, 'class':'form-control', 'placeholder':('')}),
        'religion': forms.Select(attrs={'rows':1,'class':'form-control',  'required': 'False'}),        
        'address': forms.Textarea(attrs={'rows':1, 'class':'form-control', 'placeholder':('')}),
        'state': forms.Textarea(attrs={'rows':1, 'class':'form-control', 'placeholder':('')}),
        'city': forms.Textarea(attrs={'rows':1, 'class':'form-control', 'placeholder':('')}),
        'phone_number': forms.NumberInput(attrs={'rows':1, 'class':'form-control', 'placeholder':('')}),
        'email': forms.EmailInput(attrs={'rows':7, 'class':'form-control', 'placeholder':('')}),    
        'school_name': forms.Textarea(attrs={'rows':1, 'class':'form-control', 'placeholder':('')}),
        'certificate_type': forms.Select(attrs={'rows':1,'class':'form-control',  'required': 'False'}),        
        'accept_degeer': forms.NumberInput(attrs={'rows':1, 'class':'form-control', 'placeholder':('')}),
    }
    labels = {
        'name': ('الإسم'),
        'universitiy_number': ('الرقم الجامعي'),
        'accept_type': ('نوع القبول'),
        'toll': ('الرسوم'),
        'toll_status': ('الحالة المالية'),
        'nationality': ('الجنسية '),
        'born_in': ('مكان الميلاد'),
        'born_at': ('تاريخ الميلاد'),
        'gender': ('النوع'),
        'public_number': ('الرقم الوطني'),
        'religion': ('الديانة'),
        'address': ('العنوان'),
        'state': ('الولاية'),
        'city': ('المديتة'),
        'phone_number': ('رقم الهاتف'),
        'email': ('البريد الإلكتروني'),
        'school_name': ('اسم المدرسة'),
        'certificate_type': ('نوع الشهادة'),
        'accept_degeer': ('نسبة القبول'),
        'blood_type': (' فصيلة الدم '),
    }
