import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):

    question_asked = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date published")

    class Meta:
        ordering = ("-pub_date",)

    def __str__(self):
        return self.question_asked

    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="choices")
    choice_asked = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:
        ordering = ("votes",)

    def __str__(self):
        return self.choice_asked
