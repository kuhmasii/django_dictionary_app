from django.contrib import admin
from . models import Choice, Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = "question_asked pub_date".split()
    list_filter = "pub_date".split()
    # readonly_fields = ("pub_date",)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = "choice_asked votes".split()
    list_filter = "votes".split()


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
