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
        super(Answer, self).save(*args, **kwargs)
        self._capture_history()

    def _capture_history(self):
        previous_answer = self.answerhistory_set.first()
        previous_text = previous_answer.text if previous_answer else None
        if previous_text != self.text:
            AnswerHistory.objects.create(
                text=self.text,
                answer=self,
            )
