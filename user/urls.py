from django.urls import path
from . import views
urlpatterns = [
  path('',views.home ,name= "home"),
  path('update/',views.update ,name= "update"),
  path('Test/',views.Test ,name= "Test"),
  path('Student_Support/',views.Student_Support ,name= "Student_Support"),
  path('result/',views.result ,name= "result"),
  path('notes_Book/',views.notes_Book ,name= "notes_Book"),
  path('gallary/',views.gallary ,name= "gallary"),
  path('facalty/',views.facalty ,name= "facalty"),
  path('course/',views.course ,name= "course"),
  path('blog/',views.blog ,name= "blog"),
  path('addmission/',views.addmission ,name= "addmission"),
  path('Test_result/',views.Test_result ,name= "Test_result"),
  path('quetion_solvingUI/',views.quetion_solvingUI ,name= "quetion_solvingUI"),
  
  path('gallary/',views.gallary ,name= "gallary"),
  path('facalty/',views.facalty ,name= "facalty"),

]
