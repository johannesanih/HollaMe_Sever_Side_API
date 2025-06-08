from django.db import models
from users.models import CustomUser

#post
#messages
#notifications

# Create your models here.
class Post(models.Model):
    post_type_enum = [
        ('POST', 'Post'),
        ('COMMENT', 'Comment')
    ]

    content = models.TextField(blank=False)
    post_type = models.CharField(choices=post_type_enum, blank=False)
    child_post = models.ForeignKey(
        'self',
        related_name = 'threads',
        on_delete=models.SET_NULL,
        null = True,
        blank = True
    )
    author = models.ForeignKey(CustomUser, related_name='posts', on_delete=models.CASCADE)
    appearance_count = models.IntegerField(default=0)
    likes = models.ManyToManyField(
        CustomUser,
        related_name = 'liked_posts',
        blank = True,
        through = 'PostLike'
    )
    shares = models.ManyToManyField(
        CustomUser,
        related_name = 'shared_posts',
        blank = True,
        through = 'PostShare'
    )
    seen_by = models.ManyToManyField(
        CustomUser,
        related_name = 'seen_posts',
        blank = True,
        through = 'PostSeen'
    )
    user_tags = models.ManyToManyField(
        CustomUser,
        related_name = 'tagged_in_posts',
        blank = True,
        through = 'PostUserTag'
    )
    posted_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return f"HollaMe {self.post_type} - \"{self.content[:30]} ...\" - {self.author.username}"

class PostUserTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tagged_on = models.DateTimeField(auto_now_add=True)

class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    liked_on = models.DateTimeField(auto_now_add=True)

class PostShare(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    shared_on = models.DateTimeField(auto_now_add=True)

class PostSeen(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    seen_on = models.DateTimeField(auto_now_add=True)