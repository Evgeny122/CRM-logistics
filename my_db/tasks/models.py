from django.db import models
from django.conf import settings
from profiles.models import UserInformation
User = settings.AUTH_USER_MODEL

STATUS_TASKS = (
    ('Новая','Новая'),
    ('Грузоперевозка','Грузоперевозка'),
    ('Выгружена', 'Выгружена'),
)



class Likes(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    like = models.BooleanField(default=False)
    

class Dnot_likes(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    dnot_like = models.BooleanField(default=False)
    

class Comments(models.Model):
    class Meta:
        ordering = ['-date']
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    

class Tasks(models.Model):
    class Meta:
        ordering = ['-date']
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    logist = models.ForeignKey(UserInformation, null=True, limit_choices_to={'post' : 'Логист'}, on_delete=models.SET_NULL, related_name='logistic_tasks')
    route = models.CharField(max_length=25)
    cargo = models.TextField()
    price_client = models.IntegerField(default=0)
    status = models.CharField(max_length=30, choices=STATUS_TASKS, default='Новая')
    transport_requirement = models.CharField(max_length=25)
    date = models.DateTimeField(auto_now_add=True)
    commentary = models.ManyToManyField(Comments)
    likes = models.ManyToManyField(Likes)
    dnot_likes = models.ManyToManyField(Dnot_likes)
    image_like = models.ImageField(
        upload_to='image_likes/',
        default='image_likes/like.png',
        null=True,
        blank=True)
    image_dlike = models.ImageField(
        upload_to='image_likes/',
        default='image_likes/dlike.png',
        null=True,
        blank=True)

    def __str__(self):
        return f"№{self.id} {self.route}"

    def count_comments(self):
        return self.commentary.count()
    

    def get_likes(self):
        return self.likes.count()
    
    def get_dont_likes(self):
        return self.dnot_likes.count()

