from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.db.models import Count
from .models import Student
from .forms import StudentForm

class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add statistics for the dashboard
        context['total_students'] = Student.objects.count()
        context['course_distribution'] = Student.objects.values('course').annotate(count=Count('id'))
        return context

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Student created successfully! 🎉')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Student'
        context['button_text'] = 'Create Student'
        context['button_icon'] = 'plus'
        return context

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Student updated successfully! ✨')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Student'
        context['button_text'] = 'Update Student'
        context['button_icon'] = 'edit'
        return context

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Student deleted successfully! 🗑️')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Student'
        return context

def home_redirect(request):
    return redirect('student_list')