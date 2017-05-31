from django.contrib import admin

from core.models import Answer, AnswerHistory, Question

admin.site.register(Answer)
admin.site.register(AnswerHistory)
admin.site.register(Question)
