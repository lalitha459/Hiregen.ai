from django.urls import path
from .import views

urlpatterns  =[
    path('',views.home,name="home"),
    path('jobseeker',views.jobseeker,name="jobseeker"),
    path('jobseeker_classic',views.jobseeker_classic,name="jobseeker_classic"),
    path('resume_finder',views.resume_finder,name="resume_finder"),
    path('resume_finder_classic',views.resume_finder_classic,name="resume_finder_classic"),
    path('download_filtered_file/<str:filename>/', views.download_filtered_file, name='download_filtered_file'),
]