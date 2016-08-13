from django.shortcuts import render
from django.shortcuts import render, render_to_response


# Create your views here.
def base(req):

    # return HttpResponse("aa")
    return render_to_response('base.html', )

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


def index(req):

    # return HttpResponse("aa")
    return render_to_response('index.html', )


def projects(req):

    # return HttpResponse("aa")
    return render_to_response('projects.html', )


def typo(req):

    # return HttpResponse("aa")
    return render_to_response('typo.html', )
