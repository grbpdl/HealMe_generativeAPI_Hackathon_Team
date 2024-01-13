from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import TaskForm
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from .models import ADHDProgress


def adhd_info(request):
    return render(request, 'base_adhd.html')


def adhd_form(request):
    form = TaskForm()
    return render(request, 'adhd.html', {'form': form})

def track_progress_report(request, id):
    form = TaskForm() 

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            selected_values = [
                form.cleaned_data[f'option{i}']
                for i in range(1, 11)
            ]
            print('valid cha')
            total_sum = sum([int(value) for sublist in selected_values for value in sublist])
            avg = total_sum / 10
            print(avg)
            level = ""
            if avg <=1:
                level = "Normal"
            elif avg <2 and avg >= 1:
                level = "Mild"
            elif avg <3 and avg >=2:
                level = "Moderate"
            elif avg<4 and avg >=3:
                level = "Severe"
            elif avg<=5 and avg>=4:
                level = "Very Severe"
            return render(request, 'adhd_report.html', {'level': level})
        else:
            messages.error(request, 'You missed some questions!')

    return render(request, 'adhd.html', {'form': form})

def progress_chart(request):
    return render(request, 'charts.html')