from django import forms
from django.contrib.auth.models import User
from . import models

#for admin
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']


#for student related form
class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
class StudentExtraForm(forms.ModelForm):
    class Meta:
        model=models.StudentExtra
        fields=['roll','cl','mobile','status' ,'cnic', 'address','father','fcnic']

#for teacher related form
class TeacherUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']        
class TeacherExtraForm(forms.ModelForm):
    class Meta:
        model=models.TeacherExtra
        fields=['salary','mobile','status','class_incharge','cnic','father','address']
        
#for Attendance related form
presence_choices=(('Present','Present'),('Absent','Absent'))
class AttendanceForm(forms.Form):
    present_status=forms.ChoiceField( choices=presence_choices)
    date=forms.DateField()

MONTH_CHOICES = [
    ('', 'Nil'),
    ('1', 'January'),
    ('2', 'February'),
    ('3', 'March'),
    ('4', 'April'),
    ('5', 'May'),
    ('6', 'June'),
    ('7', 'July'),
    ('8', 'August'),
    ('9', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December'),
]

class AskDateForm(forms.Form):
    #date=forms.DateField()
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'placeholder': 'Enter date mm/dd/yyyy'}), required=False)
    month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    year = forms.IntegerField(label='Year', required=False)
    roll = forms.CharField(label='Roll', max_length=10, required=False)

class StudentAttendanceForm(forms.Form):
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'placeholder': 'Enter date mm/dd/yyyy'}), required=False)
    month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    year = forms.IntegerField(label='Year', required=False)


#for notice related form
class NoticeForm(forms.ModelForm):
    class Meta:
        model=models.Notice
        fields='__all__'

#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))


class FeeCollectionForm(forms.Form):
    fee_amount = forms.IntegerField(label='Fee Amount', widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter Date mm/dd/yyyy'}))