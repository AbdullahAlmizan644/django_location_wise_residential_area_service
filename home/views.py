from django.shortcuts import render
from user_auth.models import Rent,Teacher,Tution

# Create your views here.
def index(request):
    all_rent_post=Rent.objects.all()[0:7]
    all_teacher_post=Teacher.objects.all()[0:7]
    return render(request, "main/index.html",{
        "all_rent_post":all_rent_post,
        "all_teacher_post":all_teacher_post,
        }
    )


def rent(request):
    all_rent_post=Rent.objects.all()
    return render(request, "main/rent.html",{
        "all_rent_post":all_rent_post,
    })


def rent_details(request,id):
    post=Rent.objects.filter(id=id).first()
    return render(request, "main/rent_details.html",{
        "post":post,
    })


def about(request):
    return render(request, "main/about.html")


def contact(request):
    return render(request, "main/contact.html")


def teacher(request):
    all_teacher_post=Teacher.objects.all()
    print(all_teacher_post)
    return render(request, "main/teacher.html",{
        "all_teacher_post":all_teacher_post,
    })


def tution(request):
    all_tution_post=Tution.objects.all()
    return render(request, "main/tution.html",{
        "all_tution_post":all_tution_post,
    })


