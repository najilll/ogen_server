from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from django.views.generic import TemplateView, DetailView, ListView
from .models import Banner, Offer_Section, Testimonials,Top_Destinations,Courses,Faq, SuccessStories
from .form import EnquiryForm

class IndexView(TemplateView):
    template_name = "web/index.html"

    def get_context_data(self):
        context = super().get_context_data()
        banner = Banner.objects.first()
        offer_section = Offer_Section.objects.all()
        top_destinations = Top_Destinations.objects.all()
        courses = Courses.objects.all()
        testimonials = Testimonials.objects.all()
        success_stories = SuccessStories.objects.filter(is_home=True)[:3]
        context['banner'] = banner
        context['offer_section'] = offer_section
        context['top_destinations'] = top_destinations
        context['courses'] = courses
        context['testimonials'] = testimonials
        context['success_stories'] = success_stories
        return context
    
    def post(self, request, *args, **kwargs):
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, self.template_name, self.get_context_data())
        context = self.get_context_data()
        context['form'] = form
        return render(request, self.template_name, context)
    

class AboutView(TemplateView):
    template_name = "web/about.html"

    def get_context_data(self):
        context = super().get_context_data()
        testimonials = Testimonials.objects.all()
        context['testimonials'] = testimonials
        return context


class CourseDetailView(DetailView):
    model = Courses
    template_name = "web/course_detail.html"
    context_object_name = "course"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = Courses.objects.exclude(pk=self.object.pk)
        faq = Faq.objects.filter(course=self.object)
        context['courses'] = course
        context['faq'] = faq
        return context
    

class SuccessStoriesView(ListView):
    model = SuccessStories
    template_name = "web/success_stories.html"
    context_object_name = "success_stories"