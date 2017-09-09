from django.contrib.auth import get_user_model
from django import forms

from nexusite import models
from django.contrib.auth.models import User
from nexusite.models import University, EducationLevel, LengthTimeWorkedEducator

class BaseModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BaseModelForm, self).__init__(*args, **kwargs)
        # add common css classes to all widgets
        for field in iter(self.fields):
            #get current classes from Meta
            classes = self.fields[field].widget.attrs.get("class")
            if classes is not None:
                classes += " form-control"
            else:
                classes = "form-control"
            self.fields[field].widget.attrs.update({
                'class': classes
            })

class SignupForm(forms.Form):
    first_name = forms.CharField(error_messages={'required': 'Please enter your first name'}, max_length=30)
    first_name.widget.attrs['class'] = 'form-control'
    first_name.widget.attrs['placeholder'] = 'First Name'
    last_name = forms.CharField(error_messages={'required': 'Please enter your first name'}, max_length=30)
    last_name.widget.attrs['placeholder'] = 'Last Name'
    email = forms.EmailField(max_length=100, label='E-mail')
    # password1 = forms.PasswordInput(label='sdf')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.password1 = self.cleaned_data['password1']
        user.save()

class FLNameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class ProfileForm_S(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('phone_number', 'zipcode', 'country', 'timezone', 'subject_s', 'grade_s', 'goal_s', 'disability_s', 'travel')
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'timezone': forms.Select(attrs={'class': 'form-control'}),
            'subject_s': forms.TextInput(attrs={'class': 'form-control'}),
            'grade_s': forms.TextInput(attrs={'class': 'form-control'}),
            'goal_s': forms.TextInput(attrs={'class': 'form-control'}),
            'disability_s': forms.RadioSelect,
            'travel': forms.CheckboxSelectMultiple,
        }

class TeacherProfilePersonal(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('phone_number', 'timezone', 'address', 'city', 'state', 'country', 'zipcode', 'range', 'travel', 'university', 'tutoringexpskill', 'academicinstitution' , 'expertfieldexp', 'professionalaward', 'professionalcertification',)
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'timezone': forms.Select(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'range': forms.Select(attrs={'class': 'form-control'}),
            'travel': forms.CheckboxSelectMultiple,
            'university': forms.Select(attrs={'class': 'form-control'}),
            'tutoringexpskill': forms.Textarea(attrs={'class': 'form-control'}),
            'academicinstitution': forms.Textarea(attrs={'class': 'form-control'}),
            'expertfieldexp': forms.Textarea(attrs={'class': 'form-control'}),
            'professionalaward': forms.Textarea(attrs={'class': 'form-control'}),
            'professionalcertification': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CreateStudent_1Form(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('timezone','country','ageverify',)
        widgets = {
            'timezone': forms.Select(attrs={'class':'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'ageverify': forms.RadioSelect
        }

class CreateStudent_2Form(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('servicetype','subject_s','goal_s', 'grade_s', 'disability_s')
        widgets = {
            'subject_s': forms.TextInput(attrs={'class': 'form-control'}),
            'goal_s':  forms.TextInput(attrs={'class': 'form-control'}),
            'grade_s':  forms.TextInput(attrs={'class': 'form-control'}),
            'servicetype': forms.CheckboxSelectMultiple,
            'disability_s': forms.RadioSelect
        }


class CreateStudent_3Form(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('travel',)
        widgets = {
            'travel': forms.CheckboxSelectMultiple
        }

class CreateStudent_4Form(BaseModelForm):
    class Meta:
        model = models.Agreement
        fields = ('agsign', 'agsigndate', 'agaddress',)

        widgets = {
            'agsign': forms.TextInput,
            'agaddress': forms.TextInput,
            'agsigndate': forms.DateInput(attrs={'type':'date'})
        }




class CreateTeacher_1Form(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('timezone','range','travel',)
        widgets = {
            'timezone': forms.Select(attrs={'class':'form-control'}),
            'range': forms.Select(attrs={'class':'form-control'}),
            'travel': forms.CheckboxSelectMultiple
        }

class CreateTeacher_2Form(BaseModelForm):
    class Meta:
        model = models.Profile
        fields = ('university','educationlevel', 'tutoringexpskill', 'expertfieldexp', 'lengthtimeworkededucator', 'professionalaward', 'academicinstitution', 'professionalcertification','userimg')

        widgets = {
            'university': forms.Select,
            'educationlevel': forms.Select,
            'tutoringexpskill': forms.Textarea,
            'expertfieldexp': forms.Textarea,
            'lengthtimeworkededucator': forms.Select,
            'professionalaward': forms.Textarea,
            'academicinstitution': forms.Textarea,
            'professionalcertification': forms.Textarea,
            'userimg': forms.FileInput
        }

class CreateTeacher_3Form(BaseModelForm):
    class Meta:
        model = models.Profile
        fields = ('birthday', 'ssn', 'address', 'city', 'state', 'zipcode')

        widgets = {
            'birthday': forms.DateInput(attrs={'type':'date'}),
            'address': forms.TextInput,
            'state': forms.TextInput,
            'ssn': forms.TextInput,
            'city': forms.TextInput,
            'zipcode': forms.TextInput
        }

class CreateTeacher_4Form(BaseModelForm):
    class Meta:
        model = models.Agreement
        fields = ('agsign', 'agsigndate', 'agaddress',)

        widgets = {
            'agsign': forms.TextInput,
            'agaddress': forms.TextInput,
            'agsigndate': forms.DateInput(attrs={'type':'date'})
        }


class BlogForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = ('btitle', 'bcontent', 'bimg')
        widgets = {
            'btitle': forms.TextInput(attrs={'class': 'form-control'}),
            'bcontent' : forms.Textarea(attrs={'class' : 'form-control'}),
            'bimg': forms.FileInput(attrs={'class': 'form-control'}),
        }

class AcademiRecordForm(forms.ModelForm):
    class Meta:
        model = models.AcademiRecord
        fields = ('atype', 'ascore', 'adate', 'asubject', 'afullscore', 'arank', 'anpart', 'apartrange', 'acomment')
        widgets = {
            'atype': forms.Select(attrs={'class': 'form-control'}),
            'ascore' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'adate': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'asubject': forms.TextInput(attrs={'class': 'form-control'}),
            'afullscore': forms.NumberInput(attrs={'class': 'form-control'}),
            'arank': forms.NumberInput(attrs={'class': 'form-control'}),
            'anpart': forms.NumberInput(attrs={'class': 'form-control'}),
            'apartrange': forms.TextInput(attrs={'class': 'form-control'}),
            'acomment': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PostRequestForm(forms.ModelForm):
    class Meta:
        model = models.PostRequest
        fields = ('preducation', 'probjective')
        widgets = {
            'preducation' : forms.Textarea(attrs={'class': 'form-control','rows':3}),
            'probjective' : forms.Textarea(attrs={'class': 'form-control','rows':3}),
        }

