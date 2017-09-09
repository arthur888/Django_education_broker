from django.core.validators import RegexValidator

from django.db import models
from django.contrib.auth.models import User
from timezone_field import TimeZoneField

from multiselectfield import MultiSelectField
from django.db.models.signals import post_save
from django.dispatch import receiver


class University(models.Model):
    uname = models.CharField(max_length=200)
    uname_ch = models.CharField(max_length=200)

    def __str__(self):
        return self.uname

class EducationLevel(models.Model):
    edlname = models.CharField(max_length=200)
    edlname_ch = models.CharField(max_length=200)
    edldescription = models.CharField(max_length=2000)
    edldescription_ch = models.CharField(max_length=2000)

    def __str__(self):
        return self.edlname

class LengthTimeWorkedEducator(models.Model):
    ltwename = models.CharField(max_length=200)
    ltwename_ch = models.CharField(max_length=200)

    def __str__(self):
        return self.ltwename



class Profile(models.Model):
    MyMajor1 = 'Math'
    MyMajor2 = 'Physics'
    MyMajor3 = 'Chemistry'
    MyMajor4 = 'Biology'

    MyMajorAll = (
        (MyMajor1, 'Math'),
        (MyMajor2, 'Physics'),
        (MyMajor3, 'Chemistry'),
        (MyMajor4, 'Biology')
    )

    IAM1 = 'Student'
    IAM2 = 'Teacher'

    IAMAll = (
        (IAM1, 'Student'),
        (IAM2, 'Teacher')
    )


    RANGE1 = '5 miles'
    RANGE2 = '10 miles'
    RANGE3 = '20 miles'
    RANGE4 = '40 miles'
    RANGE5 = 'Phone or Video'
    RANGE = (
        (RANGE1, '5 miles'),
        (RANGE2, '10 miles'),
        (RANGE3, '20 miles'),
        (RANGE4, '40 miles'),
        (RANGE5, 'Phone or Video')
    )

    TRAVEL = (('Student home', 'Student home'),
                   ('Public place', 'Public place'),
                   ('Online Video Conferencing', 'Online Video Conferencing'),
                   ('On the phone via a secure private line', 'On the phone via a secure private line'))

    AGEVERRIFY = (
        ('I am the parent of students', 'I am the parent of students'),
        ('I am a student over the age of 18', 'I am a student over the age of 18'),
        ('I am a student under the age of 18', 'I am a student under the age of 18')
    )

    DISABILITY = (
        (True, 'Yes'),
        (False, 'No')
    )

    SERVICETYPE = (('Course Tutoring', 'Course Tutoring'),
              ('College Counseling', 'College Counseling'),
              ('Standardized Test Preparation', 'Standardized Test Preparation'),
              ('Other', 'Other'))

    user = models.OneToOneField(User, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{1,15}$',
                                     message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=20, validators=[phone_regex], blank=True, null=True)
    birthday = models.DateField(blank=True, default=None, null=True)
    ssn = models.CharField(max_length=50, blank=True, default=None, null=True)
    address = models.CharField(max_length=150, blank=True, default=None, null=True)
    state = models.CharField(max_length=50, blank=True, default=None, null=True)
    city = models.CharField(max_length=50, blank=True, default=None, null=True)
    zipcode = models.CharField('ZIP code', max_length=5, blank=True, default=00000, null=True)
    hrprice = models.FloatField(max_length=20,blank=True, default=None, null=True)
    skill = models.CharField(max_length=30, blank=True, default=None, null=True)
    educationbg = models.CharField(max_length=100, blank=True, default=None, null=True)
    category = models.CharField(max_length=50,choices=MyMajorAll,default=None, null=True)
    timezone = TimeZoneField(default='America/Los_Angeles', blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, default=None, null=True)
    iam = models.CharField(max_length=30, choices=IAMAll, default='Student', null=True)
    money = models.FloatField(blank=True, default=0,null=True)
    subject_s = models.CharField(max_length=300, blank=True, default=None, null=True)
    grade_s = models.CharField(max_length=50, blank=True, default=None, null=True)
    goal_s = models.CharField(max_length=200, blank=True, default=None, null=True)
    disability_s = models.NullBooleanField(choices=DISABILITY ,default=None, null=True, blank=False)
    travel = MultiSelectField(choices=TRAVEL, blank=True, null=True)
    range = models.CharField(max_length=300, choices=RANGE, blank=True, default='5 miles', null=True)
    university = models.ForeignKey(University, blank=True, null=True, default=None)
    educationlevel = models.ForeignKey(EducationLevel, blank=True, null=True, default=None)
    tutoringexpskill = models.CharField(max_length=500, blank=True, default=None, null=True)
    expertfieldexp = models.CharField(max_length=500, blank=True, default=None, null=True)
    lengthtimeworkededucator = models.ForeignKey(LengthTimeWorkedEducator, blank=True, null=True, default=None)
    professionalaward = models.CharField(max_length=500, blank=True, default=None, null=True)
    academicinstitution = models.CharField(max_length=500, blank=True, default=None, null=True)
    professionalcertification = models.CharField(max_length=500, blank=True, default=None, null=True)
    userimg = models.ImageField(upload_to='images/', null=True)
    ageverify = models.CharField(choices=AGEVERRIFY, max_length=50, blank=False, null=True, default=None)
    servicetype = MultiSelectField(choices=SERVICETYPE, default=None, blank=True, null=True)
    completeprofile = models.NullBooleanField(default=False, null=True, blank=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.user.email

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    # class Meta:
    #     db_table = 'auth_profile'


class  Agreement(models.Model):
    agwriter = models.OneToOneField(User, on_delete=models.CASCADE)
    agsign = models.CharField(max_length=30, blank=True, default=None, null=True)
    agsigndate = models.DateField(blank=True, default=None, null=True)
    agservertime = models.DateTimeField(blank=True, default=None, null=True)
    agipaddress = models.CharField(max_length=30, blank=True, default=None, null=True)
    aguseragent = models.CharField(max_length=150, blank=True, default=None, null=True)
    agaddress = models.CharField(max_length=300, blank=True, default=None, null=True)
    agtype = models.CharField(max_length=30, blank=True, default=None, null=True)

    def __str__(self):
        return self.agwriter.get_full_name()

    @receiver(post_save, sender=User)
    def create_user_agreement(sender, instance, created, **kwargs):
        if created:
            Agreement.objects.create(agwriter=instance)

    @receiver(post_save, sender=User)
    def save_user_agreement(sender, instance, **kwargs):
        instance.agreement.save()


class Blog(models.Model):
    bwriter = models.ForeignKey(User, on_delete=models.CASCADE)
    btitle = models.CharField(max_length=100)
    bcontent = models.CharField(max_length=3000)
    bwrittentime = models.DateTimeField()
    bimg = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.btitle


class AcademiRecord(models.Model):
    AcademiType1 = 'School Test'
    AcademiType2 = 'Sport'

    AType = (
        (AcademiType1, 'Student Test'),
        (AcademiType2, 'Sport')
    )

    auser = models.ForeignKey(User, on_delete=models.CASCADE)
    atype = models.CharField(max_length=100, choices=AType )
    ascore = models.FloatField()
    adate = models.DateTimeField()
    asubject = models.CharField(max_length=3000)
    afullscore = models.FloatField()
    arank = models.IntegerField()
    anpart = models.IntegerField()
    apartrange = models.CharField(max_length=3000)
    acomment = models.CharField(max_length=3000)

    def __str__(self):
        return self.auser.get_full_name()





class Category(models.Model):
    cname = models.CharField(max_length=200)
    cname_ch = models.CharField(max_length=200)
    cdescription = models.CharField(max_length=2000)
    cdescription_ch = models.CharField(max_length=2000)

    def __str__(self):
        return self.cname

class UserRating(models.Model):
    urname = models.CharField(max_length=200)
    urname_ch = models.CharField(max_length=200)
    urdescription = models.CharField(max_length=2000)
    urdescription_ch = models.CharField(max_length=2000)

    def __str__(self):
        return self.urname



class ExperienceLevel(models.Model):
    exlname = models.CharField(max_length=200)
    exlname_ch = models.CharField(max_length=200)
    exldescription = models.CharField(max_length=2000)
    exldescription_ch = models.CharField(max_length=2000)

    def __str__(self):
        return self.exlname

class HourlyPrice(models.Model):
    hpname = models.CharField(max_length=200)
    hpname_ch = models.CharField(max_length=200)
    hpdescription = models.CharField(max_length=2000)
    hpdescription_ch = models.CharField(max_length=2000)

    def __str__(self):
        return self.hpname




class PostRequest(models.Model):
    prwriter = models.ForeignKey(User, on_delete=models.CASCADE)
    preducation = models.CharField(max_length=200)
    probjective = models.CharField(max_length=200)
    prcategory = models.ForeignKey(Category)
    pruser_rating = models.ForeignKey(UserRating)
    preducation_level = models.ForeignKey(EducationLevel)
    prexperience_level = models.ForeignKey(ExperienceLevel)
    prprice = models.ForeignKey(HourlyPrice)

    def __str__(self):
        return self.prwriter.username


class PostRespond(models.Model):
    post = models.ForeignKey(PostRequest)
    responseteacher = models.ForeignKey(User)


class Contract(models.Model):
    studentid = models.IntegerField()
    teacherid = models.IntegerField()
    price = models.FloatField()
    makingdate = models.DateField()
    agreeteacher = models.NullBooleanField(default=False, null=True, blank=True)
    complete = models.NullBooleanField(default=False, null=True, blank=True)