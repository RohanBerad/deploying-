from django.shortcuts import render, get_object_or_404,redirect
from Addpanel import models
from user import models as user

def home(request):
    data1 = models.Profile.objects.last()
    about = models.AboutSection.objects.first()
    stats = models.AcademyStats.objects.first()
    obj ={
        "stats":stats,
        "about":about,
        "data1":data1     
    }
    return render(request,"website/pages/index.html",obj)

def update(req):
    data1 = models.Profile.objects.last()
    return render(req,"website/pages/update.html",{'data1':data1})
def Test(req):
    data1 = models.Profile.objects.last()
    return render(req,"website/pages/Test.html",{'data1':data1})
def Student_Support(req):
    data1 = models.Profile.objects.last()
    return render(req,"website/pages/Student_Support.html",{'data1':data1})
def result(req):
    data1 = models.Profile.objects.last()
    return render(req,"website/pages/result.html",{'data1':data1})
def notes_Book(req):
    data1 = models.Profile.objects.last()   
    courses = models.AllCourse.objects.filter( action="Active").prefetch_related('books_notes_set')
    return render( req,"website/pages/notes&Book.html",{"courses": courses,"data1":data1})
def gallary(req):
    data1 = models.Profile.objects.last()
    return render(req,"website/pages/gallary.html",{'data1':data1})
def facalty(req):
    data1 = models.Profile.objects.last()
    return render(req,"website/pages/facalty.html",{'data1':data1})
def course(req):
    data1 = models.Profile.objects.last()
    data = models.AllCourse.objects.filter(action="Active")
    return render(req,"website/pages/course.html",{'data1':data1,"data":data})
def blog(req):
    data1 = models.Profile.objects.last()
    return render(req,"website/pages/blog.html",{'data1':data1})
def addmission(req):
    data1 = models.Profile.objects.last()
    return render(req,"website/pages/addmission.html",{'data1':data1})
def Test_result(req):
    data1 = models.Profile.objects.last()
    return render(req,"website/pages/Test_result.html",{'data1':data1})
def quetion_solvingUI(req):
    data1 = models.Profile.objects.last()
    return render(req,"website/pages/quetion_solvingUI.html",{'data1':data1})

# new 
def gallary(req):
    photos = models.Photo.objects.all()
    videos = user.Video.objects.all()
    albums = models.EventAlbum.objects.all()
    achievements = models.StudentAchievement.objects.all()  
    context = {
        "photos": photos,
        "videos": videos,
        "albums": albums,
        "achievements": achievements
    }
    return render(req,"website/pages/gallary.html",context)
def facalty(req):
    if req.method == "POST":
        faculty_id = req.POST.get("faculty_id")
        student_name = req.POST.get("student_name")
        review = req.POST.get("review")

        faculty = models.Faculty.objects.get(id=faculty_id)
        models.FacultyReview.objects.create(
            faculty=faculty,
            student_name=student_name,
            review=review
        )
        return redirect("facalty")
    faculty_list = models.Faculty.objects.filter(
        is_active=True
    ).prefetch_related(
        "reviews"
    )
    return render(
        req,
        "website/pages/facalty.html",
        {
            "faculty_list": faculty_list
        }
    )


 