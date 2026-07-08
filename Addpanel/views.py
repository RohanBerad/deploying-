from django.shortcuts import render,redirect, get_object_or_404
from Addpanel import models 
from user import models as us
import os
from django.core.files.storage import default_storage

def Login(req):
    if req.method =='POST':
        email = req.POST.get('email')
        password = req.POST.get('password')

        user = models.Profile.objects.filter(email=email,password=password).first()
        if user:
            req.session['user_email'] = email
            req.session['is_login'] = True
            req.session.set_expiry(1800)
            
            response = redirect('/admin/')
            response.set_cookie('user_email',email,max_age=3600)
            return response
    return render(req,"admin/AdminLogin.html")
def Profile(req):
    if not req.session.get('is_login'):
        return redirect('/admin/Login')    
    data = models.Profile.objects.last()
    if req.method == "POST":
        data = models.Profile(
        heading = req.POST.get('name'),
        email = req.POST.get('email'),
        mobile = req.POST.get('mobile'),
        address = req.POST.get('address'),
        password = req.POST.get('password'),
        facebook = req.POST.get('face'),
        instagram = req.POST.get('insta'),
        youtube = req.POST.get('youtube'),
        whatsapp = req.POST.get('whatsapp')
        )
        data.save()
    return render(req,"admin/adminProfile.html",{"data":data})


def addhome(req):
    if not req.session.get('is_login'):
        return redirect('/admin/Login')
    return render(req,"admin/index.html")

def NotesDownloads(req):
    if not req.session.get('is_login'):
        return redirect('/admin/Login')    
    return render(req,"admin/NotesDownloads.html")

def study_list(request):
    materials = models.Books_notes.objects.all()
    return render(request, "admin/Study_list.html", {
        "materials": materials
    })
def studymatrial(req):

    if req.method == "POST":

        course = models.AllCourse.objects.get(
            id=req.POST.get('course')
        )

        data = models.Books_notes(
            course=course,
            icons=req.POST.get('icons'),
            title=req.POST.get('title'),
            files=req.FILES.get('files')
        )

        data.save()

    courses = models.AllCourse.objects.filter(action="Active")

    return render(
        req,
        'admin/study_Materials.html',
        {
            "courses": courses
        }
    )
def delete_material(req,id):
    data = models.Books_notes.objects.get(id=id)
    if data.files:
        if os.path.isfile(data.files.path):
            os.remove(data.files.path)
    data.delete()
    return redirect('/admin/study_list/')

def Allcourses(req):
    if not req.session.get('is_login'):
        return redirect('/admin/Login')    
    if req.method == "POST":
        data = models.AllCourse(
        header = req.POST.get('header'),
        small_discription = req.POST.get('small_discription'),
        fee = req.POST.get('fee'),
        starting_date = req.POST.get('starting_date'),
        total_time = req.POST.get('total_time'),
        info_fee = req.POST.get('info_fee'),
        info_study = req.POST.get('info_study'),
        )
        data.save()
        return redirect('Allcourses')
    return render(req,"admin/Allcourses.html")       

def Manage_coures(req):
    if not req.session.get('is_login'):
        return redirect('/admin/Login')    
    data = models.AllCourse.objects.filter(action="Active")
    return render(req,'admin/Manage_coures.html',{'data':data})
def update_manage(req,id):
    if not req.session.get('is_login'):
        return redirect('/admin/Login')    
    obj = models.AllCourse.objects.get(id=id)
    if req.method == "POST":
        obj.header = req.POST.get('header')
        obj.small_discription = req.POST.get('small_discription')
        obj.fee = req.POST.get('fee')
        obj.starting_date = req.POST.get('date')
        obj.total_time = req.POST.get('total_time')
        obj.info_head = req.POST.get('info_head')
        obj.info_fee = req.POST.get('info_fee')
        obj.info_study = req.POST.get('info_study')
        obj.info_coures = req.POST.get('info_coures')
        obj.save()
        return redirect('/admin/Manage_coures/')
    return render(req,"admin/update_manage.html",{'obj':obj})     
def delete_manage(req,id):
    data = models.AllCourse.objects.get(id=id)
    data.action = "delete"
    data.save()
    return redirect('/admin/Manage_coures/') 

def manage_stats(request):
    stats=models.AcademyStats.objects.first()
    if request.method=="POST":
        if stats:
            stats.trained_students=request.POST.get("trained_students")
            stats.selected_officers=request.POST.get("selected_officers")
            stats.active_batches=request.POST.get("active_batches")
            stats.years_excellence=request.POST.get("years_excellence")
            stats.save()
        else:
            models.AcademyStats.objects.create(
                trained_students=request.POST.get("trained_students"),
                selected_officers=request.POST.get("selected_officers"),
                active_batches=request.POST.get("active_batches"),
                years_excellence=request.POST.get("years_excellence")
            )
        return redirect("manage_stats")
    return render(request,"admin/manage_stats.html",{
        "stats":models.AcademyStats.objects.all()
    })
def delete_stats(request,id):
    get_object_or_404(models.AcademyStats,id=id).delete()
    return redirect("manage_stats")

def manage_about(request):
    about=models.AboutSection.objects.first()
    if request.method=="POST":
        if about:
            about.title=request.POST.get("title")
            about.description=request.POST.get("description")
            if request.FILES.get("image"):
                about.image=request.FILES.get("image")
            about.save()
        else:
            models.AboutSection.objects.create(
                title=request.POST.get("title"),
                description=request.POST.get("description"),
                image=request.FILES.get("image")
            )
        return redirect("manage_about")
    return render(request,"admin/manage_about.html",{
        "about":models.AboutSection.objects.all()
    })
def delete_about(request,id):
    about=get_object_or_404(models.AboutSection,id=id)
    about.delete()
    return redirect("manage_about")

def add_photo(request):
    return render(request,"admin/gallery_photos.html")

def add_video(request):
    return render(request,"admin/gallery_video.html")

def add_album(request):
    return render(request,"admin/gallery_album.html")

def add_achievement(request):
    return render(request,"admin/gallery_achievement.html")


def save_photo(request):
    if request.method=="POST":
        for file in request.FILES.getlist('image'):
            models.Photo.objects.create(image=file)
    return redirect('manage_photos')


def save_video(request):
    if request.method=="POST":
        for file in request.FILES.getlist('video'):
            us.Video.objects.create(video=file)
    return redirect('manage_videos')


def save_album(request):
    if request.method=="POST":
        paths=[]
        for file in request.FILES.getlist('images'):
            path=default_storage.save(f'event_albums/{file.name}',file)
            paths.append(default_storage.url(path))
        models.EventAlbum.objects.create(
            heading=request.POST.get('heading'),
            date=request.POST.get('date'),
            content=request.POST.get('content'),
            images=paths
        )
    return redirect('manage_albums')


def save_achievement(request):
    if request.method=="POST":
        models.StudentAchievement.objects.create(
            student_name=request.POST.get('student_name'),
            year=request.POST.get('year'),
            exam=request.POST.get('exam'),
            rank_desc=request.POST.get('rank_desc'),
            image=request.FILES.get('image')
        )
    return redirect('manage_achievements')


def manage_photos(request):
    return render(request,"admin/manage_photos.html",{"photos":models.Photo.objects.all()})


def manage_videos(request):
    return render(request,"admin/manage_videos.html",{"videos":us.Video.objects.all()})


def manage_albums(request):
    return render(request,"admin/manage_albums.html",{"albums":models.EventAlbum.objects.all()})


def manage_achievements(request):
    return render(request,"admin/manage_achievements.html",{"achievements":models.StudentAchievement.objects.all()})


def delete_photo(request,pk):
    if request.method=="POST":
        get_object_or_404(models.Photo,id=pk).delete()
    return redirect('manage_photos')


def delete_video(request,pk):
    if request.method=="POST":
        get_object_or_404(us.Video,id=pk).delete()
    return redirect('manage_videos')


def delete_album(request,pk):
    if request.method=="POST":
        get_object_or_404(models.EventAlbum,id=pk).delete()
    return redirect('manage_albums')


def delete_achievement(request,pk):
    if request.method=="POST":
        get_object_or_404(models.StudentAchievement,id=pk).delete()
    return redirect('manage_achievements')


def faculty(request):
    return render(request, "admin/faculty.html")


def add_faculty(request):

    if request.method == "POST":

        faculty = models.Faculty.objects.create(
            name=request.POST.get("name"),
            designation=request.POST.get("designation"),
            description=request.POST.get("description"),
            about_faculty=request.POST.get("about_faculty"),

            image=request.FILES.get("image"),

            years_experience=request.POST.get("years_experience"),
            students_guided=request.POST.get("students_guided"),
        )
    return render(request, "admin/faculty.html")



def manage_faculty(request):
    faculty_list = models.Faculty.objects.all()
    reviews = models.FacultyReview.objects.select_related("faculty")   
    return render(request, "admin/manage_faculty.html", {
        "faculty_list": faculty_list,
        "reviews": reviews
    })


def edit_faculty(request, id):
    faculty = get_object_or_404(models.Faculty, id=id)

    if request.method == "POST":
        faculty.name = request.POST.get("name")
        faculty.designation = request.POST.get("designation")
        faculty.description = request.POST.get("description")
        faculty.about_faculty = request.POST.get("about_faculty")
        faculty.years_experience = request.POST.get("years_experience")
        faculty.students_guided = request.POST.get("students_guided")

        if request.FILES.get("image"):
            faculty.image = request.FILES.get("image")
        faculty.save()
        return redirect("manage_faculty")

    return render(request, "admin/edit_faculty.html", {
        "faculty": faculty,
        "edit_mode": True
})


def delete_faculty(request, id):
    get_object_or_404(models.Faculty, id=id).delete()
    return redirect("manage_faculty")    

def delete_review(request, id):
    review = get_object_or_404(models.FacultyReview, id=id)
    review.delete()
    return redirect("manage_faculty")


