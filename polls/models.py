import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):

    question_asked = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date published")

    class Meta:
        ordering = ("pub_date",)

    def __str__(self):
        return self.question_asked

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="choices")
    choice_asked = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:
        ordering = ("votes",)

    def __str__(self):
        return self.choice_asked
