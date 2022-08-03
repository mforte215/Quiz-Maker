from django.db import models
from django.utils.text import slugify
import uuid

class Quiz(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=400, blank=False, null=False)
    header_image_url = models.URLField(blank=False, null=False)
    published_date = models.DateField(auto_now_add=True, editable=False)
    draft = models.BooleanField(default=True)
    top_post = models.BooleanField(default=False)
    teaser_text = models.TextField(max_length=300, default='')
    slug = models.SlugField(unique=True, db_index=True, blank=True, max_length=255)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Quiz, self).save(*args, **kwargs)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=350)
    correct_answer = models.CharField(max_length=350, default='')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.choice_text

class ScoreRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    score = models.IntegerField()
    user_name = models.CharField(max_length=75, default='')
    quiz = models.ForeignKey(Quiz, related_name='scorerecords', on_delete=models.CASCADE, null=True)