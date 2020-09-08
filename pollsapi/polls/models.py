from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.question_text

class Choices(models.Model):
    choice_text = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choice')

    def __str__(self):
        return self.choice_text