from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.utils import timezone


from nexusite import models

from nexusite import forms

# Create your views here.
from nexusite.forms import ProfileForm_S, BlogForm, UserForm, PostRequestForm, AcademiRecordForm, CreateTeacher_1Form, CreateTeacher_2Form, CreateTeacher_3Form, CreateTeacher_4Form ,FLNameForm, CreateStudent_1Form, CreateStudent_2Form, CreateStudent_3Form, CreateStudent_4Form, TeacherProfilePersonal
from nexusite.models import Category, ExperienceLevel, EducationLevel, HourlyPrice, UserRating

recent_three = models.Blog.objects.order_by('bwrittentime')[:3]

def index(request):
    return render(request, "index.html", {
        'title': 'NexustarSite',
    })


@login_required
def checkuser(request):

    ad = models.Profile.objects.get(user=request.user)
    if ad.completeprofile:
        if ad.iam == 'Teacher':
            request.session['nowiam'] = 1
        elif ad.iam == 'Student':
            request.session['nowiam'] = 0
        return HttpResponseRedirect('/blog/')
    else:
        return render(request, "selectuser.html", {
                              'title': 'select user',
                          })

@login_required
def createstudent_1(request):
    if request.method == 'POST':
        savedata = CreateStudent_1Form(request.POST, instance=request.user.profile)
        if savedata.is_valid():
            obj = savedata.save(commit=False)
            obj.user = request.user
            obj.iam = 'Student'
            obj.save()
            return HttpResponseRedirect('/createstudent_2/')
    else:
        cs_1form = CreateStudent_1Form(instance=request.user.profile)
        return render(request, "createstudent_1.html", {
                              'title': 'create student step1',
                               'cs_1form': cs_1form
                          })

@login_required
def createstudent_2(request):
    if request.method == 'POST':
        savedata = CreateStudent_2Form(request.POST, instance=request.user.profile)
        if savedata.is_valid():
            obj = savedata.save(commit=False)
            obj.save()
            return HttpResponseRedirect('/createstudent_3/')
    else:
        cs_2form = CreateStudent_2Form(instance=request.user.profile)
        return render(request, "createstudent_2.html", {
                              'title': 'create student step2',
                               'cs_2form': cs_2form
                          })

@login_required
def createstudent_3(request):
    if request.method == 'POST':
        savedata = CreateStudent_3Form(request.POST, instance=request.user.profile)
        if savedata.is_valid():
            obj = savedata.save(commit=False)
            obj.save()
            return HttpResponseRedirect('/createstudent_4/')
    else:
        cs_3form = CreateStudent_3Form(instance=request.user.profile)
        return render(request, "createstudent_3.html", {
                              'title': 'create student step3',
                               'cs_3form': cs_3form
                          })


@login_required
def createstudent_4(request):
    if request.method == 'POST':
        savedata = CreateStudent_4Form(request.POST, instance=request.user.agreement)
        if savedata.is_valid():
            obj = savedata.save(commit=False)
            # obj.user = request.user
            obj.save()
            t = models.Profile.objects.get(user=request.user)
            t.completeprofile = True  # change field
            t.save()  # this will update only

            return HttpResponseRedirect('/')
    else:
        cs_4form = CreateStudent_4Form(instance=request.user.agreement)
        return render(request, "createstudent_4.html", {
                              'title': 'create student step4',
                                'cs_4form': cs_4form,
                          })



@login_required
def createteacher_1(request):
    if request.method == 'POST':
        savedata = CreateTeacher_1Form(request.POST, instance=request.user.profile)
        if savedata.is_valid():
            obj = savedata.save(commit=False)
            obj.user = request.user
            obj.iam = 'Teacher'
            obj.save()
            return HttpResponseRedirect('/createteacher_2/')
    else:
        ct_1form = CreateTeacher_1Form(instance=request.user.profile)
        return render(request, "createteacher_1.html", {
                              'title': 'create teacher step1',
                                'ct_1form': ct_1form
                          })

@login_required
def createteacher_2(request):
    if request.method == 'POST':
        savedata = CreateTeacher_2Form(request.POST, request.FILES, instance=request.user.profile)
        if savedata.is_valid():
            obj = savedata.save(commit=False)
            # obj.user = request.user
            obj.save()
            return HttpResponseRedirect('/createteacher_3/')
    else:
        ct_2form = CreateTeacher_2Form(instance=request.user.profile)
        return render(request, "createteacher_2.html", {
                              'title': 'create teacher step2',
                                'ct_2form': ct_2form
                          })

@login_required
def createteacher_3(request):
    if request.method == 'POST':
        flnameform = forms.FLNameForm(request.POST, instance=request.user)
        savedata = CreateTeacher_3Form(request.POST, instance=request.user.profile)
        if flnameform.is_valid() and savedata.is_valid():
            flnameform.save()
            obj = savedata.save(commit=False)
            # obj.user = request.user
            obj.save()
            return HttpResponseRedirect('/createteacher_4/')
    else:
        flnameform = forms.FLNameForm(instance=request.user)
        ct_3form = CreateTeacher_3Form(instance=request.user.profile)
        return render(request, "createteacher_3.html", {
                              'title': 'create teacher step3',
                                'ct_3form': ct_3form,
                                'ct_3form_flname': flnameform
                          })


@login_required
def createteacher_4(request):
    if request.method == 'POST':
        savedata = CreateTeacher_4Form(request.POST, instance=request.user.agreement)
        if savedata.is_valid():
            obj = savedata.save(commit=False)
            # obj.user = request.user
            obj.save()

            t = models.Profile.objects.get(user=request.user)
            t.completeprofile = True  # change field
            t.save()  # this will update only
            # checkuser(request)
            return HttpResponseRedirect('/')
    else:
        ct_4form = CreateTeacher_4Form(instance=request.user.agreement)
        return render(request, "createteacher_4.html", {
            'title': 'create teacher step4',
            'ct_4form': ct_4form,
        })


@login_required
def view_profilet_detail(request, tid):
    if request.method == "POST":
        st = ""
    else:
        teacherdata = models.Profile.objects.filter(user_id=tid)
        return render(request, "detailprofilet.html", {
            'title': 'Detail Tutor Profile',
            'tprofile': teacherdata,
            'nowiam': request.session['nowiam']
        })



@login_required
def view_backgroundcheck(request):
    if request.method == 'POST':
        flnameform = forms.FLNameForm(request.POST, instance=request.user)
        savedata = CreateTeacher_3Form(request.POST, instance=request.user.profile)
        if flnameform.is_valid() and savedata.is_valid():
            flnameform.save()
            obj = savedata.save(commit=False)
            # obj.user = request.user
            obj.save()
            return HttpResponseRedirect('/backgroundcheck/')
    else:
        flnameform = forms.FLNameForm(instance=request.user)
        bkchform = CreateTeacher_3Form(instance=request.user.profile)
        return render(request, "backgroundcheck.html", {
          'title': 'create teacher step3',
            'bkchform': bkchform,
            'bkchform_flname': flnameform,
            'nowiam': request.session['nowiam']
        })


@login_required
def view_teacherprofile(request):

    nowuser = request.user
    if request.method == 'POST':
        tuser_form = UserForm(request.POST, instance=request.user)
        tprofile_form = TeacherProfilePersonal(request.POST, instance=request.user.profile)
        if tuser_form.is_valid() and tprofile_form.is_valid():
            tuser_form.save()
            tprofile_form.save()
            return redirect('/teacherinfo/')

    else:
        tuser_form = UserForm(instance=nowuser)
        tprofile_form = TeacherProfilePersonal(instance=nowuser.profile)

        return render(request, "teacherinfo.html", {
          'title': 'teacher_profile',
          'tform_user': tuser_form,
          'tform_profile':tprofile_form,
            'nowiam': request.session['nowiam']
        })

@login_required
def view_userprofile(request):
    # user_profile = models.UserProfile.get_user()  objects.get(user_id = request.user.id);

    nowuser = request.user
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm_S(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('/userinfo/')

    else:
        user_form = UserForm(instance=nowuser)
        profile_form = ProfileForm_S(instance=nowuser.profile)

        return render(request, "userinfo.html", {
          'title': 'user_profile',
          'form_user': user_form,
          'form_profile':profile_form,
            'nowiam': request.session['nowiam']
        })



@login_required
def view_blogs(request):
    blogs = models.Blog.objects.all().order_by('bwrittentime').reverse()
    return render(request, "blog_show.html", {
        'title': 'blog',
        'blogs' : blogs,
        'recentblogs': recent_three,
        'nowiam': request.session['nowiam']
    })

@login_required
def view_blog_detail(request, blog_id):
    blogdata = models.Blog.objects.get(pk = blog_id)
    return render(request, "blog_show_detail.html", {
        'title':'blog_detail',
        'blog_data' : blogdata,
        'recentblogs': recent_three,
        'nowiam': request.session['nowiam']
    })


@login_required
def view_myblogs(request):

    print(recent_three)
    myblogs = models.Blog.objects.filter(bwriter = request.user).order_by('bwrittentime').reverse()
    return render(request, "blog_show.html", {
        'title': 'blog',
        'blogs': myblogs,
        'recentblogs': recent_three,
        'nowiam': request.session['nowiam']
    })


@login_required
def crete_blog(request):
    if request.method== 'POST':
        saveblogdata = BlogForm(request.POST, request.FILES)
        if saveblogdata.is_valid():
            obj = saveblogdata.save(commit=False)
            obj.bwriter = request.user
            obj.bwrittentime = timezone.now()
            obj.save()
            return HttpResponseRedirect('/blog/')
    else:
        blogform = forms.BlogForm()
        return render(request, "blog_create.html", {
            'title': 'blog edit',
            'blogform' : blogform,
            'recentblogs': recent_three,
            'nowiam': request.session['nowiam']
        })


@login_required
def crete_academirecord(request):
    if request.method== 'POST':
        saveblogdata = AcademiRecordForm(request.POST)
        if saveblogdata.is_valid():
            obj = saveblogdata.save(commit=False)
            obj.auser = request.user
            obj.save()
            return HttpResponseRedirect('/academirecord/')
    else:
        existingacrecord = models.AcademiRecord.objects.filter(auser=request.user)
        academirecordform = forms.AcademiRecordForm()
        return render(request, "academirecord.html", {
            'title': 'academic record create',
            'academirecordform' : academirecordform,
            'existingacrecord': existingacrecord,
            'nowiam': request.session['nowiam']
        })


@login_required
def view_clientsrecommendation(request):
    if request.method=='POST':
        astr = request.POST['postid']
        existing = models.PostRespond.objects.filter(post_id=astr, responseteacher=request.user)
        if existing:
            return HttpResponse("exist")
        else:
            postrespond = models.PostRespond()
            postrespond.post_id = astr
            postrespond.responseteacher = request.user
            postrespond.save()
            return HttpResponse("ok")

    else:
        post_requests = models.PostRequest.objects.all()
        return render(request, "clientsrecommendation.html", {
            'existingpost': post_requests,
            'title': 'Post request',
            'nowiam': request.session['nowiam']
        })


@login_required
def view_respondst(request):
    if request.method == 'POST':
        astr = request.POST['postid']
        # existing = models.PostRespond.objects.filter(post_id=astr, responseteacher=request.user)
        # if existing:
        #     return HttpResponse("exist")
        # else:
        #     postrespond = models.PostRespond()
        #     postrespond.post_id = astr
        #     postrespond.responseteacher = request.user
        #     postrespond.save()
        #     return HttpResponse("ok")

    else:
        postid = request.GET['postid']
        postrespond = models.PostRespond.objects.filter(post_id=postid)
        return render(request, "viewrespondst.html", {
            'responddata': postrespond,
            'title': 'Post respond',
            'nowiam': request.session['nowiam']
        })


@login_required
def post_request_s(request):
    if request.method=='POST':
        savepostdata = PostRequestForm(request.POST)
        if savepostdata.is_valid():
            postobj = savepostdata.save(commit=False)
            postobj.prcategory = Category.objects.filter(cname=request.POST.get('category')).first()
            postobj.pruser_rating = UserRating.objects.filter(urname=request.POST.get('userrating')).first()
            postobj.preducation_level = EducationLevel.objects.filter(edlname=request.POST.get('educationlevel')).first()
            postobj.prexperience_level = ExperienceLevel.objects.filter(exlname=request.POST.get('experiencelevel')).first()
            postobj.prprice = HourlyPrice.objects.filter(hpname=request.POST.get('hprice')).first()
            postobj.prwriter = request.user
            postobj.save()
            return HttpResponseRedirect('/postrequestst/')

    else:
        existingpost = models.PostRequest.objects.all()
        postform = forms.PostRequestForm()
        categories = models.Category.objects.all()
        educationlevel = models.EducationLevel.objects.all()
        experiencelevel = models.ExperienceLevel.objects.all()
        userrating = models.UserRating.objects.all()
        hprice = models.HourlyPrice.objects.all()

        return render(request, "post_request_s.html", {
            'existingpost': existingpost,
            'title': 'Post request',
            'postform': postform,
            'categories': categories,
            'educationlevels': educationlevel,
            'experiencelevels': experiencelevel,
            'userratings': userrating,
            'hprices': hprice,
            'nowiam': request.session['nowiam']
        })

@login_required
def edit_profile(request):
    if request.method=='POST':
        temp = ""
    else:
        user_form = forms.UserForm()
        edit_form = forms.ProfileForm()
        return render(request, "edit_profile.html", {
            'title': 'Edit Profile',
            'edit_form': user_form,
            'user_form': edit_form,
            'nowiam': request.session['nowiam']
        })




@login_required
def view_contact(request):
    if request.method=='POST':
        nowuser = request.user
    else:
        return render(request, "contactus.html", {
            'title': 'contact us',
            'nowiam': request.session['nowiam']
        })


@login_required
def view_booking(request, tid):
    if request.method=='POST':
        sdf= "sdf"
    else:
        teacher = models.User.objects.get(id=tid)

        student = models.User.objects.get(id=request.user.id)
        return render(request, "makecontract.html", {
            'title': 'Edit Profile',
            'teacher':  teacher,
            'student': student,
            'nowiam': request.session['nowiam']
        })
