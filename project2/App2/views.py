from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    my_dic={"insert_content":"a view from app2"}
    return render(request,"app/index.html",context=my_dic)
