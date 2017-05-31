import uuid

from django.db import models


class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Question(BaseModel):
    text = models.CharField(max_length=2048)

    def __str__(self):
        return self.text


class AnswerHistory(BaseModel):
    answer = models.ForeignKey('core.Answer', on_delete=models.CASCADE)
    text = models.TextField()


class Answer(BaseModel):
    text = models.TextField()
    question = models.OneToOneField('core.Question', on_delete=models.CASCADE)

    def __str__(self):
        return "Answer for {}".format(self.question)

    def save(self, *args, **kwargs):
        self._capture_history()
        super(Answer, self).save(*args, **kwargs)

    def _capture_history(self):
        try:
            previous_self = Answer.objects.get(pk=self.pk)
        except Answer.DoesNotExist:
            pass
        else:
            previous_answer = self.answerhistory_set.latest('created')
            previous_answer_text = previous_answer.text if previous_answer else None
            if previous_answer_text != previous_self.text:
                AnswerHistory.objects.create(
                    text=previous_self.text,
                    answer=self,
                )
