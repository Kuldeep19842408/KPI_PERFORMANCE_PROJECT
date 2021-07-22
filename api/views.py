from django.http.response import HttpResponse
from django.shortcuts import render
import os


def go(request):
    print("yahaa")
    os.system("python3 parser_project/kpiparser.py")
    return render(request, 'index.html')
