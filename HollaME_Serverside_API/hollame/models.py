from django.db import models

# Create your models here.
class Post(models.Model):
    post_type_enum = [
        ('POST', 'Post'),
        ('COMMENT', 'Comment')
    ]

    body = models.TextField(blank=False)
    views = models.IntegerField(default=0, blank=True)
    likes = models.IntegerField(default=0, blank=True)
    shares = models.IntegerField(default=0, blank=True)
    comment_count = models.IntegerField(default=0, blank=True)
    post_type = models.CharField(choices=post_type_enum, blank=False)
    tags = models.TextField(blank=True)
    # .. attached_to
    author = models.ForeignKey('users.models.CustomUser', related_name='posts', on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)