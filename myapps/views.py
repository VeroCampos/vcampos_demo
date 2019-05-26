from django.shortcuts import render, HttpResponse
from time import localtime, strftime


#datetime_object = datetime.strptime('May 21 2019 10:00AM', '%d %Y %I: %M%p')

# Create your views here.
def index(request):
    
    context = {
        "time": strftime('%A, %m-%d-%Y  %I:%M %p', localtime())
     
    }
    return render(request, 'index.html', context)