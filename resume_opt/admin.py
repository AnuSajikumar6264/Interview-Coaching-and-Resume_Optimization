from django.contrib import admin
from .models import Resume, ResumeFeedback

# Inline model to manage feedback directly within Resume
class ResumeFeedbackInline(admin.TabularInline):
    model = ResumeFeedback
    extra = 1  # Display one empty form by default

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status', 'uploaded_at')
    search_fields = ('name', 'email')
    list_filter = ('status', 'uploaded_at')
    inlines = [ResumeFeedbackInline]  # Link the inline feedback

@admin.register(ResumeFeedback)
class ResumeFeedbackAdmin(admin.ModelAdmin):
    list_display = ('resume', 'comment', 'created_at')
    search_fields = ('resume__name',)
    list_filter = ('created_at',)
