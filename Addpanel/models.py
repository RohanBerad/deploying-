from django.db import models


    
class EventAlbum(models.Model):
    heading = models.CharField(max_length=255)
    date = models.DateField()
    content = models.TextField()
    images = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Photo(models.Model):
    image = models.ImageField(upload_to='gallery/photos/')
    desc = models.CharField(max_length=255, default='') 
    is_cover = models.BooleanField(default=False)


     
class AllCourse(models.Model):
    header = models.CharField(max_length = 100)
    small_discription = models.CharField(max_length = 500)
    fee = models.IntegerField()
    starting_date = models.DateField(auto_now_add = True)
    total_time = models.IntegerField()
    # info page
    info_fee =models.CharField(max_length=500)
    info_study =models.CharField(max_length=500)
    action = models.CharField(max_length = 100,default="active")
    

class Profile(models.Model):
    heading = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    password = models.CharField(max_length=128)
    facebook = models.CharField(max_length = 100)
    instagram = models.CharField(max_length = 100)
    youtube = models.CharField(max_length = 100)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)

class Books_notes(models.Model):
    course = models.ForeignKey(
        AllCourse,
        on_delete=models.CASCADE
    )
   
    icons = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    files = models.FileField(upload_to='media')


class AcademyStats(models.Model):
    trained_students = models.IntegerField(default=0)
    selected_officers = models.IntegerField(default=0)
    active_batches = models.IntegerField(default=0)
    years_excellence = models.IntegerField(default=0)
class AboutSection(models.Model):
    image = models.ImageField(upload_to="about/")
    title = models.CharField(max_length=200)
    description = models.TextField()




class StudentAchievement(models.Model):
    student_name = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    exam = models.CharField(max_length=255)
    rank_desc = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery/achievements/')
    created_at = models.DateTimeField(auto_now_add=True)    

class Faculty(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=255)
    description = models.TextField()
    about_faculty = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="faculty/")
    years_experience = models.CharField(max_length=50)
    students_guided = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "Addpanel_faculty"
class FacultyReview(models.Model):
    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    student_name = models.CharField(max_length=150)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "Addpanel_faculty_reviews"

