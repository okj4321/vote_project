from django.db import models

# Create your models here.

class Question(models.Model):
    question_text1 = models.CharField(max_length=200)
    question_text2 = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    votes_qestion1 = models.IntegerField(default=0)
    votes_qestion2 = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text1 