from django.shortcuts import render, HttpResponse, redirect
import re
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
import random, string, math
from models import *
from django.core.urlresolvers import reverse
from django.contrib.messages import *

def index(request):
    context = {'courses':Courses.objects.all()}
    return render(request,'Courses/index.html', context)

def create(request):
    errors = Courses.objects.is_valid(request.POST)
    info = Courses.objects.all()

    if len(errors)!= 0:
        for i in errors:
            messages.add_message(request, INFO, errors[i])
    else: Courses.objects.create(course_name=request.POST["name"],desc=request.POST["desc"])


    return redirect('/')


def delete(request, course_id):
    Courses.objects.get(id=course_id).delete()

    return redirect('/')
