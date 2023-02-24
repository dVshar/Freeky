from django.shortcuts import render

# Create your views here.
def Landing(request):
    return render(request,"Ttrail/index.html")

def About(request):
    return render(request,"Ttrail/about.html")

def Blog(request):
    return render(request,"Ttrail/blog.html")

def Contact(request):
    return render(request,"Ttrail/contact.html")

def Detail(request):
    return render(request,"Ttrail/detail.html")

def Project(request):
    return render(request,"Ttrail/project.html")

def Services(request):
    return render(request,"Ttrail/service.html")

def Team(request):
    return render(request,"Ttrail/team.html")

def Testimonial(request):
    return render(request,"Ttrail/testimonial.html")