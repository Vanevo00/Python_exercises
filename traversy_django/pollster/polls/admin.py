from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3

class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [(None, {'fields': ['question_text']}), ('Date information', {'fields': ['publish _date'], 'classes': ['collapse']}),]
  inlines = [ChoiceInline ]

# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.register(Question, QuestionAdmin)
