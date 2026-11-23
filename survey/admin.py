from django.contrib import admin
from .models import SurveyResponse


@admin.register(SurveyResponse)
class SurveyResponseAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'email',
        'technology',
        'rating',
        'submitted_at',
    ]

    search_fields = [
        'name',
        'email',
    ]

    list_filter = [
        'technology',
        'rating',
    ]