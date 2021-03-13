from django.db import models

class Question(models.Model):
    title = models.CharField(verbose_name="Название вопроса",max_length=64)
    publication_date = models.DateTimeField(verbose_name="Дата публикации")
    question_text = models.TextField(verbose_name="Текст вопроса",)

class Choise(models.Model):
    chois_text = models.CharField(verbose_name="Текст ответа",max_length=64)
    votes = models.IntegerField(verbose_name="Всего ответов", default=0)
    question = models.ForeignKey(Question,verbose_name="Вопрос", on_delete=models.CASCADE)