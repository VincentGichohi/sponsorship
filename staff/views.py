from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
import json
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from .models import *
from credentials.models import *
from student.models import * 
from credentials.forms import *
from student.forms import *


