from django.db import models


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

class UserModel(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def _str_(self):
        return self.name

#class Simulation(models.Model):
