# Create web/urls.py and paste the following
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("course/<slug:slug>/", views.CourseDetailView.as_view(), name="course_detail"),
    path("success-stories/", views.SuccessStoriesView.as_view(), name="success_stories"),
]