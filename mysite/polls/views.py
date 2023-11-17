from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


# Create your views here.

def index(request):
    # return HttpResponse('Hello anh Thinh')
    myname = 'nguyen truong thinh'
    taisan1 = ['dien thoai', 'may tinh', 'may bay', 'nhieu tien']

    context = {'name': myname, 'taisan': taisan1}
    return render(request, 'polls/index.html', context)


def ham1(request):
    return HttpResponse('</h1>bau troi xanh ngat</h1><p>xin chao tan the gioi</p>')


def viewlist(request):
    list_question = Question.objects.all()
    context = {'dsquest': list_question}
    return render(request, 'polls/question_list.html', context)
