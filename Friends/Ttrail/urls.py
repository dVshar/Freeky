from django.urls import path,include
from .views import *

urlpatterns = [
    path('',Landing,name="landing"),
    path('about/',About,name="About"),
    path('blog/',Blog,name="Blog"),
    path('contact/',Contact,name="Contact"),
    path('detail/',Detail,name="Detail"),
    path('project/',Project,name="Project"),
    path('services/',Services,name="Services"),
    path('team/',Team,name="Team"),
    path('testimonial/',Testimonial,name="Testimonial")
]