from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.addhome, name='addhome'),
    path('study_list/', views.study_list, name='study_list'),
    path('study-matrial/',views.studymatrial,name='studymatrial'),
    path('delete_material/<int:id>/', views.delete_material, name='delete_material'),
    path('Allcourses/',views.Allcourses, name='Allcourses'),
    path('Manage_coures/',views.Manage_coures,name='Manage_coures'),
    path('delete_manage/<int:id>',views.delete_manage,name ="delete_manage"),
    path('update_manage/<int:id>',views.update_manage,name ="update_manage"),
    path('Login/',views.Login,name ="Login"),
    path('Profile/',views.Profile,name ="Profile"),
    path("manage_about/",views.manage_about,name="manage_about"),
    path("delete_about/<int:id>/",views.delete_about,name="delete_about"),
    path("manage_stats/",views.manage_stats,name="manage_stats"),
    path("delete_stats/<int:id>/",views.delete_stats,name="delete_stats"),
    
    path('gallery/photos/', views.manage_photos, name='manage_photos'),
    path('gallery/videos/', views.manage_videos, name='manage_videos'),
    path('gallery/albums/', views.manage_albums, name='manage_albums'),
    path('gallery/achievements/', views.manage_achievements, name='manage_achievements'),

    path('add_photo/', views.add_photo, name='add_photo'),
    path('add_video/', views.add_video, name='add_video'),
    path('add_album/', views.add_album, name='add_album'),
    path('add_achievement/', views.add_achievement, name='add_achievement'),  
    
    path('save_photo/', views.save_photo, name='save_photo'),
    path('save_video/', views.save_video, name='save_video'),
    path('save_album/', views.save_album, name='save_album'),
    path('save_achievement/', views.save_achievement, name='save_achievement'),

    path('gallery/photo/delete/<int:pk>/', views.delete_photo, name='delete_photo'),
    path('gallery/video/delete/<int:pk>/', views.delete_video, name='delete_video'),
    path('gallery/album/delete/<int:pk>/', views.delete_album, name='delete_album'),
    path('gallery/achievement/delete/<int:pk>/', views.delete_achievement, name='delete_achievement'),






    path("faculty/",views.faculty,name="faculty"),
    path('add_faculty/',views.add_faculty,name='add_faculty'),
    path("manage_faculty/", views.manage_faculty, name="manage_faculty"),
    path("edit_faculty/<int:id>/", views.edit_faculty, name="edit_faculty"),
    path("delete_faculty/<int:id>/", views.delete_faculty, name="delete_faculty"),
    path("delete_review/<int:id>/",views.delete_review,name="delete_review"),
    path('save-photo/', views.save_photo, name='save_photo'),
    path('save-video/', views.save_video, name='save_video'),
    path('save-album/', views.save_album, name='save_album'),
    path('save-achievement/', views.save_achievement, name='save_achievement'),


]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )