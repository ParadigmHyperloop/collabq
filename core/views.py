import difflib

from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import UpdateView
from django.urls import reverse

from core.models import Answer, Question


class Index(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['questions'] = Question.objects.all().order_by('-created')
        return context


class QuestionView(DetailView):
    template_name = 'core/question.html'
    model = Question


class EditAnswerView(UpdateView):
    model = Answer
    fields = ['text']

    def get_success_url(self):
        return reverse('question', args=(self.get_object().question.pk, ))

    def get_context_data(self, **kwargs):
        context = super(EditAnswerView, self).get_context_data(**kwargs)
        d = difflib.Differ()

        answer = self.get_object()
        previous_answer = answer.answerhistory_set.latest('created')
        diff = None
        if previous_answer:
            diff = d.compare(previous_answer.text.splitlines(),
                             answer.text.splitlines())
        context['latest_diff'] = '\n'.join(diff)
        return context


class AnswerHistoryView(DetailView):
    template_name = 'core/answer_history.html'
    model = Answer
