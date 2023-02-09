# import the datetime module
import datetime
from django.db import models

# import timezone from django.utils
from django.utils import timezone

# create a Question model with a question_text field of type CharField
# and a pub_date field of type DateTimeField
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # determine if the question was published recently
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text
    

# create a Choice model with a choice_text field of type CharField
# and a votes field of type IntegerField
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
