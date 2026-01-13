# Register your models here.
from django.contrib import admin
from django.utils import timezone
from . import models
from django.utils.text import slugify

class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'video', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
admin.site.register(models.Banner, BannerAdmin)

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobilenumber', 'age', 'qualification', 'location', 'created_at')
    list_filter = ('qualification', 'created_at')
    search_fields = ('name', 'email', 'mobilenumber', 'location')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
admin.site.register(models.Enquiry, EnquiryAdmin)

class OfferSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
admin.site.register(models.Offer_Section, OfferSectionAdmin)

class TopDestinationsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
admin.site.register(models.Top_Destinations, TopDestinationsAdmin)

class FaqInline(admin.TabularInline):
    model = models.Faq
    fields = ('question', 'answer')
    extra = 1
    min_num = 0
    verbose_name = "FAQ"
    verbose_name_plural = "FAQs"

@admin.register(models.Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'duration', 'location', 'price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'location', 'duration', 'price')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [FaqInline]
    actions = ['duplicate_courses']

    def duplicate_courses(self, request, queryset):
        for original in queryset:
            # store related FAQs
            original_faqs = list(original.faqs.all())

            base_slug = original.slug or slugify(original.title or "")
            new_slug = f"{base_slug}-copy-{int(timezone.now().timestamp())}"

            # duplicate course
            original.pk = None
            original.slug = new_slug
            original.title = f"{original.title} (Copy)"
            original.created_at = timezone.now()
            original.save()

            # duplicate FAQs
            for faq in original_faqs:
                models.Faq.objects.create(
                    course=original,
                    question=faq.question,
                    answer=faq.answer,
                )

        self.message_user(
            request,
            "Selected courses and their FAQs were duplicated successfully."
        )

@admin.register(models.Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('question', 'answer')

admin.site.register(models.Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'image', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'designation', 'message')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)

admin.site.register(models.SuccessStories)
class SuccessStoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'image', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'location', 'message')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)