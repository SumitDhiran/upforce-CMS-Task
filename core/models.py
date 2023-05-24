from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    POST_TYPE = (
        ('Private','Private'),
        ('Public','Public'),
    )
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    content = models.TextField()
    type = models.CharField(max_length=200, choices=POST_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.title)

    @property
    def total_likes(self)-> 'Like':
        return self.like_set.filter(value='Like').count

    @property
    def total_dislikes(self)-> 'Like':
        return self.like_set.filter(value='Dislike').count

    @property
    def total_vote_count(self)-> 'Like':
        return self.like_set.all().count

class Like(models.Model):
    VOTE_TYPE = (
        ("Like","Like"),
        ("Dislike","Dislike"),
    )
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        unique_together = ('post','user',)