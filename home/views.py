from home.models import Task
from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    context = {'success': False}
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        ins = Task(taskTitle=title,taskDesc=desc)
        print(title,desc)
        ins.save()
        context = {'success': True}
    return render(request,'index.html',context)



def tasks(request):
    allTasks = Task.objects.all()
    # print(allTasks)
    # for item in allTasks:
    #     print("hello")
    #     print(item.taskDesc)
    context = {'tasks': allTasks}

    return render(request,'tasks.html',context)