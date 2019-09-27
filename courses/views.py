from django.shortcuts import render
from .models import Lesson, Course

from django.views.generic import ListView, DetailView


class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
