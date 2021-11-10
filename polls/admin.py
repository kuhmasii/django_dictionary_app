from django.contrib import admin
from . models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = "question_asked pub_date was_published_recently".split()
    list_filter = "pub_date".split()
    # readonly_fields = ("pub_date",)
    search_fields = ["question_asked"]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)


# class ChoiceAdmin(admin.ModelAdmin):
#     list_display = "choice_asked votes".split()
#     list_filter = "votes".split()
# admin.site.register(Choice, ChoiceAdmin)
