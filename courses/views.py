from django.shortcuts import render
from .models import Lesson, Course

from django.views.generic import ListView, DetailView



class CourseListView(ListView):
    model = Course

class CourseDetailView(DetailView):
    model = Course