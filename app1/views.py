from time import gmtime, strftime
from django.shortcuts import render,HttpResponse
def index(request):
    return HttpResponse("test")

def work(request):
    return render(request, "index.html")





    
def time(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'index.html', context)


