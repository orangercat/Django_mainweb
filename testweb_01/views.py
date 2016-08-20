from django.shortcuts import render,render_to_response
from .models import Project
from .models import New

# Create your views here.
def base(request):
    # return HttpResponse("aa")
    return render(request,'base.html')

def test(req):

    # return HttpResponse("aa")
    return render_to_response('test.html', )


def about(req):

    # return HttpResponse("aa")
    return render_to_response('about.html', )


def contact(req):

    # return HttpResponse("aa")
    return render_to_response('contact.html', )


def gallery(req):

    # return HttpResponse("aa")
    return render_to_response('gallery.html', )


def index(request):
    project_list = Project.objects.all()
    new_list = New.objects.all()
    context = {'project_list' : project_list,'new_list' : new_list}
    return render(request,'index.html', context)


def projects(req):

    # return HttpResponse("aa")
    return render_to_response('projects.html', )


def typo(req):

    # return HttpResponse("aa")
    return render_to_response('typo.html', )
