from django.shortcuts import render
from django.shortcuts import render
from .forms import TaskForm
from django.contrib.auth.models import User
from django.http import HttpRequest,HttpResponse

def adhd_info(request):
    return render(request,'base_adhd.html')

def adhd_form(request):
   form = TaskForm()
   return render(request, 'adhd.html', {'form': form})


def track_progress_report(request,id):
    if request.method =='GET':
        print('gaurab')
        return HttpResponse("hi gaurab")
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            selected_values = [
                form.cleaned_data[f'option_{i}']
                for i in range(1, 11)
            ]
            total_sum = sum([int(value) for sublist in selected_values for value in sublist])
            avg = total_sum/10
            print(avg)
            level = ""
            if avg<=3 and avg>1:
                level = "Mild"
            elif avg<=7 and avg>4:
                level = "Moderate"
            elif avg<=10 and avg>8:
                level = "Severe"
            return render(request,'adhd_report.html',{'level':level})
            
    else:
        form = TaskForm()
    return render(request, 'adhd.html', {'form': form})
