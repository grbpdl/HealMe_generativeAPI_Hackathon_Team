from django.contrib import admin
from django.urls import path,include
from .views import adhd_info,adhd_form,track_progress_report

urlpatterns = [
    path('',adhd_info,name="progress"),
    path('form_fillup',adhd_form,name="adhd_form"),
    path('report/<int:id>',track_progress_report,name="progress_report"),
]