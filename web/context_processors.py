from .models import Top_Destinations, Courses
from .form import EnquiryForm

def main_context(request):
    form = EnquiryForm()
    top_destinations = Top_Destinations.objects.all()
    courses_list = Courses.objects.all()[:5]  # Limit to 5 courses for context
    return {
        'form': form,
        'top_destinations': top_destinations,
        'courses_list': courses_list
    }